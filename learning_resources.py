"""
Learning Resources module for Career Guidance Chatbot
Provides internet-backed, structured learning recommendations with roadmap and timetable
"""

import streamlit as st
from google import genai
from google.genai import types
from config import API_KEY, MODEL_NAME


EXAMPLE_QUERIES = [
    "I am a 2nd year CSE student, beginner in Python, need free AI/ML resources and a 12-week plan.",
    "I want backend developer preparation in 3 months with free courses, books, and practice platforms.",
    "Suggest a roadmap for GATE CSE + placements with official resources and weekly timetable.",
]


FALLBACK_TRACKS = {
    "ai_ml": {
        "keywords": ["ai", "ml", "machine learning", "deep learning", "data science"],
        "title": "AI / ML",
        "resources": {
            "websites": [
                ("Python Docs", "https://docs.python.org/3/"),
                ("NumPy Docs", "https://numpy.org/doc/"),
                ("pandas Docs", "https://pandas.pydata.org/docs/"),
                ("scikit-learn Docs", "https://scikit-learn.org/stable/"),
            ],
            "youtube": [
                ("freeCodeCamp", "https://www.youtube.com/@freecodecamp"),
                ("StatQuest", "https://www.youtube.com/@statquest"),
            ],
            "courses": [
                ("Kaggle Learn", "https://www.kaggle.com/learn"),
                ("Google ML Crash Course", "https://developers.google.com/machine-learning/crash-course"),
                ("NPTEL", "https://nptel.ac.in/"),
            ],
            "books": [
                ("Hands-On Machine Learning", "https://www.oreilly.com/library/view/hands-on-machine-learning/9781098125967/"),
            ],
            "practice": [
                ("Kaggle", "https://www.kaggle.com/"),
                ("LeetCode", "https://leetcode.com/"),
            ],
            "certs": [
                ("Google Cloud Skills Boost", "https://www.cloudskillsboost.google/"),
            ],
        },
    },
    "backend": {
        "keywords": ["backend", "node", "api", "spring", "django", "flask"],
        "title": "Backend Development",
        "resources": {
            "websites": [
                ("MDN Web Docs", "https://developer.mozilla.org/"),
                ("Node.js Docs", "https://nodejs.org/docs/latest/api/"),
                ("PostgreSQL Docs", "https://www.postgresql.org/docs/"),
            ],
            "youtube": [
                ("Traversy Media", "https://www.youtube.com/@TraversyMedia"),
                ("freeCodeCamp", "https://www.youtube.com/@freecodecamp"),
            ],
            "courses": [
                ("The Odin Project", "https://www.theodinproject.com/"),
                ("Full Stack Open", "https://fullstackopen.com/en/"),
            ],
            "books": [
                ("Designing Data-Intensive Applications", "https://dataintensive.net/"),
            ],
            "practice": [
                ("LeetCode", "https://leetcode.com/"),
                ("Exercism", "https://exercism.org/"),
            ],
            "certs": [
                ("AWS Skill Builder", "https://skillbuilder.aws/"),
            ],
        },
    },
    "gate": {
        "keywords": ["gate", "ese", "ssc je", "upsc", "psu"],
        "title": "GATE / Engineering Exams",
        "resources": {
            "websites": [
                ("GATE Official", "https://gate2026.iitg.ac.in/"),
                ("NPTEL", "https://nptel.ac.in/"),
            ],
            "youtube": [
                ("NPTEL", "https://www.youtube.com/@nptelhrd"),
            ],
            "courses": [
                ("SWAYAM", "https://swayam.gov.in/"),
            ],
            "books": [
                ("Standard Core Subject Textbooks", "https://nptel.ac.in/course.html"),
            ],
            "practice": [
                ("Official Previous Year Papers (Institute/Official Sources)", "https://gate2026.iitg.ac.in/"),
            ],
            "certs": [
                ("NPTEL Certificates", "https://nptel.ac.in/noc/"),
            ],
        },
    },
}


def _build_prompt(query, level, weekly_hours, free_first, include_ai_plan):
    free_pref = "Prioritize free resources first; include paid options only if highly valuable."
    if not free_first:
        free_pref = "Include both free and paid resources, but label clearly."

    ai_plan_instruction = ""
    if include_ai_plan:
        ai_plan_instruction = (
            "Also include an 'AI Learning Plan Generator Output' section with a concise"
            " 4-week adaptive plan based on the user goal."
        )

    return f"""
You are an expert learning-resources curator for engineering students in India.
Use web search grounding and provide only high-quality, trustworthy, official links.

User query:
{query}

Constraints:
1. Do not dump random links.
2. Keep output concise and structured.
3. Prefer official sources and reputable platforms.
4. Give practical, filtered recommendations.
5. User level: {level}
6. Weekly study hours available: {weekly_hours}
7. {free_pref}

Include these sections exactly:
1) Goal Understanding (2-3 bullets)
2) Best Resource Stack (grouped):
   - Websites/Docs
   - YouTube Channels
   - Courses/Tutorials
   - Recommended Books
   - Practice Platforms
   - Certification Options
   For each item include: Name | Why useful (1 line) | Official Link
3) Basic Roadmap (phase-wise, not paragraph)
4) Weekly Timetable (table format for {weekly_hours} hours/week)
5) Quick Start Checklist (first 7 days)
6) Quality Notes (short: why these are trusted)
{ai_plan_instruction}

Style:
- Crisp, actionable, no long paragraphs.
- Use headings and bullets/tables.
- Maximum 5 items per subsection unless unavoidable.
""".strip()


