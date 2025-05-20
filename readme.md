# LLM-Based RAG System 🚀

## 👋 About This Project

This is my completed version of a **Retrieval-Augmented Generation (RAG)** system built using a **Large Language Model (LLM)**. It scrapes content from the web based on user queries, processes it, and generates intelligent, contextual answers in real time.

> ✅ This project was completed as part of an assignment from a GitHub repo. I explored the architecture, understood all components, integrated them, and delivered a fully functional system with a clean modular structure.

---

## 🧠 How It Works

1. **User Input via Streamlit Interface**  
   Users enter a query in the Streamlit-based UI.

2. **Query Sent to Flask Backend**  
   The frontend sends the user query to a Flask backend via an API call.

3. **Internet Search & Content Scraping**  
   The backend performs a search using an API and scrapes content (headings, paragraphs) from the top results.

4. **Text Processing**  
   The scraped content is cleaned and structured to form a coherent prompt for the LLM.

5. **LLM Response Generation**  
   The prompt is passed to an LLM API, and a relevant answer is generated.

6. **Answer Displayed to User**  
   The backend sends the LLM-generated answer back to the frontend for display.

---

## 🌟 Features

- Clean, intuitive UI with Streamlit
- Modular Flask API backend
- Real-time web scraping and context building
- LLM-based answer generation via API
- Environment variable support for secure API key management


---

## 🛠️ Tech Stack

- **Python 3.8+**
- **Flask**
- **Streamlit**
- **LLM APIs (OpenAI, Cohere, etc.)**
- **BeautifulSoup / Requests**
- `.env` for secure key handling

---

## ⚙️ Setup Instructions

### 1. Clone the Repo

git clone https://github.com/Abhi21sar/llm-based-rag-system.git
cd llm-based-rag-system
### 2. Create a Virtual Environment

Using `venv`:

python -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate

### 3. Install Requirements
pip install -r requirements.txt

### 4. Set Up Environment Variables

Create a .env file in the root directory and add your API keys like this:
OPENAI_API_KEY=your_openai_key
SEARCH_API_KEY=your_search_key

### 5. Run the Flask Backend
cd flask_app
python app.py

### 6. Run the Streamlit Frontend

Open a new terminal window:
cd streamlit_app
streamlit run app.py

### 7. Launch the App

Visit http://localhost:8501 in your browser and start asking questions!

### 📁 Project Structure

├── flask_app/         
├── streamlit_app/      
├── .env                
├── requirements.txt     
└── README.md         
