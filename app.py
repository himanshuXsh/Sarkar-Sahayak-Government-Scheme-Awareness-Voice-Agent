import streamlit as st
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

# ---------- Language UI Translations ----------
UI_TEXT = {
    "hi-IN": {
        "hero_badge": "🇮🇳 डिजिटल इंडिया पहल",
        "hero_title": "सरकार सहायक — Sarkar Sahayak",
        "hero_subtitle": "सरकारी योजनाओं की जानकारी अब आपकी भाषा में • वॉइस + टेक्स्ट सपोर्ट • 9 भारतीय भाषाएं",
        "chat_title": "💬 एजेंट से बात करें",
        "schemes_title": "📋 लोकप्रिय सरकारी योजनाएं",
        "voice_title": "वॉइस सपोर्ट उपलब्ध",
        "voice_desc": "वॉइस के लिए एजेंट टर्मिनल में चलाएं:",
        "voice_then": "फिर जाएं:",
        "placeholder": "योजना के बारे में पूछें... हिंदी या अंग्रेजी में",
        "send_btn": "भेजें →",
        "quick_q_title": "⚡ त्वरित प्रश्न",
        "lang_label": "🌐 भाषा चुनें",
        "clear_chat": "🗑️ चैट साफ करें",
        "groq_ok": "Groq LLM ✓",
        "groq_missing": "GROQ_API_KEY नहीं मिला",
        "lk_ok": "LiveKit कॉन्फ़िगर ✓",
        "lk_missing": "LiveKit कॉन्फ़िगर नहीं",
        "footer": "सटीक जानकारी के लिए हमेशा आधिकारिक सरकारी पोर्टल देखें:",
        "ask_btn": "पूछें",
        "greeting": "🙏 नमस्ते! मैं आपका सरकार सहायक हूं। आज मैं आपको सरकारी योजनाओं के बारे में जानकारी देने के लिए यहां हूं। आप कौनसी योजना के बारे में जानना चाहते हैं?",
        "quick_questions": [
            "किसान हूं, मुझे क्या मिलेगा?",
            "मुफ्त अस्पताल इलाज कैसे?",
            "बेटी के लिए कोई योजना?",
            "घर बनाने की योजना?",
            "रोजगार गारंटी क्या है?",
            "छोटे व्यवसाय के लिए लोन?",
        ],
    },
    "en-IN": {
        "hero_badge": "🇮🇳 Digital India Initiative",
        "hero_title": "Sarkar Sahayak — Government Assistant",
        "hero_subtitle": "Government scheme information in your language • Voice + Text Support • 9 Indian Languages",
        "chat_title": "💬 Chat with Agent",
        "schemes_title": "📋 Popular Government Schemes",
        "voice_title": "Voice Support Available",
        "voice_desc": "For voice, run agent in terminal:",
        "voice_then": "Then visit:",
        "placeholder": "Ask about any scheme... in Hindi or English",
        "send_btn": "Send →",
        "quick_q_title": "⚡ Quick Questions",
        "lang_label": "🌐 Language",
        "clear_chat": "🗑️ Clear Chat",
        "groq_ok": "Groq LLM ✓",
        "groq_missing": "GROQ_API_KEY missing",
        "lk_ok": "LiveKit Configured ✓",
        "lk_missing": "LiveKit not configured",
        "footer": "For accurate info always visit official govt portals:",
        "ask_btn": "Ask",
        "greeting": "🙏 Hello! I am your Sarkar Sahayak. I am here to help you with information about government welfare schemes. Which scheme would you like to know about?",
        "quick_questions": [
            "I'm a farmer, what can I get?",
            "How to get free hospital treatment?",
            "Any scheme for my daughter?",
            "Scheme for building a house?",
            "What is employment guarantee?",
            "Loan for small business?",
        ],
    },
    "ta-IN": {
        "hero_badge": "🇮🇳 டிஜிட்டல் இந்தியா",
        "hero_title": "சர்கார் சஹாயக் — அரசு உதவியாளர்",
        "hero_subtitle": "அரசு திட்டங்கள் பற்றிய தகவல்கள் உங்கள் மொழியில் • குரல் + உரை ஆதரவு",
        "chat_title": "💬 முகவருடன் பேசுங்கள்",
        "schemes_title": "📋 பிரபலமான அரசு திட்டங்கள்",
        "voice_title": "குரல் ஆதரவு கிடைக்கிறது",
        "voice_desc": "குரலுக்கு டெர்மினலில் இயக்கவும்:",
        "voice_then": "பிறகு செல்லவும்:",
        "placeholder": "திட்டத்தைப் பற்றி கேளுங்கள்...",
        "send_btn": "அனுப்பு →",
        "quick_q_title": "⚡ விரைவு கேள்விகள்",
        "lang_label": "🌐 மொழி",
        "clear_chat": "🗑️ அரட்டையை அழி",
        "groq_ok": "Groq LLM ✓",
        "groq_missing": "GROQ_API_KEY இல்லை",
        "lk_ok": "LiveKit உள்ளமைக்கப்பட்டது ✓",
        "lk_missing": "LiveKit உள்ளமைக்கப்படவில்லை",
        "footer": "துல்லியமான தகவலுக்கு அதிகாரப்பூர்வ அரசு தளங்களை பார்வையிடவும்:",
        "ask_btn": "கேளு",
        "greeting": "🙏 வணக்கம்! நான் உங்கள் சர்கார் சஹாயக். அரசு நலத் திட்டங்களைப் பற்றி உங்களுக்கு தகவல் தர இங்கே இருக்கிறேன். எந்த திட்டத்தைப் பற்றி தெரிந்துகொள்ள விரும்புகிறீர்கள்?",
        "quick_questions": [
            "நான் விவசாயி, எனக்கு என்ன கிடைக்கும்?",
            "இலவச மருத்துவமனை சிகிச்சை எப்படி?",
            "மகளுக்கு ஏதாவது திட்டம்?",
            "வீடு கட்ட திட்டம்?",
            "வேலை உத்தரவாதம் என்ன?",
            "சிறு தொழிலுக்கு கடன்?",
        ],
    },
    "te-IN": {
        "hero_badge": "🇮🇳 డిజిటల్ ఇండియా",
        "hero_title": "సర్కార్ సహాయక్ — ప్రభుత్వ సహాయకుడు",
        "hero_subtitle": "ప్రభుత్వ పథకాల సమాచారం మీ భాషలో • వాయిస్ + టెక్స్ట్ మద్దతు",
        "chat_title": "💬 ఏజెంట్‌తో చాట్ చేయండి",
        "schemes_title": "📋 ప్రముఖ ప్రభుత్వ పథకాలు",
        "voice_title": "వాయిస్ సపోర్ట్ అందుబాటులో ఉంది",
        "voice_desc": "వాయిస్ కోసం టెర్మినల్‌లో అమలు చేయండి:",
        "voice_then": "తర్వాత వెళ్ళండి:",
        "placeholder": "పథకం గురించి అడగండి...",
        "send_btn": "పంపు →",
        "quick_q_title": "⚡ త్వరిత ప్రశ్నలు",
        "lang_label": "🌐 భాష",
        "clear_chat": "🗑️ చాట్ క్లియర్ చేయండి",
        "groq_ok": "Groq LLM ✓",
        "groq_missing": "GROQ_API_KEY లేదు",
        "lk_ok": "LiveKit కాన్ఫిగర్ ✓",
        "lk_missing": "LiveKit కాన్ఫిగర్ కాలేదు",
        "footer": "ఖచ్చితమైన సమాచారం కోసం అధికారిక ప్రభుత్వ పోర్టల్‌లను సందర్శించండి:",
        "ask_btn": "అడగండి",
        "greeting": "🙏 నమస్కారం! నేను మీ సర్కార్ సహాయక్. ప్రభుత్వ సంక్షేమ పథకాల గురించి మీకు సమాచారం అందించడానికి ఇక్కడ ఉన్నాను. మీరు ఏ పథకం గురించి తెలుసుకోవాలనుకుంటున్నారు?",
        "quick_questions": [
            "నేను రైతుని, నాకు ఏమి లభిస్తుంది?",
            "ఉచిత ఆసుపత్రి చికిత్స ఎలా?",
            "అమ్మాయికి ఏదైనా పథకం?",
            "ఇల్లు కట్టడానికి పథకం?",
            "ఉపాధి హమీ అంటే ఏమిటి?",
            "చిన్న వ్యాపారానికి రుణం?",
        ],
    },
    "bn-IN": {
        "hero_badge": "🇮🇳 ডিজিটাল ইন্ডিয়া",
        "hero_title": "সরকার সহায়ক — সরকারি সহায়তা",
        "hero_subtitle": "সরকারি প্রকল্পের তথ্য এখন আপনার ভাষায় • ভয়েস + টেক্সট সাপোর্ট",
        "chat_title": "💬 এজেন্টের সাথে কথা বলুন",
        "schemes_title": "📋 জনপ্রিয় সরকারি প্রকল্প",
        "voice_title": "ভয়েস সাপোর্ট উপলব্ধ",
        "voice_desc": "ভয়েসের জন্য টার্মিনালে চালান:",
        "voice_then": "তারপর যান:",
        "placeholder": "প্রকল্প সম্পর্কে জিজ্ঞেস করুন...",
        "send_btn": "পাঠান →",
        "quick_q_title": "⚡ দ্রুত প্রশ্ন",
        "lang_label": "🌐 ভাষা",
        "clear_chat": "🗑️ চ্যাট মুছুন",
        "groq_ok": "Groq LLM ✓",
        "groq_missing": "GROQ_API_KEY নেই",
        "lk_ok": "LiveKit কনফিগার ✓",
        "lk_missing": "LiveKit কনফিগার হয়নি",
        "footer": "সঠিক তথ্যের জন্য সবসময় সরকারি পোর্টাল দেখুন:",
        "ask_btn": "জিজ্ঞেস",
        "greeting": "🙏 নমস্কার! আমি আপনার সরকার সহায়ক। সরকারি প্রকল্প সম্পর্কে আপনাকে তথ্য দিতে এখানে আছি। আপনি কোন প্রকল্প সম্পর্কে জানতে চান?",
        "quick_questions": [
            "আমি কৃষক, আমি কী পাবো?",
            "বিনামূল্যে হাসপাতাল চিকিৎসা কীভাবে?",
            "মেয়ের জন্য কোনো প্রকল্প?",
            "বাড়ি তৈরির প্রকল্প?",
            "কর্মসংস্থান গ্যারান্টি কী?",
            "ছোট ব্যবসার জন্য ঋণ?",
        ],
    },
    "gu-IN": {
        "hero_badge": "🇮🇳 ડિજિટલ ઇન્ડિયા",
        "hero_title": "સરકાર સહાયક — સરકારી સહાયક",
        "hero_subtitle": "સરકારી યોજનાઓની માહિતી હવે તમારી ભાષામાં • વૉઇસ + ટેક્સ્ટ સપોર્ટ",
        "chat_title": "💬 એજન્ટ સાથે વાત કરો",
        "schemes_title": "📋 લોકપ્રિય સરકારી યોજનાઓ",
        "voice_title": "વૉઇસ સપોર્ટ ઉપલબ્ધ",
        "voice_desc": "વૉઇસ માટે ટર્મિનલમાં ચલાવો:",
        "voice_then": "પછી જાઓ:",
        "placeholder": "યોજના વિશે પૂછો...",
        "send_btn": "મોકલો →",
        "quick_q_title": "⚡ ઝડપી પ્રશ્નો",
        "lang_label": "🌐 ભાષા",
        "clear_chat": "🗑️ ચૅટ સાફ કરો",
        "groq_ok": "Groq LLM ✓",
        "groq_missing": "GROQ_API_KEY નથી",
        "lk_ok": "LiveKit કૉન્ફિગર ✓",
        "lk_missing": "LiveKit કૉન્ફિગર નથી",
        "footer": "સચોટ માહિતી માટે હંમેશા સત્તાવાર સરકારી પોર્ટલ જુઓ:",
        "ask_btn": "પૂછો",
        "greeting": "🙏 નમસ્તે! હું તમારો સરકાર સહાયક છું. સરકારી કલ્યાણ યોજનાઓ વિશે તમને માહિતી આપવા અહીં છું. તમે કઈ યોજના વિશે જાણવા માંગો છો?",
        "quick_questions": [
            "હું ખેડૂત છું, મને શું મળશે?",
            "મફત હોસ્પિટલ સારવાર કેવી રીતે?",
            "દીકરી માટે કોઈ યોજના?",
            "ઘર બાંધવા માટે યોજના?",
            "રોજગાર ગેરંટી શું છે?",
            "નાના વ્યવસાય માટે લોન?",
        ],
    },
    "kn-IN": {
        "hero_badge": "🇮🇳 ಡಿಜಿಟಲ್ ಇಂಡಿಯಾ",
        "hero_title": "ಸರ್ಕಾರ್ ಸಹಾಯಕ್ — ಸರ್ಕಾರಿ ಸಹಾಯಕ",
        "hero_subtitle": "ಸರ್ಕಾರಿ ಯೋಜನೆಗಳ ಮಾಹಿತಿ ಇಲ್ಲಿ ನಿಮ್ಮ ಭಾಷೆಯಲ್ಲಿ • ಧ್ವನಿ + ಪಠ್ಯ ಬೆಂಬಲ",
        "chat_title": "💬 ಏಜೆಂಟ್‌ನೊಂದಿಗೆ ಮಾತನಾಡಿ",
        "schemes_title": "📋 ಜನಪ್ರಿಯ ಸರ್ಕಾರಿ ಯೋಜನೆಗಳು",
        "voice_title": "ಧ್ವನಿ ಬೆಂಬಲ ಲಭ್ಯವಿದೆ",
        "voice_desc": "ಧ್ವನಿಗಾಗಿ ಟರ್ಮಿನಲ್‌ನಲ್ಲಿ ರನ್ ಮಾಡಿ:",
        "voice_then": "ನಂತರ ಹೋಗಿ:",
        "placeholder": "ಯೋಜನೆಯ ಬಗ್ಗೆ ಕೇಳಿ...",
        "send_btn": "ಕಳುಹಿಸಿ →",
        "quick_q_title": "⚡ ತ್ವರಿತ ಪ್ರಶ್ನೆಗಳು",
        "lang_label": "🌐 ಭಾಷೆ",
        "clear_chat": "🗑️ ಚಾಟ್ ತೆರವು",
        "groq_ok": "Groq LLM ✓",
        "groq_missing": "GROQ_API_KEY ಇಲ್ಲ",
        "lk_ok": "LiveKit ಕಾನ್ಫಿಗರ್ ✓",
        "lk_missing": "LiveKit ಕಾನ್ಫಿಗರ್ ಆಗಿಲ್ಲ",
        "footer": "ನಿಖರ ಮಾಹಿತಿಗಾಗಿ ಯಾವಾಗಲೂ ಅಧಿಕೃತ ಸರ್ಕಾರಿ ಪೋರ್ಟಲ್‌ಗಳನ್ನು ನೋಡಿ:",
        "ask_btn": "ಕೇಳಿ",
        "greeting": "🙏 ನಮಸ್ಕಾರ! ನಾನು ನಿಮ್ಮ ಸರ್ಕಾರ್ ಸಹಾಯಕ್. ಸರ್ಕಾರಿ ಕಲ್ಯಾಣ ಯೋಜನೆಗಳ ಬಗ್ಗೆ ಮಾಹಿತಿ ನೀಡಲು ಇಲ್ಲಿದ್ದೇನೆ. ನೀವು ಯಾವ ಯೋಜನೆ ಬಗ್ಗೆ ತಿಳಿಯಲು ಬಯಸುತ್ತೀರಿ?",
        "quick_questions": [
            "ನಾನು ರೈತ, ನನಗೆ ಏನು ಸಿಗುತ್ತದೆ?",
            "ಉಚಿತ ಆಸ್ಪತ್ರೆ ಚಿಕಿತ್ಸೆ ಹೇಗೆ?",
            "ಹೆಣ್ಣುಮಗಳಿಗೆ ಯೋಜನೆ?",
            "ಮನೆ ಕಟ್ಟಲು ಯೋಜನೆ?",
            "ಉದ್ಯೋಗ ಖಾತ್ರಿ ಎಂದರೇನು?",
            "ಸಣ್ಣ ವ್ಯಾಪಾರಕ್ಕೆ ಸಾಲ?",
        ],
    },
    "mr-IN": {
        "hero_badge": "🇮🇳 डिजिटल इंडिया",
        "hero_title": "सरकार सहायक — सरकारी सहाय्यक",
        "hero_subtitle": "सरकारी योजनांची माहिती आता तुमच्या भाषेत • आवाज + मजकूर समर्थन",
        "chat_title": "💬 एजंटशी बोला",
        "schemes_title": "📋 लोकप्रिय सरकारी योजना",
        "voice_title": "व्हॉइस सपोर्ट उपलब्ध",
        "voice_desc": "व्हॉइससाठी टर्मिनलमध्ये चालवा:",
        "voice_then": "मग जा:",
        "placeholder": "योजनेबद्दल विचारा...",
        "send_btn": "पाठवा →",
        "quick_q_title": "⚡ जलद प्रश्न",
        "lang_label": "🌐 भाषा",
        "clear_chat": "🗑️ चॅट साफ करा",
        "groq_ok": "Groq LLM ✓",
        "groq_missing": "GROQ_API_KEY नाही",
        "lk_ok": "LiveKit कॉन्फिगर ✓",
        "lk_missing": "LiveKit कॉन्फिगर नाही",
        "footer": "अचूक माहितीसाठी नेहमी अधिकृत सरकारी पोर्टल पहा:",
        "ask_btn": "विचारा",
        "greeting": "🙏 नमस्कार! मी तुमचा सरकार सहायक आहे. सरकारी कल्याण योजनांबद्दल तुम्हाला माहिती देण्यासाठी येथे आहे. तुम्हाला कोणत्या योजनेबद्दल जाणून घ्यायचे आहे?",
        "quick_questions": [
            "मी शेतकरी आहे, मला काय मिळेल?",
            "मोफत रुग्णालय उपचार कसे?",
            "मुलीसाठी कोणती योजना?",
            "घर बांधण्यासाठी योजना?",
            "रोजगार हमी काय आहे?",
            "लहान व्यवसायासाठी कर्ज?",
        ],
    },
    "unknown": {
        "hero_badge": "🇮🇳 Digital India Initiative",
        "hero_title": "Sarkar Sahayak — सरकार सहायक",
        "hero_subtitle": "Government scheme info in your language • Voice + Text • 9 Indian Languages",
        "chat_title": "💬 Chat with Agent",
        "schemes_title": "📋 Popular Government Schemes",
        "voice_title": "Voice Support Available",
        "voice_desc": "For voice, run agent in terminal:",
        "voice_then": "Then visit:",
        "placeholder": "Ask about any scheme...",
        "send_btn": "Send →",
        "quick_q_title": "⚡ Quick Questions",
        "lang_label": "🌐 Language / भाषा",
        "clear_chat": "🗑️ Clear Chat",
        "groq_ok": "Groq LLM ✓",
        "groq_missing": "GROQ_API_KEY missing",
        "lk_ok": "LiveKit Configured ✓",
        "lk_missing": "LiveKit not configured",
        "footer": "For accurate info always visit official govt portals:",
        "ask_btn": "Ask",
        "greeting": "🙏 Namaste! Main aapka Sarkar Sahayak hoon. Aaj main aapko sarkari yojanaon ke baare mein jaankari dene ke liye yahan hoon. Aap kaunsi yojana ke baare mein jaanna chahte hain?",
        "quick_questions": [
            "Kisan hoon, mujhe kya milega?",
            "Free hospital treatment kaise?",
            "Beti ke liye koi scheme?",
            "Ghar banane ki scheme?",
            "Rozgar guarantee kya hai?",
            "Small business loan kaise milega?",
        ],
    },
}

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

