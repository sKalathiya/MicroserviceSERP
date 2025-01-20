# 9
from selenium import webdriver
import time
from bs4 import BeautifulSoup


# Function to scrape SERP and track Google My Business visibility


def track_gmb_visibility(keyword, driver):

    # Open Google
    driver.get('https://www.google.com/search?q=' + keyword)

    driver.implicitly_wait(2)  # wait for results to load
    time.sleep(5)

    # Get page source and parse with BeautifulSoup
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    results = []

    # Extract the elements for GMB visibility
    # <div> or <g-card>
    # Look for local pack listings
    for gmb_section in soup.find_all('div', class_='l5LxJc'):

        business_name = gmb_section.find('div', class_='dbg0pd').get_text(
        ) if gmb_section.find('div', class_='dbg0pd') else 'N/A'

        results.append(business_name)

    # Display the results
    return {"data": results}