def _fetch_learning_resources(query, level, weekly_hours, free_first, include_ai_plan):
    client = genai.Client(api_key=API_KEY)
    prompt = _build_prompt(query, level, weekly_hours, free_first, include_ai_plan)

    contents = [
        types.Content(
            role="user",
            parts=[types.Part.from_text(text=prompt)],
        )
    ]

    tools = [
        types.Tool(
            googleSearch=types.GoogleSearch(),
        )
    ]

    config = types.GenerateContentConfig(
        tools=tools,
        temperature=0.35,
    )

    response_text = ""
    for chunk in client.models.generate_content_stream(
        model=MODEL_NAME,
        contents=contents,
        config=config,
    ):
        if chunk.text:
            response_text += chunk.text

    return response_text.strip()


def _pick_track(query):
    q = query.lower()
    for key, track in FALLBACK_TRACKS.items():
        if any(word in q for word in track["keywords"]):
            return key
    return "backend"


def _build_fallback_plan(query, level, weekly_hours, include_ai_plan):
    track = FALLBACK_TRACKS[_pick_track(query)]
    title = track["title"]
    r = track["resources"]

    plan = f"""
### Goal Understanding
- Target track identified: **{title}**
- Current level considered: **{level}**
- Weekly effort planned: **{weekly_hours} hours/week**

### Best Resource Stack
**Websites / Docs**
- {r['websites'][0][0]} | Official docs and fundamentals | {r['websites'][0][1]}
- {r['websites'][1][0]} | Core reference for concepts | {r['websites'][1][1]}

**YouTube Channels**
- {r['youtube'][0][0]} | Clear practical explanations | {r['youtube'][0][1]}

**Courses / Tutorials**
- {r['courses'][0][0]} | Structured learning path | {r['courses'][0][1]}

**Recommended Books**
- {r['books'][0][0]} | Strong conceptual depth | {r['books'][0][1]}

**Practice Platforms**
- {r['practice'][0][0]} | Practice and progress tracking | {r['practice'][0][1]}

**Certification Options**
- {r['certs'][0][0]} | Recognized certificate path | {r['certs'][0][1]}

### Basic Roadmap
1. Foundation (Weeks 1-2): Core concepts + official docs
2. Build (Weeks 3-6): Guided course + small projects/problems
3. Practice (Weeks 7-10): Daily problem solving + revision
4. Polish (Weeks 11-12): Mock tests/interview prep + portfolio updates

### Weekly Timetable
| Task | Hours/Week |
|---|---:|
| Concepts + Docs | {max(2, weekly_hours // 3)} |
| Practice / Problems | {max(2, weekly_hours // 3)} |
| Projects / Revision | {max(2, weekly_hours - 2 * (weekly_hours // 3))} |

### Quick Start Checklist (7 Days)
- Day 1: Finalize track + bookmark official resources
- Day 2-3: Complete first core module
- Day 4-5: Solve beginner practice set
- Day 6: Build mini artifact (notes/project/problem sheet)
- Day 7: Weekly review and next-week plan

### Quality Notes
- Links above prioritize official docs and trusted education platforms.
- For latest exam/course updates, always verify on official pages.
""".strip()

    if include_ai_plan:
        plan += """

### AI Learning Plan Generator Output
- Week A: Skill baseline and diagnostics
- Week B: Core learning sprint
- Week C: Practice and project sprint
- Week D: Review, gaps, and optimization
""".rstrip()

    return plan


def show_learning_resources_page():
    """Render learning resources search page with internet-backed recommendations."""
    st.header("Learning Resources")
    st.caption(
        "Search once and get structured, high-quality resources with official links, roadmap, and timetable."
    )

    st.markdown("**Try asking:**")
    for ex in EXAMPLE_QUERIES:
        st.markdown(f"- {ex}")

    col1, col2 = st.columns(2)
    with col1:
        level = st.selectbox("Current Level", ["Beginner", "Intermediate", "Advanced"])
    with col2:
        weekly_hours = st.slider("Weekly Study Hours", min_value=4, max_value=40, value=12, step=1)

    col3, col4 = st.columns(2)
    with col3:
        free_first = st.checkbox("Prioritize free resources", value=True)
    with col4:
        include_ai_plan = st.checkbox("AI Learning Plan Generator", value=True)

    query = st.text_input(
        "Search for learning resources",
        placeholder="Example: Free roadmap for becoming Data Analyst in 4 months with official links",
    )

    if st.button("Get Learning Plan", use_container_width=True):
        if not query.strip():
            st.warning("Please enter your learning goal or query.")
            return

        with st.spinner("Searching trusted sources and building your plan..."):
            try:
                if not API_KEY:
                    raise RuntimeError("GEMINI_API_KEY missing")
                output = _fetch_learning_resources(
                    query=query.strip(),
                    level=level,
                    weekly_hours=weekly_hours,
                    free_first=free_first,
                    include_ai_plan=include_ai_plan,
                )
                st.markdown(output)
            except Exception as exc:
                error_text = str(exc)
                if "429" in error_text or "RESOURCE_EXHAUSTED" in error_text:
                    st.warning(
                        "Gemini quota is exhausted right now, so I generated an offline trusted-plan fallback."
                    )
                else:
                    st.warning(
                        "Live search is unavailable right now, so I generated an offline trusted-plan fallback."
                    )
                st.markdown(
                    _build_fallback_plan(
                        query=query.strip(),
                        level=level,
                        weekly_hours=weekly_hours,
                        include_ai_plan=include_ai_plan,
                    )
                )
