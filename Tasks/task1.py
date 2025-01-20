# 1

from bs4 import BeautifulSoup
import time


from Tasks.helper import is_valid_url


# Function to get Google search results for a brand


def detect_backlinks(query, main_domain, driver):
    try:
        # Open Google
        driver.get('https://www.google.com/search?q=' + query)

        driver.implicitly_wait(2)  # wait for results to load
        time.sleep(5)
        # Get page source and parse with BeautifulSoup
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        # Extract links from search results
        if soup:
            links = [a['href'] for a in soup.find_all(
                'a', href=True) if main_domain not in a['href'] and is_valid_url(a['href'])]
            return {"backlinks": links}
        else:
            return {"backlinks": []}
    except Exception as e:
        print(f"Error detecting backlinks: {e}")
        return {"backlinks": []}
