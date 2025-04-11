import time
from config import SCROLL_ATTEMPTS_LIMIT, SCROLL_DELAY


def scroll_to_comments(driver):
    driver.execute_script("window.scrollTo(0, 600);")
    time.sleep(2)


def scroll_to_load_all_comments(driver):
    last_height = driver.execute_script("return document.documentElement.scrollHeight")
    scroll_attempts = 0

    while scroll_attempts < SCROLL_ATTEMPTS_LIMIT:
        driver.execute_script(
            "window.scrollTo(0, document.documentElement.scrollHeight);"
        )
        time.sleep(SCROLL_DELAY)
        new_height = driver.execute_script(
            "return document.documentElement.scrollHeight"
        )
        if new_height == last_height:
            scroll_attempts += 1
        else:
            last_height = new_height
            scroll_attempts = 0
