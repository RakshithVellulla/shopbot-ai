# 🛍️ ShopBot AI — E-commerce Shopping Assistant

An agentic AI chatbot for an online electronics store built with 
Python, Streamlit, and Groq API (Llama 3.3).

---

## What Problem It Solves

Online shoppers struggle to find the right product within their 
budget. ShopBot acts as a personal shopping assistant that 
understands natural language, searches a real product catalog, 
and gives grounded recommendations — no hallucinations.

---

## How It Works

ShopBot uses a two-stage agentic pipeline:

1. **Intent Detection** — LLM classifies the user message into 
   RECOMMEND, COMPARE, FAQ, or GENERAL
2. **Catalog Search** — Filters product database by category, 
   price range, and keywords
3. **Grounded Response** — LLM responds using only real catalog 
   data, not training data

---

## Tech Stack

| Tool | Purpose |
|---|---|
| Python | Core language |
| Groq API + Llama 3.3 | LLM provider |
| Streamlit | Chat UI |
| python-dotenv | Secure API key management |

---

## Features

- Product recommendation by budget and category
- Side by side product comparison  
- Store policy FAQ (shipping, returns, payment)
- Conversation memory across the session
- Out of stock detection
- Intent detection badge showing agent decisions

---

## How to Run Locally

1. Clone the repo
   git clone https://github.com/RakshithVellulla/shopbot-ai.git

2. Create virtual environment
   python -m venv venv
   venv\Scripts\activate

3. Install dependencies
   pip install -r requirements.txt

4. Add your API key
   Create .env file:
   GROQ_API_KEY=your_key_here

5. Run the app
   streamlit run app.py

---

## Challenges Encountered

- Model deprecation — llama3-8b-8192 was deprecated, 
  switched to llama-3.3-70b-versatile
- Malformed JSON from intent detection — added fallback handler
- Streamlit rerun behavior — used st.session_state for memory
- API key formatting — trailing whitespace caused auth failures

---

## Architecture

User Message → Intent Detection (LLM Call 1) → 
Product Search → Grounded Response (LLM Call 2) → 
Streamlit UI
