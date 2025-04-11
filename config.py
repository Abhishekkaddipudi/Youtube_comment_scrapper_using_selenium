from file_operations import json_to_text

SCROLL_ATTEMPTS_LIMIT = 3
SCROLL_DELAY = 3
EXPAND_DELAY = 1
COMMENT_EXTRACTION_DELAY = 1

llm_url = "http://localhost:11434/api/chat"
# payload
payload = {
    "model": "llama3.2",
    "messages": [
        {
            "role": "user",
            "content": "Imagine yourself as a data analyst for a YouTube channel. Analyze the following comments and replies and provide insights:\n\n"
            + json_to_text("youtube_comments_with_replies.json"),
        }
    ],
}
