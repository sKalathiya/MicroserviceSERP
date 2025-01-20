from urllib.parse import urlparse
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
# Function to validate and normalize URL


def is_valid_url(url):
    try:
        # Normalize URL: Remove "www" and check if the URL is valid
        parsed_url = urlparse(url)
        if parsed_url.scheme in ['http', 'https']:
            # Check if the URL starts with "www" and remove it
            if parsed_url.netloc.startswith("www."):
                parsed_url = parsed_url._replace(netloc=parsed_url.netloc[4:])
            return True
    except Exception:
        return False
    return False


def getDriver():
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Run in headless mode
    # Recommended for headless mode
    chrome_options.add_argument("--disable-gpu")
    # Avoid issues in certain environments
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument(
        "--disable-dev-shm-usage")  # Reduce memory issues
    # Set up Selenium WebDriver
    return webdriver.Chrome(options=chrome_options)
