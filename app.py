import streamlit as st
from llm import get_llm_response
from prompts import *
from utils import is_valid_name, is_valid_email, is_valid_phone, analyze_sentiment

# 1. PAGE CONFIG
st.set_page_config(page_title="TalentScout Hiring Assistant", layout="wide")

# 2. SESSION STATE INITIALIZATION
if "stage" not in st.session_state:
    st.session_state.stage = "name"

if "messages" not in st.session_state:
    st.session_state.messages = []

if "candidate" not in st.session_state:
    st.session_state.candidate = {
        "name": "",
        "email": "",
        "phone": "",
        "experience": "",
        "position": "",
        "location": "",
        "tech_stack": "",
        "sentiment": ""
    }

# 3. SIDEBAR SUMMARY
with st.sidebar:
    st.header("⚙️ Settings")
    language = st.selectbox("Language", ["English", "Hindi", "Spanish", "French"])
    
    st.divider()
    st.header("📋 Candidate Profile")
    for k, v in st.session_state.candidate.items():
        if v:
            st.write(f"**{k.replace('_', ' ').capitalize()}**: {v}")

SYSTEM = system_prompt(language)

# 4. INITIAL GREETING
if len(st.session_state.messages) == 0:
    greeting = (
        "Hello! 👋 Welcome to TalentScout.\n\n"
        "I am an AI Hiring Assistant. I'll help you through the initial screening.\n\n"
        "To begin, may I please know your **full name**?"
    )
    st.session_state.messages.append({"role": "assistant", "content": greeting})

# 5. UI DISPLAY
st.title("🤖 TalentScout Hiring Assistant")
st.caption("Streamlining technology recruitment through AI")

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# 6. USER INPUT PROCESSING
user_input = st.chat_input("Type your response here...")

if user_input:
    # Handle Exit Keywords
    if user_input.lower() in ["exit", "quit", "bye", "stop"]:
        st.session_state.messages.append({"role": "user", "content": user_input})
        st.session_state.messages.append({"role": "assistant", "content": "Interview terminated. Goodbye!"})
        st.session_state.stage = "end"
        st.rerun()

    # Show user message immediately
    st.session_state.messages.append({"role": "user", "content": user_input})
    
    # 7. CONVERSATION LOGIC (STATE MACHINE)
    reply = ""

    # ---- NAME ----
    if st.session_state.stage == "name":
        if not is_valid_name(user_input):
            reply = "Please enter your **full name** (First and Last name required)."
        else:
            st.session_state.candidate["name"] = user_input
            st.session_state.stage = "email"
            reply = INFO_PROMPTS["email"]

    # ---- EMAIL ----
    elif st.session_state.stage == "email":
        if not is_valid_email(user_input):
            reply = "⚠️ That email doesn't look right. Please provide a valid address (e.g., name@email.com)."
        else:
            st.session_state.candidate["email"] = user_input
            st.session_state.stage = "phone"
            reply = INFO_PROMPTS["phone"]

    # ---- PHONE ----
    elif st.session_state.stage == "phone":
        if not is_valid_phone(user_input):
            reply = "⚠️ Please provide a valid **numeric** phone number (10-13 digits)."
        else:
            st.session_state.candidate["phone"] = user_input
            st.session_state.stage = "experience"
            reply = INFO_PROMPTS["experience"]

    # ---- EXPERIENCE ----
    elif st.session_state.stage == "experience":
        st.session_state.candidate["experience"] = user_input
        st.session_state.stage = "position"
        reply = INFO_PROMPTS["position"]

    # ---- POSITION ----
    elif st.session_state.stage == "position":
        st.session_state.candidate["position"] = user_input
        st.session_state.stage = "location"
        reply = INFO_PROMPTS["location"]

    # ---- LOCATION ----
    elif st.session_state.stage == "location":
        st.session_state.candidate["location"] = user_input
        st.session_state.stage = "tech"
        reply = TECH_STACK_PROMPT

    # ---- TECH STACK & QUESTION GENERATION ----
    elif st.session_state.stage == "tech":
        st.session_state.candidate["tech_stack"] = user_input
        st.session_state.candidate["sentiment"] = analyze_sentiment(user_input)
        
        with st.spinner("Analyzing your stack and generating questions..."):
            questions = get_llm_response(
                SYSTEM, 
                TECH_QUESTION_PROMPT.format(tech_stack=user_input)
            )
        
        reply = f"Great! Here are your technical screening questions:\n\n{questions}\n\n**Please provide your answers below.**"
        st.session_state.stage = "answering"

    # ---- ANSWERING & FINAL WRAP-UP ----
    elif st.session_state.stage == "answering":
        reply = END_PROMPT
        st.session_state.stage = "end"

    # Add AI response to history and REFRESH
    st.session_state.messages.append({"role": "assistant", "content": reply})
    st.rerun()