# 15
from urllib.parse import urlparse
from selenium import webdriver
from bs4 import BeautifulSoup
import time

# Function to scrape SERP and get backlinks


def scrape_backlinks(keyword, main_domain, driver):
    backlinks = []

    # Open Google
    driver.get('https://www.google.com/search?q=' + keyword)

    driver.implicitly_wait(2)  # wait for results to load
    time.sleep(5)
    # Get page source and parse with BeautifulSoup
    soup = BeautifulSoup(driver.page_source, 'html.parser')

    # Extract all result links from the page (backlinks)
    # Container for each search result
    for result in soup.find_all('div', class_='tF2Cxc'):
        link_tag = result.find('a', href=True)
        if link_tag:
            url = link_tag['href']
            domain = urlparse(url).netloc

            # Filter out results from the main domain
            if domain != main_domain:
                title = result.find('h3').get_text(
                ) if result.find('h3') else 'N/A'

                backlinks.append({
                    'backlink_url': url,
                    'backlink_title': title,
                    'backlink_domain': domain,
                })

    return backlinks

# Function to compare backlinks between your brand and competitors


def compare_backlinks(brand_keyword, competitor_keyword, brand_domain, competitor_domain, driver):
    # Scrape backlinks for both brand and competitors
    brand_backlinks = scrape_backlinks(brand_keyword, brand_domain, driver)
    competitor_backlinks = scrape_backlinks(
        competitor_keyword, competitor_domain, driver)
    return {"data": {"brand": brand_backlinks, "competitor": competitor_backlinks}}
