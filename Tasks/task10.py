# 10
from urllib.parse import urlparse
from selenium import webdriver
import time
from bs4 import BeautifulSoup

from Tasks.helper import is_valid_url


# Function to scrape SERP and detect event-related backlinks


def detect_event_backlinks(event_keyword, main_domain, driver):

    event_backlinks = []

    # Open Google
    driver.get('https://www.google.com/search?q=' + event_keyword)

    driver.implicitly_wait(2)  # wait for results to load
    time.sleep(5)

    # Get the page source and parse with BeautifulSoup
    soup = BeautifulSoup(driver.page_source, 'html.parser')

    # Extract all links from the page (backlinks)
    # A typical container for search result links
    for result in soup.find_all('div', class_='tF2Cxc'):
        link = result.find('a', href=True)['href']
        if main_domain not in link and is_valid_url(link):
            event_backlinks.append(link)

    # Return the list of event-related backlinks
    return {"data": event_backlinks}