#MainMenu, footer, header {visibility: hidden;}
.stDeployButton {display: none;}

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
.scheme-icon { font-size: 1.8rem; margin-bottom: 0.4rem; }
.scheme-name { font-weight: 600; font-size: 0.9rem; color: var(--text-primary); margin-bottom: 0.2rem; }
.scheme-desc { font-size: 0.75rem; color: var(--text-muted); line-height: 1.4; }
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

.msg-user { display: flex; justify-content: flex-end; margin-bottom: 0.8rem; }
.msg-agent { display: flex; justify-content: flex-start; margin-bottom: 0.8rem; align-items: flex-start; gap: 0.5rem; }
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
.msg-time { font-size: 0.65rem; color: var(--text-muted); margin-top: 3px; text-align: right; }

/* ---- MIC SECTION ---- */
.mic-section {
    background: var(--card-bg);
    border: 1px solid var(--border);
    border-radius: 16px;
    padding: 1.2rem;
    text-align: center;
    margin-bottom: 1rem;
}

/* ---- BUTTONS ---- */
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

/* ---- SIDEBAR ---- */
section[data-testid="stSidebar"] {
    background: var(--navy) !important;
}
section[data-testid="stSidebar"] * {
    color: rgba(255,255,255,0.85) !important;
}

/* ---- INPUT FIX: DARK BACKGROUND + VISIBLE TEXT ---- */
.stTextInput > div > div > input,
div[data-testid="stForm"] input[type="text"],
div[data-testid="stForm"] textarea,
input[type="text"],
textarea {
    background-color: #1A1A2E !important;
    color: #FFFFFF !important;
    border: 1.5px solid #FF6B1A !important;
    border-radius: 12px !important;
    font-size: 0.9rem !important;
    caret-color: #FF6B1A !important;
}
.stTextInput > div > div > input:focus,
div[data-testid="stForm"] input[type="text"]:focus {
    border-color: #FF8C42 !important;
    box-shadow: 0 0 0 3px rgba(255,107,26,0.2) !important;
    outline: none !important;
}
input::placeholder, textarea::placeholder {
    color: rgba(255,255,255,0.4) !important;
}

