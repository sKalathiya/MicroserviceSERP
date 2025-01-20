# 2
import time
from bs4 import BeautifulSoup
from Tasks.helper import is_valid_url


# Function to rank Google search results for a brand keywords


def rank_tracking(keyword, main_domain, driver):
    try:
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
            # Check if the link exclude the main domain
            if main_domain not in link and is_valid_url(link):
                # Store rank (index + 1) and link
                results.append((index + 1, link))

        return {"data": results}
    except Exception as e:
        print(f"Error detecting backlinks: {e}")
        return {"data": []}
