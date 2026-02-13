"""
Exams and Jobs module for Career Guidance Chatbot
Provides structured exam guidance and job opportunities for engineering students in India
"""

import streamlit as st


EXAM_CATEGORIES = {
    "Higher Studies": [
        {
            "name": "GATE",
            "purpose": "M.Tech admissions, PSU shortlisting, and research opportunities.",
            "eligibility": "Final-year or graduated engineering/science students (as per current official brochure).",
            "pattern": "CBT, mostly objective; General Aptitude + Engineering Mathematics + Core Subject.",
            "timeline": "Notification: Aug-Sep | Application: Aug-Oct | Exam: Jan-Feb | Result: Mar",
            "prep_tips": [
                "Complete syllabus once, then solve PYQs topic-wise.",
                "Give weekly mock tests and track weak topics.",
                "Create a revision sheet for formulas and short notes.",
            ],
            "difficulty": 4,
            "trusted_sources": [
                ("GATE Official", "https://gate2026.iitg.ac.in/"),
            ],
        },
        {
            "name": "JAM",
            "purpose": "M.Sc. and integrated PhD admissions in IITs and partner institutes.",
            "eligibility": "Graduates/final-year students in relevant disciplines.",
            "pattern": "CBT with MCQ, MSQ, and NAT sections.",
            "timeline": "Notification: Sep | Application: Sep-Oct | Exam: Feb | Result: Mar",
            "prep_tips": [
                "Strengthen concept-heavy topics first.",
                "Practice mixed question sets with time limits.",
                "Revise standard undergraduate fundamentals regularly.",
            ],
            "difficulty": 3,
            "trusted_sources": [
                ("JAM Official", "https://jam2026.iitb.ac.in/"),
            ],
        },
        {
            "name": "CEED",
            "purpose": "M.Des and design-related higher studies in top institutes.",
            "eligibility": "Degree/diploma holders or final-year students from approved programs.",
            "pattern": "Part A (objective) + Part B (drawing/design aptitude).",
            "timeline": "Notification: Oct | Application: Oct-Nov | Exam: Jan | Result: Mar",
            "prep_tips": [
                "Practice sketching and visual communication daily.",
                "Study past CEED Part B questions.",
                "Build design thinking through case studies.",
            ],
            "difficulty": 3,
            "trusted_sources": [
                ("CEED Official", "https://www.ceed.iitb.ac.in/2026/"),
            ],
        },
        {
            "name": "UGC-NET",
            "purpose": "Eligibility for Assistant Professor and JRF in relevant subjects.",
            "eligibility": "Postgraduate with required marks (or final-year PG as per norms).",
            "pattern": "Two papers in a single session: teaching/research aptitude + subject paper.",
            "timeline": "Usually 2 cycles/year | Notification windows vary by cycle",
            "prep_tips": [
                "Focus on syllabus boundaries and unit-wise notes.",
                "Practice previous papers for Paper 1 and Paper 2.",
                "Use short revision cycles before the exam month.",
            ],
            "difficulty": 4,
            "trusted_sources": [
                ("UGC-NET Official (NTA)", "https://ugcnet.nta.ac.in/"),
            ],
        },
    ],
    "Government Jobs": [
        {
            "name": "UPSC Engineering Services (ESE)",
            "purpose": "Group A engineering officer roles in central government departments.",
            "eligibility": "Engineering degree in relevant discipline; age and other UPSC criteria apply.",
            "pattern": "Prelims (objective) + Mains (descriptive) + Personality Test.",
            "timeline": "Notification: Sep-Oct | Prelims: Feb | Mains: Jun | Interview: Later stages",
            "prep_tips": [
                "Build strong theory plus objective practice for Prelims.",
                "Prepare descriptive writing for Mains with answer structure.",
                "Track current affairs relevant to engineering/public policy.",
            ],
            "difficulty": 5,
            "trusted_sources": [
                ("UPSC Official", "https://upsc.gov.in/"),
                ("UPSC Active Examinations", "https://upsc.gov.in/examinations/active-exams"),
            ],
        },
        {
            "name": "SSC JE",
            "purpose": "Junior Engineer roles in central government organizations.",
            "eligibility": "Diploma/B.E./B.Tech depending on post and department notification.",
            "pattern": "Tier 1 (objective) + Tier 2 (objective/descriptive as per latest notification).",
            "timeline": "Notification cycles vary yearly | Check SSC calendar",
            "prep_tips": [
                "Master core technical topics plus GS/reasoning basics.",
                "Solve past year papers for speed and accuracy.",
                "Keep formula notebooks for quick revision.",
            ],
            "difficulty": 3,
            "trusted_sources": [
                ("SSC Official", "https://ssc.gov.in/"),
            ],
        },
        {
            "name": "State PSC Engineering Exams",
            "purpose": "State-level Assistant Engineer/Junior Engineer recruitment.",
            "eligibility": "Engineering degree/diploma as per specific state PSC notification.",
            "pattern": "Usually objective prelims + mains/interview (varies by state).",
            "timeline": "State-wise notifications across the year",
            "prep_tips": [
                "Follow your state PSC syllabus strictly.",
                "Prepare technical subjects + state GK/current affairs.",
                "Track official state PSC updates frequently.",
            ],
            "difficulty": 3,
            "trusted_sources": [
                ("UPSC Portal (reference)", "https://upsc.gov.in/"),
            ],
        },
        {
            "name": "PSU Recruitment (via GATE)",
            "purpose": "Engineer/Executive roles in PSUs like IOCL, NTPC, ONGC, etc.",
            "eligibility": "Valid GATE score + branch-specific PSU criteria.",
            "pattern": "GATE score shortlisting + GD/Interview/medical as per PSU.",
            "timeline": "PSU forms: generally after GATE application/result windows",
            "prep_tips": [
                "Target high GATE score with strong fundamentals.",
                "Prepare HR + technical interview questions.",
                "Track each PSU eligibility and cutoff trends.",
            ],
            "difficulty": 4,
            "trusted_sources": [
                ("GATE Official", "https://gate2026.iitg.ac.in/"),
            ],
        },
    ],
    "MBA / Management": [
        {
            "name": "CAT",
            "purpose": "MBA/PGDM admissions in IIMs and many top B-schools.",
            "eligibility": "Bachelor degree with required aggregate as per official criteria.",
            "pattern": "CBT with VARC, DILR, and QA sections.",
            "timeline": "Notification: Jul-Aug | Exam: Nov | Results: Dec-Jan",
            "prep_tips": [
                "Build sectional strategy with timed mocks.",
                "Analyze every mock deeply, not just score.",
                "Keep daily quant and reading practice.",
            ],
            "difficulty": 4,
            "trusted_sources": [
                ("CAT Official", "https://iimcat.ac.in/"),
            ],
        },
        {
            "name": "XAT",
            "purpose": "MBA admissions in XLRI and other participating institutes.",
            "eligibility": "Bachelor degree in any discipline.",
            "pattern": "Decision Making + Verbal/Logical + Quant + GK/Essay components.",
            "timeline": "Application: Jul-Dec | Exam: Jan",
            "prep_tips": [
                "Practice decision-making caselets separately.",
                "Train for higher verbal difficulty.",
                "Take mocks aligned with XAT format.",
            ],
            "difficulty": 4,
            "trusted_sources": [
                ("XAT Official", "https://xatonline.in/"),
            ],
        },
        {
            "name": "GMAT",
            "purpose": "MBA/business school admissions in India and abroad.",
            "eligibility": "No strict degree stream restriction; institute criteria apply.",
            "pattern": "Standardized adaptive test (Quant, Verbal, Data Insights).",
            "timeline": "Year-round scheduling",
            "prep_tips": [
                "Use adaptive mock tests for pacing.",
                "Focus on weak area diagnostics each week.",
                "Plan attempts based on application deadlines.",
            ],
            "difficulty": 3,
            "trusted_sources": [
                ("GMAT Official", "https://www.mba.com/exams/gmat-exam"),
            ],
        },
    ],
    "Abroad Studies": [
        {
            "name": "GRE",
            "purpose": "MS/PhD admissions in many international universities.",
            "eligibility": "Open to graduates/final-year students; university criteria vary.",
            "pattern": "Verbal Reasoning, Quantitative Reasoning, Analytical Writing.",
            "timeline": "Year-round slots (center availability based)",
            "prep_tips": [
                "Build vocabulary systematically.",
                "Practice quant with timed accuracy drills.",
                "Write weekly AWA essays for feedback.",
            ],
            "difficulty": 3,
            "trusted_sources": [
                ("GRE Official", "https://www.ets.org/gre.html"),
            ],
        },
        {
            "name": "TOEFL",
            "purpose": "English proficiency proof for global admissions.",
            "eligibility": "Open test; score requirements depend on university.",
            "pattern": "Reading, Listening, Speaking, Writing.",
            "timeline": "Multiple test dates throughout the year",
            "prep_tips": [
                "Practice note-taking from audio passages.",
                "Use speaking templates for fluency.",
                "Work on timed writing responses.",
            ],
            "difficulty": 2,
            "trusted_sources": [
                ("TOEFL Official", "https://www.ets.org/toefl.html"),
            ],
        },
        {
            "name": "IELTS",
            "purpose": "English proficiency for admissions, visa, and migration pathways.",
            "eligibility": "Open test; institution/country cutoff applies.",
            "pattern": "Listening, Reading, Writing, Speaking (Academic/General).",
            "timeline": "Frequent test dates year-round",
            "prep_tips": [
                "Practice band-descriptor based writing.",
                "Improve speaking through daily mock prompts.",
                "Use official sample tests for pacing.",
            ],
            "difficulty": 2,
            "trusted_sources": [
                ("IELTS Official", "https://ielts.org/"),
            ],
        },
    ],
}


