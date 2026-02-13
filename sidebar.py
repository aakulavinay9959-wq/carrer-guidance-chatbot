"""
Sidebar module for Career Guidance Chatbot
Handles sidebar UI and navigation
"""

import streamlit as st


def create_sidebar():
    """
    Create a sidebar with navigation options for the app.

    Returns:
        str: Selected section ('home', 'career_recommender', 'roadmaps', 'exams_jobs', 'learning_resources', 'career_planner')
    """
    st.sidebar.markdown("""
        <style>
        [data-testid="stSidebar"] .block-container {
            padding-top: 1.2rem;
        }

        .sidebar-title {
            font-size: 22px;
            font-weight: 900;
            color: #2e7d32;
            font-family: 'Poppins', sans-serif;
            margin-bottom: 22px;
        }

        [data-testid="stSidebar"] .stRadio > div[role="radiogroup"] > label {
            margin-bottom: 10px;
            padding-top: 4px;
            padding-bottom: 4px;
        }

        [data-testid="stSidebar"] .stRadio > div[role="radiogroup"] > label:last-child {
            margin-bottom: 0;
        }

        .sidebar-link {
            font-size: 16px;
            font-weight: 600;
            color: #333;
            margin-bottom: 10px;
            font-family: 'Poppins', sans-serif;
        }
        </style>
    """, unsafe_allow_html=True)

    st.sidebar.markdown('<div class="sidebar-title">Navigation</div>', unsafe_allow_html=True)

    page = st.sidebar.radio(
        "",
        [
            "\U0001F3E0 Home",
            "\U0001F3AF Career Recommender",
            "\U0001F5FA\ufe0f Roadmaps",
            "\U0001F4DD Exams and Jobs",
            "\U0001F4DA Learning Resources",
            "\U0001F5FA\ufe0f My Career Planner",
        ],
        key="sidebar_nav",
    )

    if page == "\U0001F3E0 Home":
        return "home"
    if page == "\U0001F3AF Career Recommender":
        return "career_recommender"
    if page == "\U0001F5FA\ufe0f Roadmaps":
        return "roadmaps"
    if page == "\U0001F4DD Exams and Jobs":
        return "exams_jobs"
    if page == "\U0001F4DA Learning Resources":
        return "learning_resources"
    if page == "\U0001F5FA\ufe0f My Career Planner":
        return "career_planner"

    return "home"
