import os
import streamlit as st
from google import genai
from google.genai import types

# -----------------------------
# Gemini Configuration
# -----------------------------
API_KEY = os.getenv("GEMINI_API_KEY")
MODEL_NAME = "gemini-3-flash-preview"

client = genai.Client(api_key=API_KEY)

SYSTEM_PROMPT = """
You are a professional Career Guidance Chatbot designed specifically for engineering students.

Responsibilities:
1. Answer only career-related questions.
2. Suggest career paths based on interests, strengths, skills, and academic background.
3. Provide accurate info on:
   - Competitive exams (GATE, GRE, CAT, UPSC, etc.)
   - Government/private jobs
   - Engineering domains (AI, Data Science, Core Engineering, Software, etc.)
4. Recommend relevant learning resources:
   - Online courses, Certifications, Books, Platforms (Coursera, Udemy, NPTEL)
5. Offer career planning guidance:
   - Roadmaps, Skill development, Resume-building, Internship advice
6. Ask clarifying questions if the query is incomplete.
7. Structured responses with headings and bullet points.
8. Keep responses practical, supportive, and easy to understand.

Strict Rule:
If a user asks anything not related to career guidance for engineering students,
politely refuse with: "I am designed to assist only with career-related guidance for engineering students. Please ask a career-related question."

Before giving suggestions, briefly analyze the student’s situation.
Ask 2–3 diagnostic questions if needed.
Prioritize realistic and achievable advice.
"""

# -----------------------------
# Streamlit UI
# -----------------------------
st.set_page_config(page_title="Engineering Career Guidance Chatbot", layout="centered")
st.title("🎓 Engineering Career Guidance Chatbot")

user_input = st.text_area(
    "Enter your question:",
    placeholder="Example: I'm a 3rd-year CS student interested in AI. How should I prepare for GATE?",
    height=120
)

if st.button("Submit"):
    if user_input.strip() == "":
        st.warning("Please enter a question.")
    else:
        # Use the backend logic from your Career Guide Bot
        contents = [
            types.Content(
                role="system",
                parts=[types.Part.from_text(text=SYSTEM_PROMPT)],
            ),
            types.Content(
                role="user",
                parts=[types.Part.from_text(text=user_input)],
            ),
        ]

        response = ""
        # Stream response from Gemini using your existing backend code
        for chunk in client.models.generate_content_stream(
            model=MODEL_NAME,
            contents=contents,
        ):
            if chunk.text:
                response += chunk.text

        st.subheader("Response")
        st.write(response)
