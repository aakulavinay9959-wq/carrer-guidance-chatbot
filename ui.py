"""
UI module for Career Guidance Chatbot
Handles all Streamlit UI components and layout
"""

import streamlit as st
from chatbot import initialize_gemini_client, generate_response
from config import (
    PAGE_TITLE,
    PAGE_LAYOUT,
    APP_TITLE,
    APP_SUBTITLE,
    PAGE_ICON,
    ROADMAP_OPTIONS,
)
from styles import (
    apply_all_styles,
    apply_roadmap_card_styling,
    add_minimal_spacing,
    add_roadmap_heading,
)
from navbar import create_navbar
from sidebar import create_sidebar
from profile import show_profile_page
from news import show_news
from exams_jobs import show_exams_jobs_page
from learning_resources import show_learning_resources_page


CAREER_RECOMMENDER_QUESTIONS = [
    {
        "question": "What subjects or activities do you enjoy the most?",
        "examples": ["Math and coding", "Robotics club", "Designing apps"],
    },
    {
        "question": "What skills do you currently have? (technical skills, soft skills, tools, programming languages, etc.)",
        "examples": ["Python, SQL basics", "Good communication", "Canva and Excel"],
    },
    {
        "question": "Do you prefer creative work, analytical work, technical work, or management-related work?",
        "examples": ["Mostly analytical", "Technical + creative", "Management-oriented"],
    },
    {
        "question": "Do you prefer working in a team or independently?",
        "examples": ["Prefer team projects", "Prefer independent work", "Both are fine"],
    },
    {
        "question": "What are your long-term goals? (job, higher studies, startup, government exams, research, etc.)",
        "examples": ["Product job in 2 years", "M.Tech after B.Tech", "Prepare for GATE"],
    },
]

CAREER_RECOMMENDER_SYSTEM_PROMPT = """
You are a structured AI Career Recommender for engineering students in India.

You will receive 5 collected answers from the student.
Your task:
1. Analyze the answers carefully.
2. Suggest 3-5 suitable career paths.
3. For each path include:
   - Why it matches the user
   - Required skills
   - Recommended learning roadmap
   - Example job roles
   - Future scope

Response style:
- Friendly and motivational.
- Practical and personalized, not generic.
- Use clear headings and bullet points.
"""

ROADMAP_SH_OPTIONS = {
    "Frontend": "frontend",
    "Backend": "backend",
    "Full Stack": "full-stack",
    "DevOps": "devops",
    "AI & Data Scientist": "ai-data-scientist",
    "Data Analyst": "data-analyst",
    "Android": "android",
    "iOS": "ios",
    "Cyber Security": "cyber-security",
    "Blockchain": "blockchain",
    "QA / Testing": "qa",
    "System Design": "system-design",
    "Python": "python",
    "Java": "java",
    "JavaScript": "javascript",
    "React": "react",
    "Node.js": "nodejs",
    "AWS": "aws",
    "Docker": "docker",
    "Kubernetes": "kubernetes",
}

SKILL_BASED_ROADMAPS = {
    "SQL": "sql",
    "Computer Science": "computer-science",
    "React": "react",
    "Vue": "vue",
    "Angular": "angular",
    "JavaScript": "javascript",
    "TypeScript": "typescript",
    "Node.js": "nodejs",
    "Python": "python",
    "System Design": "system-design",
    "Java": "java",
    "ASP.NET Core": "aspnet-core",
    "API Design": "api-design",
    "Spring Boot": "spring-boot",
    "Flutter": "flutter",
    "C++": "cpp",
    "Rust": "rust",
    "Go": "go",
    "Design and Architecture": "design-system",
    "GraphQL": "graphql",
    "React Native": "react-native",
    "Design System": "design-system",
    "Prompt Engineering": "prompt-engineering",
    "MongoDB": "mongodb",
    "Linux": "linux",
    "Kubernetes": "kubernetes",
    "Docker": "docker",
    "AWS": "aws",
    "Terraform": "terraform",
    "Data Structures & Algorithms": "dsa",
    "Redis": "redis",
    "Git and GitHub": "git-github",
    "PHP": "php",
    "Cloudflare": "cloudflare",
    "AI Red Teaming": "ai-red-teaming",
    "AI Agents": "ai-agents",
    "HTML": "html",
    "CSS": "css",
    "Swift & SwiftUI": "swift",
    "Shell / Bash": "bash",
    "Laravel": "laravel",
    "Elasticsearch": "elasticsearch",
    "WordPress": "wordpress",
}


