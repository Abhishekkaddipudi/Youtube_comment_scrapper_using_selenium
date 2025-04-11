# Youtube_comment_scrapper_using_selenium



```markdown
# 📺 YouTube Comment Scraper + LLM Analysis via Ollama

A Python-based automation tool to scrape YouTube comments and replies using Selenium, and analyze them with an LLM model (e.g., LLaMA 3) through Ollama's local API.

---

## 🔍 Features

- Scrapes all top-level comments and replies from any YouTube video  
- Saves data in both `.json` and `.txt` formats  
- Integrates with [Ollama](https://ollama.com) for powerful local LLM analysis via API  
- Fully headless operation using Chrome WebDriver  

---

## 🧰 Requirements

- Python 3.8+
- Google Chrome
- ChromeDriver (make sure it's in your PATH)
- Ollama installed and running locally

---

## 📦 Python Libraries

Install required packages:

```bash
pip install selenium requests
```

---

## ⚙️ Ollama Setup

1. **Install Ollama** from: https://ollama.com  
2. **Run a model locally**, e.g., LLaMA 3:

    ```bash
    ollama run llama3
    ```

    *(Or pull the model first if not downloaded: `ollama pull llama3`)*

3. Ollama runs an HTTP API at:  
   `http://localhost:11434`

---

## 🔁 How the Flow Works

1. You run the script and input a YouTube video URL.  
2. Selenium opens the video, scrolls down, and scrapes all comments & replies.  
3. The data is saved to:
   - `youtube_comments_with_replies.json`
   - `youtube_comments_with_replies.txt`
4. The `.txt` version of the data is sent to Ollama’s API as part of a prompt.  
5. Ollama analyzes the feedback using an LLM and returns structured insights.

---

## ▶️ Running the Scraper

```bash
python youtube_scraper.py
```

Then paste a YouTube video URL when prompted.

---

## 🧠 Analyzing Comments with Ollama

Use this companion script to send the `.txt` data to Ollama for analysis:

```python
import requests
from your_module import json_to_text  # assuming you have json_to_text() in a file

url = "http://localhost:11434/api/chat"

payload = {
    "model": "llama3",
    "messages": [
        {
            "role": "user",
            "content": "Act like a data analyst. Here are some YouTube comments and replies. Analyze them:\n\n"
                       + json_to_text("youtube_comments_with_replies.json"),
        }
    ],
}

response = requests.post(url, json=payload, stream=True)

for line in response.iter_lines(decode_unicode=True):
    if line:
        try:
            data = json.loads(line)
            if "message" in data and "content" in data["message"]:
                print(data["message"]["content"], end="")
        except Exception as e:
            print("Error:", e)
```

---

## 📄 Output

- `youtube_comments_with_replies.json`: Raw comment + reply structure  
- `youtube_comments_with_replies.txt`: Readable format for LLM  
- Terminal: Real-time streaming response from the LLM via Ollama

---

## 📌 Notes

- For high-volume videos, increase the scroll attempts in the script.  
- Customize the prompt to guide the LLM for sentiment analysis, topic extraction, etc.  
- You can modify the browser visibility by setting `--headless` to `False`.

---
