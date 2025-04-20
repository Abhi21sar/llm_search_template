# This file is intentionally left empty. It indicates that this directory is a package.
from flask import Flask, request, jsonify
from flask_cors import CORS
from dotenv import load_dotenv
import os
from utils import search_articles, concatenate_content, generate_answer

load_dotenv()
app = Flask(__name__)
CORS(app)

@app.route('/query', methods=['POST'])
def query():
    data = request.get_json()
    user_query = data.get("query", "")

    print("Received query:", user_query)

    # Pipeline: Search → Combine → Answer
    articles = search_articles(user_query)
    content = concatenate_content(articles)
    answer = generate_answer(content, user_query)

    return jsonify({"answer": answer})

if __name__ == '__main__':
    app.run(host='localhost', port=5001)