/* Form container dark background */
div[data-testid="stForm"] {
    background: #111827 !important;
    border: 1px solid #2D2D2D !important;
    border-radius: 14px !important;
    padding: 0.8rem !important;
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
if "selected_language" not in st.session_state:
    st.session_state.selected_language = "hi-IN"
if "prev_language" not in st.session_state:
    st.session_state.prev_language = "hi-IN"

# Get current UI text
lang = st.session_state.selected_language
T = UI_TEXT.get(lang, UI_TEXT["hi-IN"])

# Reset greeting if language changed
if st.session_state.prev_language != lang:
    st.session_state.messages = [
        {"role": "agent", "content": T["greeting"], "time": "Now"}
    ]
    st.session_state.prev_language = lang

if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "agent", "content": T["greeting"], "time": "Now"}
    ]

# ---------- Schemes Data (names stay consistent, desc in Hindi/relevant) ----------
SCHEMES = [
    {"icon": "🌾", "name": "PM Kisan Samman Nidhi", "desc": "₹6000/year for farmer families", "tag": "Farmers", "query": "PM Kisan Samman Nidhi yojana ke baare mein batao aur kaise milega?"},
    {"icon": "🏥", "name": "Ayushman Bharat", "desc": "₹5 lakh free health insurance", "tag": "Health", "query": "Ayushman Bharat card kaise banwayein aur kya documents chahiye?"},
    {"icon": "🏠", "name": "PM Awas Yojana", "desc": "Pucca house for poor families", "tag": "Housing", "query": "PM Awas Yojana ke liye apply kaise karein?"},
    {"icon": "👧", "name": "Sukanya Samriddhi", "desc": "Savings scheme for girl child", "tag": "Girl Child", "query": "Sukanya Samriddhi Yojana ke baare mein batao aur account kaise kholein?"},
    {"icon": "🔥", "name": "PM Ujjwala Yojana", "desc": "Free LPG connection for BPL families", "tag": "Energy", "query": "Ujjwala Yojana ka free gas connection kaise milega?"},
    {"icon": "💼", "name": "MGNREGA", "desc": "100 days employment guarantee", "tag": "Employment", "query": "MGNREGA job card kaise banwayein aur kya eligibility hai?"},
    {"icon": "🏦", "name": "PM Jan Dhan Yojana", "desc": "Zero balance account + insurance", "tag": "Finance", "query": "Jan Dhan account kaise kholein aur kya fayde hain?"},
    {"icon": "📈", "name": "PM Mudra Yojana", "desc": "Business loan up to ₹10 lakh", "tag": "Business", "query": "Mudra loan ke liye apply kaise karein aur kya eligibility hai?"},
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

Always end with a question asking if they want to know more, in the appropriate language. 🙏"""

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
    st.markdown(f"""
    <div style="padding: 1rem 0 0.5rem;">
        <div style="font-size:1.5rem; font-weight:800; color:white;">🇮🇳 Sarkar Sahayak</div>
        <div style="font-size:0.75rem; color:rgba(255,255,255,0.4); margin-top:4px;">Government Scheme Assistant</div>
    </div>
    <hr style="border-color:rgba(255,255,255,0.1); margin:0.8rem 0;"/>
    """, unsafe_allow_html=True)

    st.markdown(f'<div style="font-size:0.7rem; color:rgba(255,255,255,0.4); text-transform:uppercase; letter-spacing:1.5px; margin-bottom:6px;">{T["lang_label"]}</div>', unsafe_allow_html=True)
    
    current_lang_name = {v: k for k, v in LANGUAGES.items()}.get(st.session_state.selected_language, "Hindi (हिंदी)")
    lang_list = list(LANGUAGES.keys())
    default_idx = lang_list.index(current_lang_name) if current_lang_name in lang_list else 0
    
    selected_lang_name = st.selectbox("Language", lang_list, index=default_idx, label_visibility="collapsed")
    new_lang = LANGUAGES[selected_lang_name]
    
    if new_lang != st.session_state.selected_language:
        st.session_state.selected_language = new_lang
        st.rerun()

    st.markdown('<hr style="border-color:rgba(255,255,255,0.1); margin:0.8rem 0;"/>', unsafe_allow_html=True)
    st.markdown(f'<div style="font-size:0.7rem; color:rgba(255,255,255,0.4); text-transform:uppercase; letter-spacing:1.5px; margin-bottom:8px;">{T["quick_q_title"]}</div>', unsafe_allow_html=True)

    for q in T["quick_questions"]:
        if st.button(f"→ {q}", key=f"qs_{q}", use_container_width=True):
            send_message(q)
            st.rerun()

    st.markdown('<hr style="border-color:rgba(255,255,255,0.1); margin:0.8rem 0;"/>', unsafe_allow_html=True)

    groq_key = os.getenv("GROQ_API_KEY", "")
    lk_url = os.getenv("LIVEKIT_URL", "")

    if groq_key:
        st.markdown(f'<div style="display:flex;align-items:center;gap:8px;font-size:0.78rem;"><span style="width:8px;height:8px;background:#2ecc71;border-radius:50%;display:inline-block;box-shadow:0 0 5px #2ecc71;"></span>{T["groq_ok"]}</div>', unsafe_allow_html=True)
    else:
        st.markdown(f'<div style="display:flex;align-items:center;gap:8px;font-size:0.78rem;"><span style="width:8px;height:8px;background:#e74c3c;border-radius:50%;display:inline-block;"></span>{T["groq_missing"]}</div>', unsafe_allow_html=True)

    if lk_url:
        st.markdown(f'<div style="display:flex;align-items:center;gap:8px;font-size:0.78rem;margin-top:4px;"><span style="width:8px;height:8px;background:#2ecc71;border-radius:50%;display:inline-block;box-shadow:0 0 5px #2ecc71;"></span>{T["lk_ok"]}</div>', unsafe_allow_html=True)
    else:
        st.markdown(f'<div style="display:flex;align-items:center;gap:8px;font-size:0.78rem;margin-top:4px;"><span style="width:8px;height:8px;background:#f39c12;border-radius:50%;display:inline-block;"></span>{T["lk_missing"]}</div>', unsafe_allow_html=True)

    st.markdown('<hr style="border-color:rgba(255,255,255,0.1); margin:0.8rem 0;"/>', unsafe_allow_html=True)
    if st.button(T["clear_chat"], use_container_width=True):
        st.session_state.messages = [{"role": "agent", "content": T["greeting"], "time": "Now"}]
        st.rerun()

# =================== MAIN CONTENT ===================
st.markdown(f"""
<div class="hero-header">
    <div class="hero-badge">{T["hero_badge"]}</div>
    <div class="hero-title">{T["hero_title"]}</div>
    <div class="hero-subtitle">{T["hero_subtitle"]}</div>
</div>
""", unsafe_allow_html=True)

col_chat, col_schemes = st.columns([3, 2], gap="large")

# ---- CHAT COLUMN ----
with col_chat:
    st.markdown(f'<div class="section-title">{T["chat_title"]}</div>', unsafe_allow_html=True)

    st.markdown(f"""
    <div class="mic-section">
        <div style="font-size:1.8rem;">🎙️</div>
        <div style="font-weight:600; font-size:0.85rem; color:#1A1A1A; margin:4px 0;">{T["voice_title"]}</div>
        <div style="font-size:0.78rem; color:#6B6B6B;">
            {T["voice_desc"]}<br>
            <code style="background:#F4F1EB; padding:2px 8px; border-radius:6px; display:inline-block; margin:4px 0;">python scheme_awareness_agent.py dev</code><br>
            {T["voice_then"]} <a href="https://agents-playground.livekit.io" target="_blank" style="color:#0A6E3F; font-weight:600;">agents-playground.livekit.io</a>
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

    # Text input form — dark themed
    with st.form("chat_form", clear_on_submit=True):
        c1, c2 = st.columns([5, 1])
        with c1:
            user_input = st.text_input(
                "msg",
                placeholder=T["placeholder"],
                label_visibility="collapsed"
            )
        with c2:
            submitted = st.form_submit_button(T["send_btn"])
        if submitted and user_input:
            send_message(user_input)
            st.rerun()

# ---- SCHEMES COLUMN ----
with col_schemes:
    st.markdown(f'<div class="section-title">{T["schemes_title"]}</div>', unsafe_allow_html=True)

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
            if st.button(T["ask_btn"], key=f"sc_{scheme['name']}", use_container_width=True):
                send_message(scheme['query'])
                st.rerun()

# Footer
st.markdown(f"""
<div style="text-align:center; padding:1.5rem 0 0.5rem; color:#9B9B9B; font-size:0.72rem; border-top:1px solid #E8E2D6; margin-top:1rem;">
    Powered by <strong>Groq LLaMA 3.3</strong> + <strong>Sarvam AI</strong> (STT/TTS) + <strong>LiveKit</strong> &nbsp;|&nbsp;
    {T["footer"]} <strong>india.gov.in</strong>
</div>
""", unsafe_allow_html=True)