def setup_page_config():
    """Configure Streamlit page settings."""
    st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON, layout=PAGE_LAYOUT)


def render_header():
    """Render header section with title and subtitle."""
    st.title(APP_TITLE)
    st.markdown(
        f"""
    <div style='text-align:center; font-size:18px; color:#2e7d32; margin-top:4px; margin-bottom:12px; font-family: Poppins, sans-serif;'>
    {APP_SUBTITLE}
    </div>
    """,
        unsafe_allow_html=True,
    )


def initialize_chat_state():
    """Initialize session state for chat history."""
    if "messages" not in st.session_state:
        st.session_state.messages = [
            {
                "role": "assistant",
                "content": (
                    "Welcome! I am here to help you grow, plan, and succeed. "
                    "Share your branch/year, your target role or exam, and your current skill level "
                    "and we will create a clear path forward together."
                ),
            }
        ]


def render_chat_history():
    """Render all chat messages."""
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])


def _format_recommender_question(index):
    """Build question text with subtle sample answers."""
    item = CAREER_RECOMMENDER_QUESTIONS[index]
    sample_text = " | ".join(item["examples"])
    return (
        f"Question {index + 1}: {item['question']}\n\n"
        f"<span style='opacity:0.65; font-size: 13px;'>"
        f"Example answers: {sample_text}"
        f"</span>"
    )


def _normalize_text(text):
    """Normalize text for case-insensitive matching."""
    return (text or "").strip().lower()


def _render_roadmap_buttons(roadmaps, key_prefix):
    """Render roadmap buttons in a 3-column grid."""
    names = list(roadmaps.keys())
    cols_per_row = 3

    for idx in range(0, len(names), cols_per_row):
        row_names = names[idx : idx + cols_per_row]
        cols = st.columns(cols_per_row, gap="small")
        for col_idx, roadmap_name in enumerate(row_names):
            with cols[col_idx]:
                if st.button(
                    roadmap_name,
                    key=f"{key_prefix}_{roadmap_name}",
                    use_container_width=True,
                ):
                    st.session_state.selected_roadmap_name = roadmap_name
                    st.session_state.selected_roadmap_slug = roadmaps[roadmap_name]


def handle_chat_turn(prompt, client):
    """Handle one user turn and stream model response."""
    history = st.session_state.messages.copy()

    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        placeholder = st.empty()
        full_response = ""

        reply = generate_response(prompt, client, history=history)
        full_response += reply
        placeholder.markdown(full_response)

    st.session_state.messages.append({"role": "assistant", "content": full_response})


def render_roadmap_section():
    """Render roadmap selection section with path options."""
    add_minimal_spacing()
    add_roadmap_heading()
    apply_roadmap_card_styling()

    col1, col2, col3 = st.columns(3, gap="small")

    with col1:
        if st.button(
            f"{ROADMAP_OPTIONS[0]['emoji']} {ROADMAP_OPTIONS[0]['number']}. {ROADMAP_OPTIONS[0]['text']}"
        ):
            st.session_state.quick_redirect_page = "career_recommender"
            st.rerun()

    with col2:
        if st.button(
            f"{ROADMAP_OPTIONS[1]['emoji']} {ROADMAP_OPTIONS[1]['number']}. {ROADMAP_OPTIONS[1]['text']}"
        ):
            st.session_state.quick_redirect_page = "career_recommender"
            st.rerun()

    with col3:
        if st.button(
            f"{ROADMAP_OPTIONS[2]['emoji']} {ROADMAP_OPTIONS[2]['number']}. {ROADMAP_OPTIONS[2]['text']}"
        ):
            st.session_state.quick_redirect_page = "career_recommender"
            st.rerun()


