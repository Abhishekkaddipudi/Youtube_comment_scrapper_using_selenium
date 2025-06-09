# Youtube_comment_scrapper_using_selenium



```markdown
# 📺 YouTube Comment Scraper + LLM Analysis via Ollama

A Python-based automation tool to scrape YouTube comments using Selenium, and analyze them with an LLM model (e.g., LLaMA 3) through Ollama's local API.

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
python main.py
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
## 🧪 Example Analysis: KSI Comedy Video Comments
📹 **Video Analyzed:** [KSI Tries Not To Laugh Video](https://www.youtube.com/watch?v=JfUVGBWDJ_M)

After scraping and analyzing the comments from a popular KSI video, here are the key findings based on sentiment, tone, and engagement:

---

### ✅ Positive Sentiment

- Only **2%** of comments express positive sentiment (e.g., "Great job!", "I love this!").
- Most comments are either **neutral or negative**, with a few containing profanity or personal attacks.

---

### ❌ Negative Sentiment

- Over **70%** of comments contain negative words or phrases, such as:
  - Derogatory terms for the creator (e.g., _"bum"_, _"thief"_)
  - Criticisms of the content (e.g., _"boring"_, _"not funny"_)
  - Personal attacks directed at other commenters
- Some are dismissive or apathetic (e.g., _"I don't get it"_)

---

### 🧌 Trolling & Spam

- Around **10%** of comments appear to be **spam or trolling** in nature:
  - (e.g., _"Like none of them were funny"_, _"Let's see your forehead"_)
- Some include **irrelevant or suspicious content** that doesn’t relate to the video.

---

### 💬 Engagement & Participation

- Only about **5%** of commenters **engage in actual conversation** by replying to other comments.
- The majority are **stand-alone reactions** without any follow-up discussion.

---

### 🗣️ Language & Tone

- Language used is **informal**, often **abrasive or dismissive** in tone.
- Multiple comments include **profanities** or **derogatory slurs**.
- Repetition of critiques suggests a common pattern of discontent.

---

### 📉 Content Analysis

- The video's content is seen as **unoriginal and formulaic**:
  - (e.g., _"Man too forced some of these, people just do anything for views"_)
- The creator seems to rely on **shock value** or **cheap laughs** rather than original humor.
- Some comments suggest the **video is outdated** or lacks relevance.

---

### 🔍 Insights & Suggestions

- **Viewer sentiment** is largely **disappointed or unimpressed**, leading to negative feedback.
- The **creator may need to reconsider** their approach to comedy or content strategy.
- **Low engagement** suggests a lack of strong community investment or repeat viewership.

> ⚠️ _Disclaimer: This analysis reflects only the subset of users who left comments on this particular video. It may not represent the opinions of the entire audience._

---

## ⚙️ How to Set Up Ollama Locally

Ollama allows you to run large language models locally with ease.

### 1. 🖥 Install Ollama

Download and install Ollama from the official website:  
👉 [https://ollama.com](https://ollama.com)

Choose your platform (macOS, Linux, Windows) and follow the installer instructions.

### 2. 📦 Pull a Model

You can pull any model like LLaMA 3.2:

```bash
ollama pull llama3.2
