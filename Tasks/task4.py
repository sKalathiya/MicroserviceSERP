# 4
from Tasks.helper import is_valid_url
import spacy
from selenium import webdriver
from bs4 import BeautifulSoup
import time


# Load spaCy model
nlp = spacy.load("en_core_web_sm")

# Function to evaluate anchor text relevance using spaCy


def evaluate_relevance(anchor_text, keyword):

    # Process both the anchor text and keyword using spaCy
    anchor_doc = nlp(anchor_text)
    keyword_doc = nlp(keyword)

    # Check similarity between anchor text and keyword
    similarity_score = anchor_doc.similarity(keyword_doc)

    # Return the similarity score and the entities found
    return similarity_score


# Function to get SERP rank for brand-related keywords excluding the main domain and to evaluate the anchor text


def evaluate_anchor_SERP(keyword, main_domain, driver):

    # Open Google
    driver.get('https://www.google.com/search?q=' + keyword)

    driver.implicitly_wait(2)  # wait for results to load
    time.sleep(5)

    # Get page source and parse with BeautifulSoup
    soup = BeautifulSoup(driver.page_source, 'html.parser')

    # Extract links and anchor texts from search results
    results = []
    for index, a_tag in enumerate(soup.find_all('a', href=True)):
        link = a_tag['href']
        anchor_text = a_tag.get_text()  # Extract anchor text

        # Check if the link is a valid URL, excluding the main domain
        if main_domain not in link and is_valid_url(link):
            similarity_score = evaluate_relevance(
                anchor_text, keyword)  # Evaluate anchor text relevance
            # Store rank, link, anchor text, and score
            results.append((index + 1, link, anchor_text, similarity_score))

    return {"data": results}
