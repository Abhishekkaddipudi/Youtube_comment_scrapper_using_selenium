from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def setup_browser(headless=True):
    options = Options()
    if headless:
        options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    options.add_argument("--log-level=3")
    return webdriver.Chrome(options=options)
