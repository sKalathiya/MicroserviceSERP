# 8
from selenium import webdriver
import time
from bs4 import BeautifulSoup
from textblob import TextBlob


# Function to fetch reviews from a review page


def get_reviews_from_url(url, driver):
    driver.get(url)  # error shows because we have not passed any url yet
    driver.implicitly_wait(2)  # wait for results to load
    time.sleep(10)
    soup = BeautifulSoup(driver.page_source, 'html.parser')

    reviews = []
    # Extract review data
    # Modify according to the actual website structure
    for review_tag in soup.find_all('div', class_='review'):
        try:
            review_text = review_tag.find(
                'span', class_='review-text').get_text()
            reviews.append(review_text)
        except AttributeError:
            continue

    return reviews

# Function to perform sentiment analysis on a review


def analyze_sentiment(review_text):
    blob = TextBlob(review_text)
    polarity = blob.sentiment.polarity
    return polarity  # Compound score: -1 to 1

# Function to analyze sentiment trends for reviews from a URL


def analyze_sentiment_trends(url, driver):
    reviews = get_reviews_from_url(url, driver)

    # Perform sentiment analysis for each review
    sentiment_scores = []
    for review in reviews:
        print(review)
        sentiment_score = analyze_sentiment(review)
        sentiment_scores.append(
            {'text': review, 'sentiment_score': sentiment_score})

    return {"data": sentiment_scores}
