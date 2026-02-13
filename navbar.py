"""
Navigation bar module for Career Guidance Chatbot
Handles navbar UI and settings
"""

import streamlit as st
from datetime import datetime


def create_navbar():
    """
    Create a navigation bar with home, news, and profile sections

    Returns:
        str: Selected section ('home', 'news', 'profile')
    """
    # Container for navbar with custom styling
    st.markdown("""
        <style>
        /* Navbar styling */
        .nav-container {
            background: linear-gradient(90deg, #2e7d32, #1b5e20);
            padding: 8px 20px;
            border-radius: 10px;
            margin-bottom: 20px;
            box-shadow: 0 2px 8px rgba(46, 125, 50, 0.15);
        }

        .nav-brand {
            font-size: 20px;
            font-weight: 900;
            color: #ff7f11;
            font-family: 'Poppins', sans-serif;
        }

        /* Custom navbar button styling - different from main buttons */
        .nav-button {
            background: transparent !important;
            color: white !important;
            border: 2px solid transparent !important;
            border-radius: 6px !important;
            padding: 6px 14px !important;
            font-size: 14px !important;
            font-weight: 600 !important;
            font-family: 'Poppins', sans-serif !important;
            transition: all 0.25s ease !important;
            cursor: pointer !important;
            min-width: 90px !important;
            text-align: center !important;
            display: inline-block !important;
        }

        .nav-button:hover {
            background: rgba(255, 235, 59, 0.2) !important;
            border: 2px solid #ffeb3b !important;
            color: #ffeb3b !important;
        }

        .nav-button:active {
            background: rgba(255, 235, 59, 0.35) !important;
        }
        </style>
    """, unsafe_allow_html=True)

    # Navbar layout - balanced columns with equal-sized buttons
    col_brand, col_space1, col_home, col_space2, col_news, col_space3, col_profile, col_end = st.columns([1.8, 0.3, 1, 0.2, 1, 0.2, 1, 0.5])

    with col_brand:
        brand_icon_col, brand_text_col = st.columns([0.18, 0.82], gap="small")
        with brand_icon_col:
            st.image("robot.png", width=28)
        with brand_text_col:
            st.markdown("""
                <div style='padding: 6px 0; font-size: 18px; font-weight: 900; color: #ff7f11; font-family: Poppins, sans-serif;'>
                CareerGuide
                </div>
            """, unsafe_allow_html=True)

    with col_space1:
        st.write("")  # Spacer

    with col_home:
        if st.button(" 🏠Home", key="nav_home", use_container_width=True):
            st.session_state.current_page = "home"
            st.rerun()

    with col_space2:
        st.write("")  # Space between buttons

    with col_news:
        if st.button(" 📣News", key="nav_news", use_container_width=True):
            st.session_state.current_page = "news"
            st.rerun()

    with col_space3:
        st.write("")  # Space between buttons

    with col_profile:
        if st.button(" 👤Profile", key="nav_profile", use_container_width=True):
            st.session_state.current_page = "profile"
            st.rerun()

    with col_end:
        st.write("")  # Spacing

    st.markdown("---")

    # Return current page from session state, default to home
    return st.session_state.get("current_page", "home")
