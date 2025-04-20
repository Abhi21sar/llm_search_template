from flask import Flask, request, jsonify
from dotenv import load_dotenv
import os
import openai

from utils import search_articles, concatenate_content, generate_answer

# Load environment variables
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")
app = Flask(__name__)

@app.route('/query', methods=['POST'])
def query():
    try:
        data = request.get_json()
        user_query = data.get("query", "")
        print("✅ Received query:", user_query)

        # Step 1: Search articles
        articles = search_articles(user_query)
        print("🔍 Found articles:", articles)

        # Step 2: Scrape and concatenate content
        content = concatenate_content(articles)
        print("📚 Combined content length:", len(content))

        # Step 3: Generate answer
        answer = generate_answer(content, user_query)
        print("🧠 Answer generated:\n", answer)

        return jsonify({"answer": answer})

    except Exception as e:
        print("❌ Backend Exception:", e)
        return jsonify({"answer": "Sorry, there was an error generating the answer."}), 500

if __name__ == '__main__':
    app.run(host='localhost', port=5001)