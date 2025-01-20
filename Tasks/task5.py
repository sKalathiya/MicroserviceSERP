# 5
from selenium import webdriver
import whois
import time
from bs4 import BeautifulSoup
from urllib.parse import urlparse

from Tasks.helper import is_valid_url

# Function to check if the URL is secure (HTTPS)


def is_https(url):
    return url.lower().startswith("https://")

# Function to get domain age using whois


def get_domain_age(url):
    try:
        domain = urlparse(url).netloc
        w = whois.whois(domain)
        creation_date = w.creation_date
        if isinstance(creation_date, list):
            creation_date = creation_date[0]
        if creation_date:
            # age in years
            return (time.time() - creation_date.timestamp()) / (60 * 60 * 24 * 365)
        else:
            return 0
    except Exception:
        return 0  # Return 0 if age is unavailable


# Function to extract external backlinks from SERP and analyze domain metrics
def scrap_serp(keyword, main_domain, driver):

    # Open Google
    driver.get('https://www.google.com/search?q=' + keyword)

    driver.implicitly_wait(2)  # wait for results to load
    time.sleep(5)

    # Get page source and parse with BeautifulSoup
    soup = BeautifulSoup(driver.page_source, 'html.parser')

    # Extract links from search results
    results = []
    for index, a_tag in enumerate(soup.find_all('a', href=True)):
        link = a_tag['href']
        # Check if the link is a valid external URL, excluding the main domain
        if is_valid_url(link) and main_domain not in link:
            # Analyze the domain metrics for the backlink
            domain_metrics = analyze_domain_metrics(link)
            # Store rank, link, and domain metrics
            results.append((index + 1, link, domain_metrics))

    return {"data": results}

# Function to analyze domain metrics (HTTPS, Age)


def analyze_domain_metrics(url):
    domain_metrics = {}

    # Check for HTTPS usage
    domain_metrics['HTTPS'] = is_https(url)

    # Get domain age (in years)
    domain_metrics['Age (years)'] = get_domain_age(url)

    # Estimate authority based on these heuristics
    authority_score = domain_metrics['HTTPS'] * 0.45 + \
        min(domain_metrics['Age (years)'], 20) * 0.55
    domain_metrics['Estimated Authority Score'] = round(authority_score, 2)

    return domain_metrics