JOB_OPPORTUNITIES = [
    {
        "role": "Software Development Engineer",
        "focus": "Product and service companies (frontend, backend, full-stack).",
        "entry_route": "Campus placements, off-campus drives, coding contests, internships.",
        "skills": "DSA, one backend language, SQL, Git, project deployment.",
        "where_to_apply": "Company career pages, LinkedIn, Naukri, Internshala, referral networks.",
    },
    {
        "role": "Data Analyst / BI Analyst",
        "focus": "Analytics teams in IT, fintech, e-commerce, consulting.",
        "entry_route": "Internships, analyst trainee roles, certification-backed applications.",
        "skills": "SQL, Excel, Python, Power BI/Tableau, statistics basics.",
        "where_to_apply": "LinkedIn jobs, analytics hiring portals, campus drives.",
    },
    {
        "role": "AI/ML Engineer (Entry Level)",
        "focus": "AI product startups and R&D-focused organizations.",
        "entry_route": "Strong projects + internships + research/public portfolios.",
        "skills": "Python, ML basics, model evaluation, data preprocessing, APIs.",
        "where_to_apply": "Startup boards, GitHub-backed profiles, direct hiring pages.",
    },
    {
        "role": "Core Engineering Roles",
        "focus": "Mechanical, Civil, Electrical, Electronics domain jobs.",
        "entry_route": "Campus placements, GATE-based hiring, state and private sector hiring.",
        "skills": "Core subject depth, CAD/tools, technical documentation, practical exposure.",
        "where_to_apply": "Core company portals, PSU notifications, apprenticeship drives.",
    },
    {
        "role": "Government Engineer (JE/AE/ESE)",
        "focus": "Public works, railways, power, central/state engineering services.",
        "entry_route": "SSC JE, State PSC, ESE, department recruitment exams.",
        "skills": "Technical syllabus + aptitude + current affairs + consistent revision.",
        "where_to_apply": "UPSC, SSC, state PSC, department recruitment portals.",
    },
    {
        "role": "PSU Engineer",
        "focus": "Public sector companies across energy, oil, power, telecom, infra.",
        "entry_route": "Primarily GATE score + interview/selection rounds.",
        "skills": "High GATE score, technical interview readiness, communication.",
        "where_to_apply": "Official PSU websites and GATE-linked recruitment notices.",
    },
]


