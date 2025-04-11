from browser_setup import setup_browser
from scrolling import scroll_to_comments, scroll_to_load_all_comments
from comment_extraction import expand_all_replies, extract_comments_and_replies
from file_operations import count_json_length, save_to_json, save_to_txt
import time


def get_youtube_comments_and_replies(video_url):
    print("[*] Opening YouTube video...")
    driver = setup_browser()
    driver.get(video_url)
    time.sleep(2)

    scroll_to_comments(driver)
    print("[*] Scrolling to load all comments...")
    scroll_to_load_all_comments(driver)

    print("[*] Expanding all replies...")
    expand_all_replies(driver)

    print("[*] Extracting comments and replies...")
    comments_data = extract_comments_and_replies(driver)
    driver.quit()

    # Save data
    save_to_json(comments_data, "youtube_comments_with_replies.json")
    save_to_txt(comments_data, "youtube_comments_with_replies.txt")

    total_comments = count_json_length(comments_data)
    print(f"[✓] Scraped {total_comments} comments with their replies.")
    return comments_data


if __name__ == "__main__":
    video_url = input("Enter the YouTube URL: ")
    get_youtube_comments_and_replies(video_url)
