from selenium.webdriver.common.by import By
import time
from config import EXPAND_DELAY, COMMENT_EXTRACTION_DELAY


def expand_all_replies(driver):
    expanders = driver.find_elements(
        By.XPATH, "//div[contains(@class, 'more-button') and @aria-expanded='false']"
    )

    for idx, expander in enumerate(expanders):
        try:
            button = expander.find_element(By.XPATH, ".//button")
            driver.execute_script(
                "arguments[0].scrollIntoView({block: 'center'});", button
            )
            time.sleep(EXPAND_DELAY)
            button.click()
            time.sleep(EXPAND_DELAY)
        except Exception as e:
            print(f"Could not click button {idx+1}: {e}")


def extract_comments_and_replies(driver):
    comments_data = []
    threads = driver.find_elements(By.XPATH, "//ytd-comment-thread-renderer")

    for thread in threads:
        try:
            # Top-level comment
            main_comment = thread.find_element(By.ID, "content-text").text.strip()
            main_author = thread.find_element(By.ID, "author-text").text.strip()
            replies = extract_replies(thread)

            comments_data.append(
                {"author": main_author, "comment": main_comment, "replies": replies}
            )
        except Exception as e:
            print(f"Error extracting comment block: {e}")
            continue

    return comments_data


def extract_replies(thread):
    replies = []
    reply_section = thread.find_elements(By.XPATH, ".//ytd-comment-replies-renderer")

    if reply_section:
        # Find all reply elements within the replies section
        reply_elements = reply_section[0].find_elements(
            By.XPATH, ".//ytd-comment-view-model"
        )

        for reply in reply_elements:
            try:
                reply_author_el = reply.find_element(
                    By.XPATH, ".//a[@id='author-text']"
                )
                reply_text_el = reply.find_element(
                    By.XPATH, ".//yt-attributed-string[@id='content-text']"
                )
                reply_author = reply_author_el.text.strip()
                reply_comment = reply_text_el.text.strip()

                if reply_comment and reply_author:
                    replies.append({"author": reply_author, "comment": reply_comment})
            except:
                continue

    return replies
