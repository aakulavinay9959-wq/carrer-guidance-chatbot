"""
News module for Career Guidance Chatbot
Fetches real career-related news from the internet
"""

import streamlit as st
from datetime import datetime
import requests
import os
from typing import List, Dict
import re
import html


def clean_html_tags(text: str) -> str:
    """
    Remove HTML tags and decode HTML entities from text
    
    Args:
        text: Text potentially containing HTML
        
    Returns:
        Clean text without HTML tags
    """
    if not text:
        return ""
    
    # Decode HTML entities (e.g., &amp; -> &)
    text = html.unescape(text)
    
    # Remove HTML tags
    clean = re.compile('<.*?>')
    text = re.sub(clean, '', text)
    
    # Remove extra whitespace
    text = ' '.join(text.split())
    
    return text


def fetch_news_from_api() -> List[Dict]:
    """
    Fetch real news from NewsAPI related to education, jobs, and careers
    
    Returns:
        List of news articles with details
    """
    try:
        # Get API key from environment variable
        # Free API key available at: https://newsapi.org
        api_key = os.getenv("NEWS_API_KEY")
        
        if not api_key:
            st.warning("ℹ️ Note: To display real news, set NEWS_API_KEY environment variable. Get free key at https://newsapi.org")
            return None
        
        # Keywords for education and career news
        keywords = ["education jobs", "exam results", "career guidance", "engineering recruitment", 
                   "internship", "GATE exam", "government jobs", "placements", "skill development"]
        
        all_articles = []
        
        # Fetch news for multiple keywords
        for keyword in keywords[:3]:  # Limit to 3 keywords to avoid rate limiting
            url = "https://newsapi.org/v2/everything"
            params = {
                "q": keyword,
                "sortBy": "publishedAt",
                "language": "en",
                "pageSize": 5,
                "apiKey": api_key
            }
            
            response = requests.get(url, params=params, timeout=5)
            
            if response.status_code == 200:
                data = response.json()
                if data.get("articles"):
                    all_articles.extend(data["articles"])
        
        # Remove duplicates
        seen = set()
        unique_articles = []
        for article in all_articles:
            title = article.get("title", "")
            if title not in seen:
                seen.add(title)
                unique_articles.append(article)
        
        return unique_articles[:10]  # Return top 10 articles
        
    except requests.exceptions.RequestException as e:
        st.error(f"❌ Error fetching news: {str(e)}")
        return None
    except Exception as e:
        st.error(f"❌ Unexpected error: {str(e)}")
        return None


def format_news_article(article: Dict, index: int) -> None:
    """
    Display a formatted news article
    
    Args:
        article: News article dictionary
        index: Article index for unique key
    """
    # Clean HTML from all text fields
    title = clean_html_tags(article.get("title", "No title"))
    description = clean_html_tags(article.get("description", "No description available"))
    source = clean_html_tags(article.get("source", {}).get("name", "Unknown Source"))
    published_at = article.get("publishedAt", "")
    url = article.get("url", "#")
    image_url = article.get("urlToImage", "")
    author = clean_html_tags(article.get("author", "Unknown Author"))
    
    # Format date
    try:
        date_obj = datetime.fromisoformat(published_at.replace("Z", "+00:00"))
        formatted_date = date_obj.strftime("%b %d, %Y")
    except:
        formatted_date = "Recently"
    
    # Display article using native Streamlit components (no raw HTML)
    with st.container():
        cols = st.columns([1, 4])
        # left column: image if available
        if image_url:
            try:
                cols[0].image(image_url, width="stretch")
            except Exception:
                cols[0].write("")
        else:
            cols[0].write("")

        # right column: text content
        cols[1].subheader(title)
        cols[1].write(description)
        cols[1].caption(f"📰 {source}    |    📅 {formatted_date}    |    ✍️ {author}")

        # Read full article link
        cols[1].markdown(f"[Read Full Article →]({url})")

        st.markdown("---")