def initialize_recommender_state():
    """Initialize session state for structured career recommender flow."""
    if "rec_messages" not in st.session_state:
        st.session_state.rec_messages = [
            {
                "role": "assistant",
                "content": (
                    "Hi! I am your structured AI Career Recommender. "
                    "I will ask 5 short questions, one by one, before suggesting career paths.\n\n"
                    f"{_format_recommender_question(0)}"
                ),
            }
        ]
        st.session_state.rec_question_index = 0
        st.session_state.rec_answers = []
        st.session_state.rec_complete = False


def _build_recommender_input():
    """Build model input from collected recommender answers."""
    answers = st.session_state.rec_answers
    return f"""
Student responses:
1. Subjects/activities enjoyed: {answers[0]}
2. Current skills: {answers[1]}
3. Preferred work type: {answers[2]}
4. Team vs independent preference: {answers[3]}
5. Long-term goals: {answers[4]}

Now provide personalized recommendations exactly as instructed.
""".strip()


def render_career_recommender_page():
    """Render structured question-by-question career recommender."""
    client = initialize_gemini_client()

    st.header("Career Recommender")
    st.caption("Answer each question. After 5 answers, you will get personalized career paths.")

    initialize_recommender_state()

    for message in st.session_state.rec_messages:
        with st.chat_message(message["role"]):
            if message["role"] == "assistant":
                st.markdown(message["content"], unsafe_allow_html=True)
            else:
                st.markdown(message["content"])

    user_answer = st.chat_input("Type your answer...")

    if user_answer and user_answer.strip():
        answer = user_answer.strip()
        st.session_state.rec_messages.append({"role": "user", "content": answer})

        if not st.session_state.rec_complete:
            st.session_state.rec_answers.append(answer)
            st.session_state.rec_question_index += 1

            if st.session_state.rec_question_index < len(CAREER_RECOMMENDER_QUESTIONS):
                next_idx = st.session_state.rec_question_index
                st.session_state.rec_messages.append(
                    {
                        "role": "assistant",
                        "content": _format_recommender_question(next_idx),
                    }
                )
            else:
                with st.spinner("Analyzing your responses and preparing recommendations..."):
                    model_input = _build_recommender_input()
                    recommendation = generate_response(
                        model_input,
                        client,
                        history=None,
                        system_prompt=CAREER_RECOMMENDER_SYSTEM_PROMPT,
                    )

                st.session_state.rec_messages.append(
                    {"role": "assistant", "content": recommendation}
                )
                st.session_state.rec_complete = True

        st.rerun()

    if st.button("Restart Recommender"):
        for key in ["rec_messages", "rec_question_index", "rec_answers", "rec_complete"]:
            if key in st.session_state:
                del st.session_state[key]
        st.rerun()


