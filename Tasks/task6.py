# 6

from selenium import webdriver
import time
from bs4 import BeautifulSoup
import requests
from Tasks.helper import is_valid_url
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


# Function to fetch content from a URL using BeautifulSoup
def get_page_content(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            # Extract text content (ignoring scripts and styles)
            content = ' '.join([p.get_text() for p in soup.find_all('p')])
            return content
        else:
            return ''
    except requests.exceptions.RequestException:
        return ''

# Function to scrape external backlinks from SERP results


def scrape_serp_backlinks(keyword, main_domain, driver):
    backlinks = []

    # Open Google
    driver.get('https://www.google.com/search?q=' + keyword)

    driver.implicitly_wait(2)  # wait for results to load
    time.sleep(5)

    # Get page source and parse with BeautifulSoup
    soup = BeautifulSoup(driver.page_source, 'html.parser')

    # Extract external backlinks (excluding main domain)
    for a_tag in soup.find_all('a', href=True):
        link = a_tag['href']
        if is_valid_url(link) and main_domain not in link:
            backlinks.append(link)

    return backlinks

# Function to calculate keyword relevance for external backlinks


def analyze_keyword_relevance(keyword, backlinks):

    # Get content for each backlink
    documents = [get_page_content(url) for url in backlinks]

    # Apply TF-IDF Vectorizer to calculate term relevance
    vectorizer = TfidfVectorizer(stop_words='english')
    tfidf_matrix = vectorizer.fit_transform([keyword] + documents)

    # Calculate cosine similarity between keywords and each document
    cosine_similarities = cosine_similarity(
        tfidf_matrix[0:1], tfidf_matrix[1:])

    # Store the relevance scores (cosine similarities)
    relevance_scores = {backlink: similarity[0] for backlink, similarity in zip(
        backlinks, cosine_similarities.T)}

    return relevance_scores

# function to start both the above functions


def analyze_backlink_relevance(keyword, main_domain, driver):
    # generate backlinks
    backlinks = scrape_serp_backlinks(keyword, main_domain, driver)

    # Analyze keyword relevance
    relevance_scores = analyze_keyword_relevance(keyword, backlinks)

    return {"data": relevance_scores}