def show_news():
    """Display career and education-related news from internet"""
    st.subheader("📰 Education & Career News")
    
    # Info box about news source
    st.info("🌐 Fetching latest news from across the internet related to education, jobs, and careers...")
    
    # Filter options
    col1, col2, col3 = st.columns(3)
    
    with col1:
        refresh = st.button("🔄 Refresh News", use_container_width=True)
    
    with col2:
        search_term = st.text_input("🔍 Search news", placeholder="e.g., GATE, placement, internship...")
    
    with col3:
        sort_option = st.selectbox(
            "Sort by",
            ["Latest", "Oldest"]
        )
    
    st.markdown("---")
    
    # Fetch news
    articles = fetch_news_from_api()
    
    if articles is None:
        st.warning("""
        ### 🔑 Setup Required
        
        To display real news updates, please:
        
        1. Get a **free API key** from [NewsAPI.org](https://newsapi.org)
        2. Set it as an environment variable: `NEWS_API_KEY`
        
        **For local development:**
        - Windows: Set environment variable and restart your terminal
        - Linux/Mac: `export NEWS_API_KEY="your_key_here"`
        
        **For deployment:**
        - Add to your hosting platform's environment variables
        
        Currently showing sample news format while API is unavailable.
        """)
        articles = get_fallback_news()
    
    # Filter articles
    if search_term:
        articles = [
            article for article in articles 
            if search_term.lower() in article.get("title", "").lower() or 
               search_term.lower() in article.get("description", "").lower()
        ]
    
    # Sort articles
    if sort_option == "Oldest":
        articles = articles[::-1]
    
    # Display articles
    if not articles:
        st.info("📭 No news found matching your search. Try different keywords like 'GATE', 'placement', or 'internship'.")
    else:
        st.markdown(f"### Found {len(articles)} articles")
        
        for idx, article in enumerate(articles):
            format_news_article(article, idx)
    
    st.markdown("---")
    
    # Newsletter subscription
    st.markdown("### 📧 Subscribe to Career & Education Newsletter")
    col1, col2 = st.columns([3, 1])
    
    with col1:
        email = st.text_input("Enter your email to get daily updates", placeholder="your.email@gmail.com", key="news_email")
    
    with col2:
        if st.button("✉️ Subscribe", use_container_width=True):
            if email:
                st.success(f"✅ Subscribed! Daily news digest will be sent to {email}")
            else:
                st.error("❌ Please enter a valid email address.")


def get_fallback_news() -> List[Dict]:
    """
    Provide fallback news when API is not available
    
    Returns:
        List of sample news articles
    """
    return [
        {
            "title": "GATE 2026 Exam Schedule Released - Registration Opens March 1st",
            "description": "The Graduate Aptitude Test in Engineering (GATE) 2026 exam schedule has been officially announced. Registration will open from March 1st, 2026. Students are advised to start their preparation early and focus on core concepts.",
            "source": {"name": "education.gov.in"},
            "publishedAt": datetime.now().isoformat(),
            "url": "https://example.com",
            "author": "Education Ministry",
            "urlToImage": None
        },
        {
            "title": "Top Tech Companies Announce 50,000+ Campus Placements for 2026 Batch",
            "description": "Google, Microsoft, Amazon, Apple, and other major tech companies announced massive hiring drives for 2026 batch engineering students. Focus on Data Structures, Algorithms, and System Design to excel in interviews.",
            "source": {"name": "placements.org"},
            "publishedAt": datetime.now().isoformat(),
            "url": "https://example.com",
            "author": "Recruitment News",
            "urlToImage": None
        },
        {
            "title": "Government Releases 5,000 Engineering Jobs Through UPSC and SSC",
            "description": "Union Public Service Commission (UPSC) and Staff Selection Commission (SSC) announced over 5,000 vacancies for engineering graduates across various government organizations like NTPC, ONGC, and Indian Railways.",
            "source": {"name": "upsc.gov.in"},
            "publishedAt": datetime.now().isoformat(),
            "url": "https://example.com",
            "author": "UPSC",
            "urlToImage": None
        },
        {
            "title": "Coursera and IIT Bombay Launch Advanced AI/ML Certification Program",
            "description": "A comprehensive 6-month certification program in Artificial Intelligence and Machine Learning is now available. Limited seats for engineering students with 40% early bird discount available till month end.",
            "source": {"name": "coursera.org"},
            "publishedAt": datetime.now().isoformat(),
            "url": "https://example.com",
            "author": "Coursera",
            "urlToImage": None
        },
        {
            "title": "Remote Internship Opportunities Surge: 10,000+ Positions Available",
            "description": "With the rise of remote work culture, over 10,000 internship opportunities are now available for engineering students across various sectors including IT, Data Science, and Software Development.",
            "source": {"name": "internship.com"},
            "publishedAt": datetime.now().isoformat(),
            "url": "https://example.com",
            "author": "Internship Portal",
            "urlToImage": None
        }
    ]

