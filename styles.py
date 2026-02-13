"""
Styling module for Career Guidance Chatbot
Contains all CSS and Streamlit styling
"""

import streamlit as st


def apply_title_styling():
    """Apply custom styling for the main title"""
    st.markdown("""
        <style>
        /* Import Google Font */
        @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@700&display=swap');

        h1 {
            font-family: 'Poppins', sans-serif !important;
            font-weight: 900 !important;
            font-size: 42px !important;
            letter-spacing: 1px;
            color: #2e7d32;   /* Green */
            text-align: center;
        }
        </style>
    """, unsafe_allow_html=True)


def apply_button_styling():
    """Apply custom styling for buttons"""
    st.markdown("""
        <style>
        /* Blue Button */
        .stButton > button {
            background-color: #1f77ff;   /* Blue */
            color: white;                /* White text */
            border-radius: 8px;
            border: none;
            padding: 8px 16px;
            font-weight: bold;
        }

        /* Hover Effect */
        .stButton > button:hover {
            background-color: white;
            color: #1f77ff;              /* Blue text */
            border: 2px solid #1f77ff;
        }
        </style>
    """, unsafe_allow_html=True)


def apply_theme_styling():
    """Apply light green and white theme with styled title"""
    st.markdown("""
        <style>
        /* Background with light green & white gradient */
        .stApp {
            background: linear-gradient(to bottom right, #f0fff4, #ffffff);
        }

        /* Custom Title Styling */
        .custom-title {
            font-family: 'Trebuchet MS', sans-serif;
            font-size: 40px;
            font-weight: bold;
            text-align: center;
            background: linear-gradient(90deg, #2e7d32, #ff7f11);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            margin-bottom: 10px;
        }

        /* Button styling */
        .stButton > button {
            background-color: #ff7f11;
            color: white;
            border-radius: 8px;
            border: none;
            padding: 8px 16px;
            font-weight: bold;
        }

        .stButton > button:hover {
            background-color: #2e7d32;
            color: white;
        }

        /* Text area border */
        .stTextArea textarea {
            border: 2px solid #2e7d32;
            border-radius: 8px;
        }
        </style>
    """, unsafe_allow_html=True)


def apply_orange_green_theme():
    """Apply orange and green theme"""
    st.markdown("""
        <style>
        /* Main background */
        .stApp {
            background-color: #f9fff9;
        }

        /* Title styling */
        h1 {
            color: #ff7f11;  /* Orange */
            text-align: center;
        }

        /* Subheader styling */
        h2, h3 {
            color: #2e7d32;  /* Green */
        }

        /* Button styling */
        .stButton > button {
            background-color: #ff7f11;  /* Orange */
            color: white;
            border-radius: 8px;
            border: none;
            padding: 8px 16px;
            font-weight: bold;
        }

        .stButton > button:hover {
            background-color: #2e7d32;  /* Green */
            color: white;
        }

        /* Text area border */
        .stTextArea textarea {
            border: 2px solid #2e7d32;  /* Green */
            border-radius: 8px;
        }

        /* Warning message */
        .stAlert {
            border-left: 5px solid #ff7f11;
        }
        </style>
    """, unsafe_allow_html=True)


def apply_roadmap_card_styling():
    """Apply styling for roadmap option cards"""
    st.markdown("""
        <style>
        .stButton > button {
            background: #ffffff !important;
            border: 1px solid #e6e6e6 !important;
            border-radius: 10px !important;
            padding: 12px 8px !important;
            text-align: center !important;
            box-shadow: 0 1px 4px rgba(0,0,0,0.05) !important;
            color: #2e7d32 !important;
            font-weight: 600 !important;
            width: 100% !important;
        }
        .stButton > button:hover {
            background: #ff7f11 !important;
            color: #ffffff !important;
        }
        </style>
    """, unsafe_allow_html=True)


def apply_subtitle_styling():
    """Apply styling for app subtitle"""
    st.markdown("""
        <div style='text-align:center; font-size:18px; color:#2e7d32; margin-top:4px; margin-bottom:12px; font-family: Poppins, sans-serif;'>
        Discover your perfect carrer path with intelligent, personalized guidance
        </div>
    """, unsafe_allow_html=True)


def apply_all_styles():
    """Apply all styling to the app"""
    apply_title_styling()
    apply_button_styling()
    apply_theme_styling()
    apply_orange_green_theme()
    apply_chat_input_styling()


