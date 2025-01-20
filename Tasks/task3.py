# 3

from bs4 import BeautifulSoup
import time
from textblob import TextBlob
from Tasks.helper import is_valid_url


# Function to get SERP results for keywords and sentiment analysis of the mentions


def sentiment_analysis_mentions(keyword, main_domain, driver):

    # Open Google
    driver.get('https://www.google.com/search?q=' + keyword)

    driver.implicitly_wait(2)  # wait for results to load
    time.sleep(5)

    # Get page source and parse with BeautifulSoup
    soup = BeautifulSoup(driver.page_source, 'html.parser')

    # Extract links and snippets from search results
    results = []
    for index, a_tag in enumerate(soup.find_all('a', href=True)):
        link = a_tag['href']
        # Extract the text snippet or title
        snippet = a_tag.get_text()  # Default to link text

        # Check if the link is a valid URL, excluding the main domain
        if main_domain not in link and is_valid_url(link):
            # Analyze sentiment of the snippet
            sentiment = analyze_sentiment(snippet)
            # Store rank, link, snippet, and sentiment
            results.append((index + 1, link, snippet, sentiment))

    return {"data": results}

# Function to perform sentiment analysis using TextBlob


def analyze_sentiment(text):
    # Perform sentiment analysis using TextBlob
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity

    # Determine sentiment label based on polarity
    if polarity > 0:
        return "Positive"
    elif polarity < 0:
        return "Negative"
    else:
        return "Neutral"
