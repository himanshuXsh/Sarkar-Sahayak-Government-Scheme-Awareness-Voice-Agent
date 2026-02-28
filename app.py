import streamlit as st
import asyncio
import threading
import queue
import time
import os
from dotenv import load_dotenv

load_dotenv()

# ---------- Page Config ----------
st.set_page_config(
    page_title="Sarkar Sahayak - Government Scheme Assistant",
    page_icon="🇮🇳",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ---------- Custom CSS ----------
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Tiro+Devanagari+Hindi&family=DM+Sans:wght@300;400;500;600;700&display=swap');

:root {
    --saffron: #FF6B1A;
    --deep-green: #0A6E3F;
    --white: #FAFAF8;
    --navy: #0D1B2A;
    --gold: #D4A017;
    --light-bg: #F4F1EB;
    --card-bg: #FFFFFF;
    --border: #E8E2D6;
    --text-primary: #1A1A1A;
    --text-muted: #6B6B6B;
}

html, body, [class*="css"] {
    font-family: 'DM Sans', sans-serif;
    background-color: var(--light-bg);
}

/* Hide Streamlit branding */
#MainMenu, footer, header {visibility: hidden;}
.stDeployButton {display: none;}

/* Main background */
.main .block-container {
    padding: 1.5rem 2rem;
    max-width: 1400px;
}

/* ---- HEADER ---- */
.hero-header {
    background: linear-gradient(135deg, var(--navy) 0%, #1a3a5c 50%, var(--deep-green) 100%);
    border-radius: 20px;
    padding: 2rem 2.5rem;
    margin-bottom: 1.5rem;
    position: relative;
    overflow: hidden;
}
.hero-header::before {
    content: "🇮🇳";
    position: absolute;
    right: 2rem;
    top: 50%;
    transform: translateY(-50%);
    font-size: 5rem;
    opacity: 0.12;
}
.hero-header::after {
    content: "";
    position: absolute;
    top: 0; left: 0; right: 0;
    height: 4px;
    background: linear-gradient(90deg, var(--saffron), var(--white), var(--deep-green));
}
.hero-title {
    color: white;
    font-size: 2rem;
    font-weight: 700;
    margin: 0;
    letter-spacing: -0.5px;
}
.hero-subtitle {
    color: rgba(255,255,255,0.75);
    font-size: 1rem;
    margin-top: 0.4rem;
    font-weight: 300;
}
.hero-badge {
    display: inline-block;
    background: rgba(255,107,26,0.2);
    border: 1px solid var(--saffron);
    color: #FFB347;
    font-size: 0.7rem;
    padding: 3px 10px;
    border-radius: 20px;
    margin-bottom: 0.8rem;
    letter-spacing: 1px;
    text-transform: uppercase;
    font-weight: 600;
}

/* ---- CARDS ---- */
.scheme-card {
    background: var(--card-bg);
    border: 1px solid var(--border);
    border-radius: 14px;
    padding: 1.2rem;
    margin-bottom: 0.8rem;
    position: relative;
    overflow: hidden;
}
.scheme-card::before {
    content: "";
    position: absolute;
    left: 0; top: 0; bottom: 0;
    width: 3px;
    background: var(--saffron);
    border-radius: 3px 0 0 3px;
}
.scheme-icon {
    font-size: 1.8rem;
    margin-bottom: 0.4rem;
}
.scheme-name {
    font-weight: 600;
    font-size: 0.9rem;
    color: var(--text-primary);
    margin-bottom: 0.2rem;
}
.scheme-desc {
    font-size: 0.75rem;
    color: var(--text-muted);
    line-height: 1.4;
}
.scheme-tag {
    display: inline-block;
    background: #FFF3E8;
    color: var(--saffron);
    font-size: 0.65rem;
    padding: 2px 8px;
    border-radius: 10px;
    margin-top: 0.4rem;
    font-weight: 600;
}

/* ---- CHAT ---- */
.chat-container {
    background: var(--card-bg);
    border: 1px solid var(--border);
    border-radius: 16px;
    height: 420px;
    overflow-y: auto;
    padding: 1.2rem;
    margin-bottom: 1rem;
}
.chat-container::-webkit-scrollbar { width: 4px; }
.chat-container::-webkit-scrollbar-track { background: transparent; }
.chat-container::-webkit-scrollbar-thumb { background: var(--border); border-radius: 2px; }

.msg-user {
    display: flex;
    justify-content: flex-end;
    margin-bottom: 0.8rem;
}
.msg-agent {
    display: flex;
    justify-content: flex-start;
    margin-bottom: 0.8rem;
    align-items: flex-start;
    gap: 0.5rem;
}
.bubble-user {
    background: linear-gradient(135deg, var(--saffron), #FF8C42);
    color: white;
    padding: 0.7rem 1rem;
    border-radius: 18px 18px 4px 18px;
    max-width: 75%;
    font-size: 0.88rem;
    line-height: 1.5;
    box-shadow: 0 2px 8px rgba(255,107,26,0.25);
}
.bubble-agent {
    background: var(--light-bg);
    color: var(--text-primary);
    padding: 0.7rem 1rem;
    border-radius: 18px 18px 18px 4px;
    max-width: 75%;
    font-size: 0.88rem;
    line-height: 1.5;
    border: 1px solid var(--border);
}
.agent-avatar {
    width: 32px; height: 32px;
    background: linear-gradient(135deg, var(--deep-green), #0ea05c);
    border-radius: 50%;
    display: flex; align-items: center; justify-content: center;
    font-size: 0.9rem;
    flex-shrink: 0;
}
.msg-time {
    font-size: 0.65rem;
    color: var(--text-muted);
    margin-top: 3px;
    text-align: right;
}

/* ---- MIC SECTION ---- */
.mic-section {
    background: var(--card-bg);
    border: 1px solid var(--border);
    border-radius: 16px;
    padding: 1.2rem;
    text-align: center;
    margin-bottom: 1rem;
}

/* Streamlit button overrides */
.stButton > button {
    background: linear-gradient(135deg, var(--saffron), #FF8C42) !important;
    color: white !important;
    border: none !important;
    border-radius: 12px !important;
    font-weight: 600 !important;
    font-size: 0.85rem !important;
    transition: all 0.2s !important;
}
.stButton > button:hover {
    box-shadow: 0 4px 15px rgba(255,107,26,0.4) !important;
    transform: translateY(-1px) !important;
}

/* Sidebar */
section[data-testid="stSidebar"] {
    background: var(--navy) !important;
}
section[data-testid="stSidebar"] * {
    color: rgba(255,255,255,0.85) !important;
}

/* Text input */
.stTextInput > div > div > input {
    border-radius: 12px !important;
    border: 1px solid var(--border) !important;
    font-size: 0.9rem !important;
    background: var(--card-bg) !important;
}
.stTextInput > div > div > input:focus {
    border-color: var(--saffron) !important;
    box-shadow: 0 0 0 2px rgba(255,107,26,0.15) !important;
}

.section-title {
    font-size: 0.75rem;
    font-weight: 700;
    color: var(--text-muted);
    text-transform: uppercase;
    letter-spacing: 1.5px;
    margin-bottom: 0.8rem;
    padding-bottom: 0.4rem;
    border-bottom: 1px solid var(--border);
}
</style>
""", unsafe_allow_html=True)

# ---------- Session State ----------
if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "agent",
            "content": "🙏 Namaste! Main aapka Sarkar Sahayak hoon. Aaj main aapko sarkari yojanaon ke baare mein jaankari dene ke liye yahan hoon. Aap kaunsi yojana ke baare mein jaanna chahte hain?",
            "time": "Now"
        }
    ]
if "selected_language" not in st.session_state:
    st.session_state.selected_language = "hi-IN"

# ---------- Schemes Data ----------
SCHEMES = [
    {"icon": "🌾", "name": "PM Kisan Samman Nidhi", "desc": "Kisan parivaaron ko ₹6000/year", "tag": "Farmers", "query": "PM Kisan Samman Nidhi yojana ke baare mein batao aur kaise milega?"},
    {"icon": "🏥", "name": "Ayushman Bharat", "desc": "₹5 lakh tak free health insurance", "tag": "Health", "query": "Ayushman Bharat card kaise banwayein aur kya documents chahiye?"},
    {"icon": "🏠", "name": "PM Awas Yojana", "desc": "Garib parivaaron ko pucca ghar", "tag": "Housing", "query": "PM Awas Yojana ke liye apply kaise karein?"},
    {"icon": "👧", "name": "Sukanya Samriddhi", "desc": "Beti ke liye savings scheme", "tag": "Girl Child", "query": "Sukanya Samriddhi Yojana ke baare mein batao aur account kaise kholein?"},
    {"icon": "🔥", "name": "PM Ujjwala Yojana", "desc": "BPL parivaaron ko free LPG connection", "tag": "Energy", "query": "Ujjwala Yojana ka free gas connection kaise milega?"},
    {"icon": "💼", "name": "MGNREGA", "desc": "100 din ka rozgar guarantee", "tag": "Employment", "query": "MGNREGA job card kaise banwayein aur kya eligibility hai?"},
    {"icon": "🏦", "name": "PM Jan Dhan Yojana", "desc": "Zero balance bank account + insurance", "tag": "Finance", "query": "Jan Dhan account kaise kholein aur kya fayde hain?"},
    {"icon": "📈", "name": "PM Mudra Yojana", "desc": "Small business ke liye ₹10 lakh loan", "tag": "Business", "query": "Mudra loan ke liye apply kaise karein aur kya eligibility hai?"},
]

LANGUAGES = {
    "Hindi (हिंदी)": "hi-IN",
    "English": "en-IN",
    "Tamil (தமிழ்)": "ta-IN",
    "Telugu (తెలుగు)": "te-IN",
    "Bengali (বাংলা)": "bn-IN",
    "Gujarati (ગુજરાતી)": "gu-IN",
    "Kannada (ಕನ್ನಡ)": "kn-IN",
    "Marathi (मराठी)": "mr-IN",
    "Auto Detect": "unknown",
}

QUICK_QUESTIONS = [
    "Kisan hoon, mujhe kya milega?",
    "Free hospital treatment kaise?",
    "Beti ke liye koi scheme?",
    "Ghar banane ki scheme?",
    "Rozgar guarantee kya hai?",
    "Small business loan kaise milega?",
]

def get_ai_response(user_msg, language):
    try:
        from groq import Groq
        client = Groq(api_key=os.getenv("GROQ_API_KEY"))

        lang_names = {v: k for k, v in LANGUAGES.items()}
        lang_name = lang_names.get(language, "Hindi")

        system_prompt = f"""You are Sarkar Sahayak, a helpful government scheme awareness assistant for Indian citizens.

Respond in {lang_name} language. If auto-detect, use Hindi.
Keep responses concise (3-5 sentences), friendly and easy to understand.
Use simple language, no complex jargon.

Key schemes:
- PM Kisan Samman Nidhi (farmer income ₹6000/year, need Aadhaar + bank account)
- Ayushman Bharat (health insurance ₹5 lakh, PM-JAY card)
- PM Awas Yojana (pucca house for BPL families)
- Sukanya Samriddhi Yojana (girl child savings, open at post office/bank)
- PM Ujjwala Yojana (free LPG to BPL women)
- MGNREGA (100 days job guarantee, job card required)
- PM Jan Dhan Yojana (zero balance account, ₹2 lakh accident insurance)
- PM Mudra Yojana (business loans: Shishu ₹50k, Kishor ₹5L, Tarun ₹10L)
- Atal Pension Yojana (pension ₹1000-5000/month)
- Skill India Mission (free skill training)

Always end with: "Kya aur kuch jaanna chahte hain? 🙏" """

        messages = [{"role": "system", "content": system_prompt}]
        for msg in st.session_state.messages[-6:]:
            role = "user" if msg["role"] == "user" else "assistant"
            messages.append({"role": role, "content": msg["content"]})
        messages.append({"role": "user", "content": user_msg})

        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=messages,
            max_tokens=350,
            temperature=0.7
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Maafi chahta hoon, abhi response nahi de pa raha. Kripya GROQ_API_KEY check karein. Error: {str(e)[:100]}"

def send_message(text):
    if text.strip():
        now = time.strftime("%I:%M %p")
        st.session_state.messages.append({"role": "user", "content": text, "time": now})
        with st.spinner("🤔 Soch raha hoon..."):
            response = get_ai_response(text, st.session_state.selected_language)
        st.session_state.messages.append({"role": "agent", "content": response, "time": time.strftime("%I:%M %p")})

# =================== SIDEBAR ===================
with st.sidebar:
    st.markdown("""
    <div style="padding: 1rem 0 0.5rem;">
        <div style="font-size:1.5rem; font-weight:800; color:white;">🇮🇳 Sarkar Sahayak</div>
        <div style="font-size:0.75rem; color:rgba(255,255,255,0.4); margin-top:4px;">Government Scheme Assistant</div>
    </div>
    <hr style="border-color:rgba(255,255,255,0.1); margin:0.8rem 0;"/>
    """, unsafe_allow_html=True)

    # Language Selector
    st.markdown('<div style="font-size:0.7rem; color:rgba(255,255,255,0.4); text-transform:uppercase; letter-spacing:1.5px; margin-bottom:6px;">🌐 Language / भाषा</div>', unsafe_allow_html=True)
    selected_lang_name = st.selectbox("Language", list(LANGUAGES.keys()), index=0, label_visibility="collapsed")
    st.session_state.selected_language = LANGUAGES[selected_lang_name]

    st.markdown('<hr style="border-color:rgba(255,255,255,0.1); margin:0.8rem 0;"/>', unsafe_allow_html=True)
    st.markdown('<div style="font-size:0.7rem; color:rgba(255,255,255,0.4); text-transform:uppercase; letter-spacing:1.5px; margin-bottom:8px;">⚡ Quick Questions</div>', unsafe_allow_html=True)

    for q in QUICK_QUESTIONS:
        if st.button(f"→ {q}", key=f"qs_{q}", use_container_width=True):
            send_message(q)
            st.rerun()

    st.markdown('<hr style="border-color:rgba(255,255,255,0.1); margin:0.8rem 0;"/>', unsafe_allow_html=True)

    # Status
    groq_key = os.getenv("GROQ_API_KEY", "")
    lk_url = os.getenv("LIVEKIT_URL", "")

    if groq_key:
        st.markdown('<div style="display:flex;align-items:center;gap:8px;font-size:0.78rem;"><span style="width:8px;height:8px;background:#2ecc71;border-radius:50%;display:inline-block;box-shadow:0 0 5px #2ecc71;"></span>Groq LLM ✓</div>', unsafe_allow_html=True)
    else:
        st.markdown('<div style="display:flex;align-items:center;gap:8px;font-size:0.78rem;"><span style="width:8px;height:8px;background:#e74c3c;border-radius:50%;display:inline-block;"></span>GROQ_API_KEY missing</div>', unsafe_allow_html=True)

    if lk_url:
        st.markdown('<div style="display:flex;align-items:center;gap:8px;font-size:0.78rem;margin-top:4px;"><span style="width:8px;height:8px;background:#2ecc71;border-radius:50%;display:inline-block;box-shadow:0 0 5px #2ecc71;"></span>LiveKit Configured ✓</div>', unsafe_allow_html=True)
    else:
        st.markdown('<div style="display:flex;align-items:center;gap:8px;font-size:0.78rem;margin-top:4px;"><span style="width:8px;height:8px;background:#f39c12;border-radius:50%;display:inline-block;"></span>LiveKit not configured</div>', unsafe_allow_html=True)

    st.markdown('<hr style="border-color:rgba(255,255,255,0.1); margin:0.8rem 0;"/>', unsafe_allow_html=True)
    if st.button("🗑️ Clear Chat", use_container_width=True):
        st.session_state.messages = [st.session_state.messages[0]]
        st.rerun()

# =================== MAIN CONTENT ===================

# Hero Header
st.markdown("""
<div class="hero-header">
    <div class="hero-badge">🇮🇳 Digital India Initiative</div>
    <div class="hero-title">Sarkar Sahayak — सरकार सहायक</div>
    <div class="hero-subtitle">Sarkari yojanaon ki jaankari ab aapki bhasha mein &nbsp;•&nbsp; Voice + Text Support &nbsp;•&nbsp; 9 Indian Languages</div>
</div>
""", unsafe_allow_html=True)

col_chat, col_schemes = st.columns([3, 2], gap="large")

# ---- CHAT COLUMN ----
with col_chat:
    st.markdown('<div class="section-title">💬 Chat with Agent</div>', unsafe_allow_html=True)

    # Voice info box
    st.markdown("""
    <div class="mic-section">
        <div style="font-size:1.8rem;">🎙️</div>
        <div style="font-weight:600; font-size:0.85rem; color:#1A1A1A; margin:4px 0;">Voice Support Available</div>
        <div style="font-size:0.78rem; color:#6B6B6B;">
            Voice ke liye agent terminal mein run karein:<br>
            <code style="background:#F4F1EB; padding:2px 8px; border-radius:6px; display:inline-block; margin:4px 0;">python scheme_awareness_agent.py dev</code><br>
            Phir jao: <a href="https://agents-playground.livekit.io" target="_blank" style="color:#0A6E3F; font-weight:600;">agents-playground.livekit.io</a>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Chat messages
    chat_html = '<div class="chat-container">'
    for msg in st.session_state.messages:
        if msg["role"] == "user":
            chat_html += f"""
            <div class="msg-user">
                <div>
                    <div class="bubble-user">{msg['content']}</div>
                    <div class="msg-time">{msg.get('time','')}</div>
                </div>
            </div>"""
        else:
            chat_html += f"""
            <div class="msg-agent">
                <div class="agent-avatar">🤖</div>
                <div>
                    <div class="bubble-agent">{msg['content']}</div>
                    <div class="msg-time">{msg.get('time','')}</div>
                </div>
            </div>"""
    chat_html += '</div>'
    st.markdown(chat_html, unsafe_allow_html=True)

    # Text input form
    with st.form("chat_form", clear_on_submit=True):
        c1, c2 = st.columns([5, 1])
        with c1:
            user_input = st.text_input(
                "msg",
                placeholder="Yojana ke baare mein puchein... Hindi ya English mein",
                label_visibility="collapsed"
            )
        with c2:
            submitted = st.form_submit_button("Send →")
        if submitted and user_input:
            send_message(user_input)
            st.rerun()

# ---- SCHEMES COLUMN ----
with col_schemes:
    st.markdown('<div class="section-title">📋 Popular Government Schemes</div>', unsafe_allow_html=True)

    for scheme in SCHEMES:
        c1, c2 = st.columns([4, 1])
        with c1:
            st.markdown(f"""
            <div class="scheme-card">
                <div class="scheme-icon">{scheme['icon']}</div>
                <div class="scheme-name">{scheme['name']}</div>
                <div class="scheme-desc">{scheme['desc']}</div>
                <span class="scheme-tag">{scheme['tag']}</span>
            </div>
            """, unsafe_allow_html=True)
        with c2:
            st.write("")
            if st.button("Ask", key=f"sc_{scheme['name']}", use_container_width=True):
                send_message(scheme['query'])
                st.rerun()

# Footer
st.markdown("""
<div style="text-align:center; padding:1.5rem 0 0.5rem; color:#9B9B9B; font-size:0.72rem; border-top:1px solid #E8E2D6; margin-top:1rem;">
    Powered by <strong>Groq LLaMA 3.3</strong> + <strong>Sarvam AI</strong> (STT/TTS) + <strong>LiveKit</strong> &nbsp;|&nbsp;
    Accurate info ke liye hamesha official govt portals visit karein: <strong>india.gov.in</strong>
</div>
""", unsafe_allow_html=True)