def render_roadmaps_page():
    """Render searchable roadmap.sh explorer with preset roadmap options."""
    st.markdown(
        """
        <style>
        /* Roadmaps page buttons: yellow theme */
        .stButton > button {
            background-color: #f4c430 !important;
            color: #1f2937 !important;
            border: 1px solid #e0b100 !important;
            font-weight: 700 !important;
        }
        .stButton > button:hover {
            background-color: #ffd84d !important;
            color: #111827 !important;
            border-color: #c99800 !important;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    st.header("Roadmaps")
    st.caption("Search a roadmap or choose from the preset options below.")

    if "selected_roadmap_name" not in st.session_state:
        st.session_state.selected_roadmap_name = None
    if "selected_roadmap_slug" not in st.session_state:
        st.session_state.selected_roadmap_slug = None

    query = st.text_input(
        "Search roadmap",
        placeholder="Example: frontend, devops, data analyst, python",
        key="roadmap_search_query",
    )

    normalized_query = _normalize_text(query)
    combined_roadmaps = {**ROADMAP_SH_OPTIONS, **SKILL_BASED_ROADMAPS}

    filtered_roadmaps = {}
    for name, slug in combined_roadmaps.items():
        if normalized_query in _normalize_text(name) or normalized_query in slug:
            filtered_roadmaps[name] = slug

    if normalized_query and not filtered_roadmaps:
        st.info("No exact preset match found. Try another keyword from the available roadmap options.")
    else:
        if normalized_query:
            st.subheader("Search Results")
            _render_roadmap_buttons(filtered_roadmaps, key_prefix="search_roadmap")
        else:
            st.subheader("Top Tech Roadmaps")
            _render_roadmap_buttons(ROADMAP_SH_OPTIONS, key_prefix="top_roadmap")
            st.markdown("---")
            st.subheader("Skill Based Roadmap")
            _render_roadmap_buttons(SKILL_BASED_ROADMAPS, key_prefix="skill_roadmap")

    selected_name = st.session_state.get("selected_roadmap_name")
    selected_slug = st.session_state.get("selected_roadmap_slug")
    if selected_name and selected_slug:
        slug = selected_slug
        url = f"https://roadmap.sh/{slug}"
        st.markdown("---")
        st.subheader(f"{selected_name} Roadmap")
        st.warning(
            "roadmap.sh blocks iframe embedding in many browsers. "
            "Use the button below to open the roadmap directly."
        )
        st.link_button(f"Open {selected_name} on roadmap.sh", url, use_container_width=True)
        st.markdown(f"[Open in new tab]({url})")


def run_app():
    """Main application runner with navigation and sidebar."""
    if "current_page" not in st.session_state:
        st.session_state.current_page = "home"
    if "user_logged_in" not in st.session_state:
        st.session_state.user_logged_in = False
    if "last_sidebar_page" not in st.session_state:
        st.session_state.last_sidebar_page = "home"
    if "quick_redirect_page" not in st.session_state:
        st.session_state.quick_redirect_page = None

    setup_page_config()
    apply_all_styles()

    # Use sidebar for navigation
    sidebar_page = create_sidebar()

    if st.session_state.quick_redirect_page:
        sidebar_page = st.session_state.quick_redirect_page
        st.session_state.quick_redirect_page = None

    # Move to main-content flow only when sidebar selection actually changes.
    if sidebar_page != st.session_state.last_sidebar_page:
        st.session_state.current_page = "home"
        st.session_state.last_sidebar_page = sidebar_page

    # Restore top navbar (Profile, News only)
    current_page = create_navbar()

    # Sidebar controls main content, navbar for quick access to profile/news
    if current_page == "news":
        show_news()
        return
    if current_page == "profile":
        show_profile_page()
        return

    # Sidebar navigation for main sections
    if sidebar_page == "home":
        render_home_page()
    elif sidebar_page == "career_recommender":
        render_career_recommender_page()
    elif sidebar_page == "roadmaps":
        render_roadmaps_page()
    elif sidebar_page == "exams_jobs":
        show_exams_jobs_page()
    elif sidebar_page == "learning_resources":
        show_learning_resources_page()
    elif sidebar_page == "career_planner":
        st.header("My Career Planner")
        st.info("Plan your career path here. [Placeholder]")
    else:
        render_home_page()


def render_home_page():
    """Render the home page with conversational chatbot."""
    client = initialize_gemini_client()

    render_header()
    initialize_chat_state()
    render_chat_history()

    prompt = st.chat_input("Ask your career question...")
    if prompt and prompt.strip():
        handle_chat_turn(prompt.strip(), client)

    render_roadmap_section()
