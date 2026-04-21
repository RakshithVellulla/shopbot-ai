from groq import Groq
from dotenv import load_dotenv
from products import search_products, format_products_for_llm
import streamlit as st
import json
import os

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

# ── SYSTEM PROMPT ──
SYSTEM_PROMPT = """
You are ShopBot, a friendly and knowledgeable AI shopping assistant 
for an online electronics store.

You can help users with three things:
1. FIND & RECOMMEND products based on their needs and budget
2. COMPARE two or more products side by side
3. ANSWER FAQs about shipping, returns, and store policies

Store Policies:
- Shipping: Free shipping on orders over $50. Standard delivery 3-5 days.
- Returns: 30 day return policy. Item must be unused and in original packaging.
- Payment: We accept Visa, Mastercard, PayPal and Apple Pay.

Rules you must follow:
- Only answer questions related to shopping and our store
- If someone asks something unrelated, politely say you can only help with shopping
- Always ask clarifying questions if the user's budget or needs are unclear
- Be concise and helpful
- When product data is provided to you, ONLY recommend those products
- Never make up products that are not in the provided data
"""

# ── INTENT DETECTION ──
def detect_intent(user_message):
    """
    Ask the LLM to classify what the user wants.
    Returns a structured JSON with intent and extracted filters.
    """
    prompt = f"""
    Analyze this user message and extract structured information.
    
    User message: "{user_message}"
    
    Available categories: Laptops & Computers, Phones & Tablets, 
    Headphones & Audio, Gaming, Smart Home, Accessories & Cables, 
    Cameras & Webcams, TVs & Monitors
    
    Respond ONLY with a JSON object in this exact format, nothing else:
    {{
        "intent": "RECOMMEND" or "COMPARE" or "FAQ" or "GENERAL",
        "category": "category name or null",
        "max_price": number or null,
        "min_price": number or null,
        "query": "keyword to search or null"
    }}
    """

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}],
        temperature=0  # 0 = more deterministic, better for classification
    )

    raw = response.choices[0].message.content.strip()

    try:
        return json.loads(raw)
    except json.JSONDecodeError:
        # If LLM didn't return clean JSON, default to GENERAL
        return {"intent": "GENERAL", "category": None, 
                "max_price": None, "min_price": None, "query": None}


# ── AGENTIC RESPONSE ──
def get_response(user_message, conversation_history):
    """
    The brain of ShopBot.
    Detects intent → fetches relevant data → responds intelligently.
    """

    # Step 1 — Detect what the user wants
    intent_data = detect_intent(user_message)
    intent = intent_data.get("intent", "GENERAL")

    # Step 2 — Act based on intent
    product_context = ""

    if intent in ["RECOMMEND", "COMPARE"]:
        # Search the catalog with extracted filters
        results = search_products(
            query=intent_data.get("query"),
            category=intent_data.get("category"),
            max_price=intent_data.get("max_price"),
            min_price=intent_data.get("min_price")
        )
        
        if results:
            product_context = f"""
            Here are the relevant products from our catalog:
            
            {format_products_for_llm(results)}
            
            Use ONLY these products in your response.
            """
        else:
            product_context = """
            No products found matching those criteria. 
            Let the user know and ask if they want to adjust their budget or preferences.
            """

    # Step 3 — Build the messages with context
    messages = [
        {"role": "system", "content": SYSTEM_PROMPT}
    ]

    # Add conversation history
    messages += conversation_history

    # Add product context if we have it
    if product_context:
        messages.append({
            "role": "system",
            "content": product_context
        })

    # Add current user message
    messages.append({
        "role": "user",
        "content": user_message
    })

    # Step 4 — Get the final response
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=messages
    )

    return response.choices[0].message.content, intent


# ── STREAMLIT UI ──
st.set_page_config(page_title="ShopBot AI", page_icon="🛍️")
st.title("🛍️ ShopBot AI")
st.caption("Your personal electronics shopping assistant")

# Initialize session state
if "messages" not in st.session_state:
    st.session_state.messages = []
    st.session_state.messages.append({
        "role": "assistant",
        "content": "Hi! I'm ShopBot 🛍️ I can help you find electronics, compare products, or answer questions about shipping and returns. What are you looking for today?"
    })

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat input
if user_input := st.chat_input("Ask me anything about our products..."):

    # Show user message
    with st.chat_message("user"):
        st.markdown(user_input)

    st.session_state.messages.append({
        "role": "user",
        "content": user_input
    })

    # Get agentic response
    with st.chat_message("assistant"):
        with st.spinner("ShopBot is thinking..."):
            reply, intent = get_response(
                user_input,
                st.session_state.messages[:-1]  # history without current message
            )
            st.markdown(reply)
            # Show intent badge so you can see the agent working
            st.caption(f"🤖 Intent detected: `{intent}`")

    st.session_state.messages.append({
        "role": "assistant",
        "content": reply
    })