def add_minimal_spacing():
    """Add minimal spacing below submit button"""
    st.markdown("""
        <div style='margin-top:6px;'></div>
    """, unsafe_allow_html=True)


def add_roadmap_heading():
    """Add centered heading for roadmap section"""
    st.markdown("""
        <div style='text-align:center;'>
            <h3 style='color:#2e7d32; margin:6px 0 10px 0; font-family: Poppins, sans-serif;'>Choose Your path</h3>
        </div>
    """, unsafe_allow_html=True)


def apply_input_field_styling():
    """Apply attractive styling to the input text area with curved edges"""
    st.markdown("""
        <style>
        /* Input text area styling */
        .stTextArea textarea {
            border: 2px solid #2e7d32 !important;
            border-radius: 15px !important;
            padding: 12px 16px !important;
            font-size: 16px !important;
            font-family: 'Poppins', sans-serif !important;
            background-color: #f9fff9 !important;
            box-shadow: 0 2px 8px rgba(46, 125, 50, 0.1) !important;
            transition: all 0.3s ease !important;
        }
        
        .stTextArea textarea:focus {
            border: 2px solid #ff7f11 !important;
            box-shadow: 0 4px 12px rgba(255, 127, 17, 0.2) !important;
        }
        
        /* Remove default focus outline */
        .stTextArea textarea:focus-visible {
            outline: none !important;
        }
        </style>
    """, unsafe_allow_html=True)


def apply_submit_button_styling():
    """Apply attractive styling to the submit button"""
    st.markdown("""
        <style>
        /* Submit button styling */
        .submit-button-container {
            display: flex;
            justify-content: center;
            margin-top: 16px;
            margin-bottom: 8px;
        }
        
        .stButton button[kind="primary"] {
            background: linear-gradient(135deg, #ff7f11, #ff9844) !important;
            color: white !important;
            border: none !important;
            border-radius: 12px !important;
            padding: 12px 48px !important;
            font-size: 16px !important;
            font-weight: 700 !important;
            font-family: 'Poppins', sans-serif !important;
            box-shadow: 0 4px 15px rgba(255, 127, 17, 0.3) !important;
            transition: all 0.3s ease !important;
            letter-spacing: 0.5px !important;
        }
        
        .stButton button[kind="primary"]:hover {
            background: linear-gradient(135deg, #ff9844, #ffb380) !important;
            box-shadow: 0 6px 20px rgba(255, 127, 17, 0.4) !important;
            transform: translateY(-2px) !important;
        }
        
        .stButton button[kind="primary"]:active {
            transform: translateY(0px) !important;
        }
        </style>
    """, unsafe_allow_html=True)


def apply_chat_input_styling():
    """Apply attractive styling to the Streamlit chat input bar."""
    st.markdown("""
        <style>
        /* Chat input shell */
        div[data-testid="stChatInput"] {
            background: linear-gradient(135deg, #ffffff, #f6fff7) !important;
            border: 2px solid #d8f0da !important;
            border-radius: 18px !important;
            box-shadow: 0 8px 22px rgba(46, 125, 50, 0.12) !important;
            padding: 6px !important;
            transition: all 0.25s ease !important;
        }

        /* Input area */
        div[data-testid="stChatInput"] textarea {
            font-family: 'Poppins', sans-serif !important;
            font-size: 15px !important;
            color: #1f2937 !important;
        }

        div[data-testid="stChatInput"]:focus-within {
            border-color: #ff7f11 !important;
            box-shadow: 0 10px 28px rgba(255, 127, 17, 0.24) !important;
            transform: translateY(-1px) !important;
        }

        /* Placeholder */
        div[data-testid="stChatInput"] textarea::placeholder {
            color: #6b7280 !important;
            opacity: 0.95 !important;
        }

        /* Send button */
        button[data-testid="stChatInputSubmitButton"] {
            background: linear-gradient(135deg, #ff7f11, #ff9a3d) !important;
            border: none !important;
            border-radius: 12px !important;
            box-shadow: 0 4px 10px rgba(255, 127, 17, 0.32) !important;
        }

        button[data-testid="stChatInputSubmitButton"]:hover {
            background: linear-gradient(135deg, #ff9a3d, #ffb669) !important;
            transform: translateY(-1px) !important;
        }
        </style>
    """, unsafe_allow_html=True)