def _difficulty_label(level: int) -> str:
    labels = {
        1: "Very Easy",
        2: "Easy",
        3: "Moderate",
        4: "Hard",
        5: "Very Hard",
    }
    return labels.get(level, "Moderate")


def _difficulty_badge(level: int) -> str:
    clamped = max(1, min(level, 5))
    filled = "*" * clamped
    empty = "-" * (5 - clamped)
    return f"{filled}{empty}  {_difficulty_label(level)}"


def render_exams_tab() -> None:
    st.subheader("Engineering Exams (India)")
    st.caption("Exam details are supported by trusted official websites. Use source links for latest updates.")

    category_options = ["All"] + list(EXAM_CATEGORIES.keys())
    selected_category = st.selectbox("Choose exam category", category_options)

    categories_to_show = list(EXAM_CATEGORIES.keys())
    if selected_category != "All":
        categories_to_show = [selected_category]

    for category in categories_to_show:
        st.markdown(f"### {category}")
        exams = EXAM_CATEGORIES[category]

        for exam in exams:
            with st.expander(f"{exam['name']}  |  Difficulty: {_difficulty_badge(exam['difficulty'])}"):
                st.markdown(f"**Purpose:** {exam['purpose']}")
                st.markdown(f"**Eligibility:** {exam['eligibility']}")
                st.markdown(f"**Exam Pattern:** {exam['pattern']}")
                st.markdown(f"**Important Timeline:** {exam['timeline']}")
                st.markdown("**Preparation Tips:**")
                for tip in exam["prep_tips"]:
                    st.markdown(f"- {tip}")
                if exam.get("trusted_sources"):
                    st.markdown("**Trusted Source(s):**")
                    for source_name, source_url in exam["trusted_sources"]:
                        st.markdown(f"- [{source_name}]({source_url})")


def render_jobs_tab() -> None:
    st.subheader("Job Opportunities for Engineering Students")
    st.caption("Practical roles and entry routes that are commonly relevant in India.")

    for job in JOB_OPPORTUNITIES:
        with st.container(border=True):
            st.markdown(f"### {job['role']}")
            st.markdown(f"**Where this role fits:** {job['focus']}")
            st.markdown(f"**Entry route:** {job['entry_route']}")
            st.markdown(f"**Key skills to build:** {job['skills']}")
            st.markdown(f"**Where to apply:** {job['where_to_apply']}")


def show_exams_jobs_page() -> None:
    """Render complete Exams and Jobs page."""
    st.header("Exams and Jobs")
    st.caption("Structured guidance for engineering students in India.")

    tab_exams, tab_jobs = st.tabs(["Exams", "Job Opportunities"])

    with tab_exams:
        render_exams_tab()

    with tab_jobs:
        render_jobs_tab()

    st.info(
        "Exam dates and patterns can change each cycle. Always verify final details on official exam websites before applying."
    )
