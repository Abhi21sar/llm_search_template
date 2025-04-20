import os
from dotenv import load_dotenv
import openai
import requests
from bs4 import BeautifulSoup
from duckduckgo_search import ddg

load_dotenv()
SERPER_API_KEY = os.getenv("SERPER_API_KEY")
OPENAI_API_KEY = os.getenv("Your_OPENAI_API_KEY")
openai.api_key = OPENAI_API_KEY

def search_articles(query):
    """
    Searches for articles related to the query using DuckDuckGo.
    Returns a list of dictionaries with URL and snippet.
    """
    print(f"Searching articles for: {query}")
    results = ddg(query, max_results=5)
    articles = [{"url": result["href"], "title": result["title"]} for result in results]
    return articles


def fetch_article_content(url):
    """
    Fetches the article content from a URL.
    """
    try:
        response = requests.get(url, timeout=5)
        soup = BeautifulSoup(response.text, 'html.parser')

        # Grab relevant tags for meaningful content
        text_parts = []
        for tag in soup.find_all(['h1', 'h2', 'h3', 'p']):
            text_parts.append(tag.get_text(strip=True))

        return "\n".join(text_parts)
    except Exception as e:
        print(f"Error fetching content from {url}: {e}")
        return ""

def concatenate_content(articles):
    """
    Loops through article URLs and collects all content.
    """
    print("Concatenating article content...")
    full_text = ""
    for article in articles:
        url = article["url"]
        content = fetch_article_content(url)
        if content:
            full_text += f"\n--- Article: {url} ---\n{content}\n"
    return full_text


def generate_answer(content, query):
    """
    Uses OpenAI GPT to answer based on given content and query.
    """
    prompt = f"""You are an expert assistant. Based on the context below, answer the user's question.

Context:
{content}

Question: {query}

Answer:"""

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7,
            max_tokens=1000
        )
        return response['choices'][0]['message']['content']
    except Exception as e:
        print("OpenAI error:", e)
        return "Sorry, there was an error generating the answer."
