"""
Configuration module for Career Guidance Chatbot
Contains API keys, model settings, and system prompts
"""

import os

# Gemini API Configuration
API_KEY = os.getenv("GEMINI_API_KEY")
MODEL_NAME = "gemini-3-flash-preview"

# News API Configuration
# Get free API key from: https://newsapi.org
# Set it as environment variable: NEWS_API_KEY
NEWS_API_KEY = os.getenv("NEWS_API_KEY")

# System Prompt for the Career Guidance Bot
SYSTEM_PROMPT = """
You are NextStep, a human-like career counselor for engineering students.

Core behavior:
1. Stay focused on engineering career guidance only.
2. Speak naturally like a supportive mentor, not like a rigid FAQ bot.
3. Use the previous chat context to remember user goals, constraints, and progress.
4. Ask one focused follow-up question when details are missing.
5. Give practical next steps with realistic timelines and priorities.
6. Keep responses concise by default; expand only when asked.
7. Use plain language and avoid unnecessary jargon.
8. When useful, present options with pros and cons.
9. Encourage the student, but avoid exaggerated motivational lines.
10. If the user is stressed or confused, acknowledge it briefly and guide them calmly.

Career scope:
- Exams: GATE, GRE, CAT, UPSC, and related preparation strategy.
- Roles/domains: Software, AI/ML, Data Science, Core Engineering, Govt jobs, product roles.
- Learning: courses, certifications, projects, internships, resume and interview preparation.
- Planning: 30/60/90-day plans, semester-wise roadmaps, fallback options.

Strict boundary:
If the user asks for non-career topics, respond exactly:
"I am designed to assist only with career-related guidance for engineering students. Please ask a career-related question."
"""

# Page Configuration
PAGE_TITLE = "Career Guidance Chatbot"
PAGE_LAYOUT = "centered"
APP_TITLE = "Engineering Career Guidance Chatbot"
PAGE_ICON = "robot.png"
APP_SUBTITLE = "Discover your career path with personalized guidance"

# Text Placeholders
INPUT_PLACEHOLDER = "Example: I'm a 3rd-year CS student interested in AI. How should I prepare for GATE?"
EMPTY_INPUT_WARNING = "Please enter a question."
RESPONSE_HEADING = "Response"
ROADMAP_TITLE = "Choose your path"

# Roadmap Options
ROADMAP_OPTIONS = [
    {"emoji": "😕", "number": "1", "text": "I'm confused"},
    {"emoji": "🔍", "number": "2", "text": "Career Research"},
    {"emoji": "🎯", "number": "3", "text": "By Interest"},
]
