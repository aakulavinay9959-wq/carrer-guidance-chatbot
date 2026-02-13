"""
Career Guidance Chatbot - Main Entry Point

This is the main application file. The code is organized into separate modules:
- config.py: Configuration settings (API keys, prompts, constants)
- styles.py: All CSS and styling functions
- chatbot.py: Gemini API interaction logic
- ui.py: Streamlit UI components and layout

Run this file with: streamlit run demo2.py
"""

from ui import run_app


if __name__ == "__main__":
    run_app()
