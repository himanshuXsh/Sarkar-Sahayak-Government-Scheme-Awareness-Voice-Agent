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

# ---------- UI Translations ----------
UI_TEXT = {
    "hi-IN": {
        "badge": "🇮🇳 डिजिटल इंडिया पहल",
        "title": "सरकार सहायक — Sarkar Sahayak",
        "subtitle": "सरकारी योजनाओं की जानकारी अब आपकी भाषा में • वॉइस + टेक्स्ट सपोर्ट • 9 भारतीय भाषाएं",
        "chat_title": "💬 एजेंट से बात करें",
        "schemes_title": "📋 लोकप्रिय सरकारी योजनाएं",
        "voice_title": "वॉइस सपोर्ट उपलब्ध",
        "voice_desc": "वॉइस के लिए एजेंट टर्मिनल में चलाएं:",
        "voice_then": "फिर जाएं:",
        "placeholder": "योजना के बारे में पूछें... हिंदी या English में",
        "send_btn": "भेजें →",
        "clear_btn": "🗑️ चैट साफ करें",
        "lang_label": "🌐 भाषा",
        "quick_q_label": "⚡ त्वरित प्रश्न",
        "status_groq_ok": "Groq LLM ✓",
        "status_groq_miss": "GROQ_API_KEY नहीं है",
        "status_lk_ok": "LiveKit कॉन्फ़िगर ✓",
        "status_lk_miss": "LiveKit कॉन्फ़िगर नहीं",
        "ask_btn": "पूछें",
        "footer": "Powered by <strong>Groq LLaMA 3.3</strong> + <strong>Sarvam AI</strong> (STT/TTS) + <strong>LiveKit</strong> &nbsp;|&nbsp; सटीक जानकारी के लिए हमेशा आधिकारिक सरकारी पोर्टल देखें: <strong>india.gov.in</strong>",
        "welcome": "🙏 नमस्ते! मैं आपका सरकार सहायक हूं। आज मैं आपको सरकारी योजनाओं के बारे में जानकारी देने के लिए यहां हूं। आप कौन सी योजना के बारे में जानना चाहते हैं?",
        "quick_questions": [
            "किसान हूं, मुझे क्या मिलेगा?",
            "फ्री हॉस्पिटल ट्रीटमेंट कैसे?",
            "बेटी के लिए कोई योजना?",
            "घर बनाने की योजना?",
            "रोजगार गारंटी क्या है?",
            "Small business loan कैसे मिलेगा?",
        ],
    },
    "en-IN": {
        "badge": "🇮🇳 Digital India Initiative",
        "title": "Sarkar Sahayak — Government Assistant",
        "subtitle": "Government scheme information in your language • Voice + Text Support • 9 Indian Languages",
        "chat_title": "💬 Chat with Agent",
        "schemes_title": "📋 Popular Government Schemes",
        "voice_title": "Voice Support Available",
        "voice_desc": "For voice, run the agent in terminal:",
        "voice_then": "Then visit:",
        "placeholder": "Ask about any scheme... in Hindi or English",
        "send_btn": "Send →",
        "clear_btn": "🗑️ Clear Chat",
        "lang_label": "🌐 Language",
        "quick_q_label": "⚡ Quick Questions",
        "status_groq_ok": "Groq LLM ✓",
        "status_groq_miss": "GROQ_API_KEY missing",
        "status_lk_ok": "LiveKit Configured ✓",
        "status_lk_miss": "LiveKit not configured",
        "ask_btn": "Ask",
        "footer": "Powered by <strong>Groq LLaMA 3.3</strong> + <strong>Sarvam AI</strong> (STT/TTS) + <strong>LiveKit</strong> &nbsp;|&nbsp; For accurate info always visit official govt portals: <strong>india.gov.in</strong>",
        "welcome": "🙏 Hello! I am your Sarkar Sahayak. I am here to help you with information about government welfare schemes. Which scheme would you like to know about?",
        "quick_questions": [
            "I'm a farmer, what can I get?",
            "How to get free hospital treatment?",
            "Any scheme for daughter?",
            "Scheme for building a house?",
            "What is employment guarantee?",
            "How to get small business loan?",
        ],
    },
    "ta-IN": {
        "badge": "🇮🇳 டிஜிட்டல் இந்தியா முன்முயற்சி",
        "title": "சர்கார் சஹாயக் — அரசு உதவியாளர்",
        "subtitle": "அரசு திட்டங்கள் பற்றிய தகவல்கள் இப்போது உங்கள் மொழியில் • குரல் + உரை ஆதரவு",
        "chat_title": "💬 முகவருடன் அரட்டை",
        "schemes_title": "📋 பிரபலமான அரசு திட்டங்கள்",
        "voice_title": "குரல் ஆதரவு கிடைக்கிறது",
        "voice_desc": "குரலுக்கு, முனையத்தில் முகவரை இயக்கவும்:",
        "voice_then": "பிறகு செல்லவும்:",
        "placeholder": "திட்டத்தைப் பற்றி கேளுங்கள்...",
        "send_btn": "அனுப்பு →",
        "clear_btn": "🗑️ அரட்டை அழி",
        "lang_label": "🌐 மொழி",
        "quick_q_label": "⚡ விரைவு கேள்விகள்",
        "status_groq_ok": "Groq LLM ✓",
        "status_groq_miss": "GROQ_API_KEY இல்லை",
        "status_lk_ok": "LiveKit கட்டமைக்கப்பட்டது ✓",
        "status_lk_miss": "LiveKit கட்டமைக்கப்படவில்லை",
        "ask_btn": "கேள்",
        "footer": "Powered by <strong>Groq LLaMA 3.3</strong> + <strong>Sarvam AI</strong> + <strong>LiveKit</strong> &nbsp;|&nbsp; துல்லியமான தகவலுக்கு: <strong>india.gov.in</strong>",
        "welcome": "🙏 வணக்கம்! நான் உங்கள் சர்கார் சஹாயக். அரசு திட்டங்கள் பற்றி தகவல் தர இங்கே இருக்கிறேன். நீங்கள் எந்த திட்டத்தைப் பற்றி அறிய விரும்புகிறீர்கள்?",
        "quick_questions": [
            "விவசாயி, எனக்கு என்ன கிடைக்கும்?",
            "இலவச மருத்துவமனை சிகிச்சை?",
            "மகளுக்கு திட்டம்?",
            "வீடு கட்ட திட்டம்?",
            "வேலை உத்தரவாதம் என்ன?",
            "சிறு வணிக கடன்?",
        ],
    },
    "te-IN": {
        "badge": "🇮🇳 డిజిటల్ ఇండియా చొరవ",
        "title": "సర్కార్ సహాయక్ — ప్రభుత్వ సహాయకుడు",
        "subtitle": "ప్రభుత్వ పథకాల సమాచారం ఇప్పుడు మీ భాషలో • వాయిస్ + టెక్స్ట్ సపోర్ట్",
        "chat_title": "💬 ఏజెంట్‌తో చాట్",
        "schemes_title": "📋 ప్రముఖ ప్రభుత్వ పథకాలు",
        "voice_title": "వాయిస్ సపోర్ట్ అందుబాటులో ఉంది",
        "voice_desc": "వాయిస్ కోసం, టెర్మినల్‌లో ఏజెంట్ రన్ చేయండి:",
        "voice_then": "తర్వాత వెళ్ళండి:",
        "placeholder": "పథకం గురించి అడగండి...",
        "send_btn": "పంపు →",
        "clear_btn": "🗑️ చాట్ క్లియర్",
        "lang_label": "🌐 భాష",
        "quick_q_label": "⚡ త్వరిత ప్రశ్నలు",
        "status_groq_ok": "Groq LLM ✓",
        "status_groq_miss": "GROQ_API_KEY లేదు",
        "status_lk_ok": "LiveKit కాన్ఫిగర్ ✓",
        "status_lk_miss": "LiveKit కాన్ఫిగర్ కాలేదు",
        "ask_btn": "అడగు",
        "footer": "Powered by <strong>Groq LLaMA 3.3</strong> + <strong>Sarvam AI</strong> + <strong>LiveKit</strong> &nbsp;|&nbsp; ఖచ్చితమైన సమాచారానికి: <strong>india.gov.in</strong>",
        "welcome": "🙏 నమస్కారం! నేను మీ సర్కార్ సహాయక్. ప్రభుత్వ పథకాల గురించి సమాచారం ఇవ్వడానికి ఇక్కడ ఉన్నాను. మీరు ఏ పథకం గురించి తెలుసుకోవాలనుకుంటున్నారు?",
        "quick_questions": [
            "రైతుకు ఏమి దొరుకుతుంది?",
            "ఉచిత ఆసుపత్రి చికిత్స?",
            "అమ్మాయికి పథకం?",
            "ఇల్లు కట్టే పథకం?",
            "ఉపాధి హామీ ఏమిటి?",
            "చిన్న వ్యాపార రుణం?",
        ],
    },
    "bn-IN": {
        "badge": "🇮🇳 ডিজিটাল ইন্ডিয়া উদ্যোগ",
        "title": "সরকার সহায়ক — সরকারি সহকারী",
        "subtitle": "সরকারি প্রকল্পের তথ্য এখন আপনার ভাষায় • ভয়েস + টেক্সট সাপোর্ট",
        "chat_title": "💬 এজেন্টের সাথে চ্যাট",
        "schemes_title": "📋 জনপ্রিয় সরকারি প্রকল্প",
        "voice_title": "ভয়েস সাপোর্ট উপলব্ধ",
        "voice_desc": "ভয়েসের জন্য, টার্মিনালে এজেন্ট চালান:",
        "voice_then": "তারপর যান:",
        "placeholder": "প্রকল্প সম্পর্কে জিজ্ঞেস করুন...",
        "send_btn": "পাঠান →",
        "clear_btn": "🗑️ চ্যাট মুছুন",
        "lang_label": "🌐 ভাষা",
        "quick_q_label": "⚡ দ্রুত প্রশ্ন",
        "status_groq_ok": "Groq LLM ✓",
        "status_groq_miss": "GROQ_API_KEY নেই",
        "status_lk_ok": "LiveKit কনফিগার ✓",
        "status_lk_miss": "LiveKit কনফিগার নয়",
        "ask_btn": "জিজ্ঞেস করুন",
        "footer": "Powered by <strong>Groq LLaMA 3.3</strong> + <strong>Sarvam AI</strong> + <strong>LiveKit</strong> &nbsp;|&nbsp; সঠিক তথ্যের জন্য: <strong>india.gov.in</strong>",
        "welcome": "🙏 নমস্কার! আমি আপনার সরকার সহায়ক। সরকারি প্রকল্প সম্পর্কে তথ্য দিতে এখানে আছি। আপনি কোন প্রকল্প সম্পর্কে জানতে চান?",
        "quick_questions": [
            "কৃষক, আমি কী পাব?",
            "বিনামূল্যে হাসপাতাল চিকিৎসা?",
            "মেয়ের জন্য প্রকল্প?",
            "বাড়ি তৈরির প্রকল্প?",
            "কর্মসংস্থান গ্যারান্টি কী?",
            "ছোট ব্যবসায় ঋণ?",
        ],
    },
    "gu-IN": {
        "badge": "🇮🇳 ડિજિટલ ઈન્ડિયા પહેલ",
        "title": "સરકાર સહાયક — સરકારી સહાયક",
        "subtitle": "સરકારી યોજનાઓની માહિતી હવે તમારી ભાષામાં • વૉઇસ + ટેક્સ્ટ સપોર્ટ",
        "chat_title": "💬 એજન્ટ સાથે ચેટ",
        "schemes_title": "📋 લોકપ્રિય સરકારી યોજનાઓ",
        "voice_title": "વૉઇસ સપોર્ટ ઉપલબ્ધ",
        "voice_desc": "વૉઇસ માટે, ટર્મિનલમાં એજન્ટ ચલાવો:",
        "voice_then": "પછી જાઓ:",
        "placeholder": "યોજના વિશે પૂછો...",
        "send_btn": "મોકલો →",
        "clear_btn": "🗑️ ચેટ સાફ કરો",
        "lang_label": "🌐 ભાષા",
        "quick_q_label": "⚡ ઝડપી પ્રશ્નો",
        "status_groq_ok": "Groq LLM ✓",
        "status_groq_miss": "GROQ_API_KEY નથી",
        "status_lk_ok": "LiveKit ગોઠવ્યું ✓",
        "status_lk_miss": "LiveKit ગોઠવ્યું નથી",
        "ask_btn": "પૂછો",
        "footer": "Powered by <strong>Groq LLaMA 3.3</strong> + <strong>Sarvam AI</strong> + <strong>LiveKit</strong> &nbsp;|&nbsp; સચોટ માહિતી માટે: <strong>india.gov.in</strong>",
        "welcome": "🙏 નમસ્કાર! હું તમારો સરકાર સહાયક છું. સરકારી યોજનાઓ વિશે માહિતી આપવા માટે અહીં છું. તમે કઈ યોજના વિશે જાણવા માગો છો?",
        "quick_questions": [
            "ખેડૂત છું, મને શું મળશે?",
            "ફ્રી હોસ્પિટલ સારવાર?",
            "દીકરી માટે કોઈ યોજના?",
            "ઘર બનાવવાની યોજના?",
            "રોજગાર ગેરંટી શું છે?",
            "નાના ધંધા માટે લોન?",
        ],
    },
    "kn-IN": {
        "badge": "🇮🇳 ಡಿಜಿಟಲ್ ಇಂಡಿಯಾ ಉಪಕ್ರಮ",
        "title": "ಸರ್ಕಾರ್ ಸಹಾಯಕ — ಸರ್ಕಾರಿ ಸಹಾಯಕ",
        "subtitle": "ಸರ್ಕಾರಿ ಯೋಜನೆಗಳ ಮಾಹಿತಿ ಈಗ ನಿಮ್ಮ ಭಾಷೆಯಲ್ಲಿ • ಧ್ವನಿ + ಪಠ್ಯ ಬೆಂಬಲ",
        "chat_title": "💬 ಏಜೆಂಟ್ ಜೊತೆ ಚಾಟ್",
        "schemes_title": "📋 ಜನಪ್ರಿಯ ಸರ್ಕಾರಿ ಯೋಜನೆಗಳು",
        "voice_title": "ಧ್ವನಿ ಬೆಂಬಲ ಲಭ್ಯವಿದೆ",
        "voice_desc": "ಧ್ವನಿಗಾಗಿ, ಟರ್ಮಿನಲ್‌ನಲ್ಲಿ ಏಜೆಂಟ್ ಚಲಾಯಿಸಿ:",
        "voice_then": "ನಂತರ ಹೋಗಿ:",
        "placeholder": "ಯೋಜನೆಯ ಬಗ್ಗೆ ಕೇಳಿ...",
        "send_btn": "ಕಳುಹಿಸು →",
        "clear_btn": "🗑️ ಚಾಟ್ ತೆರವು",
        "lang_label": "🌐 ಭಾಷೆ",
        "quick_q_label": "⚡ ತ್ವರಿತ ಪ್ರಶ್ನೆಗಳು",
        "status_groq_ok": "Groq LLM ✓",
        "status_groq_miss": "GROQ_API_KEY ಇಲ್ಲ",
        "status_lk_ok": "LiveKit ಕಾನ್ಫಿಗರ್ ✓",
        "status_lk_miss": "LiveKit ಕಾನ್ಫಿಗರ್ ಆಗಿಲ್ಲ",
        "ask_btn": "ಕೇಳಿ",
        "footer": "Powered by <strong>Groq LLaMA 3.3</strong> + <strong>Sarvam AI</strong> + <strong>LiveKit</strong> &nbsp;|&nbsp; ನಿಖರ ಮಾಹಿತಿಗೆ: <strong>india.gov.in</strong>",
        "welcome": "🙏 ನಮಸ್ಕಾರ! ನಾನು ನಿಮ್ಮ ಸರ್ಕಾರ್ ಸಹಾಯಕ. ಸರ್ಕಾರಿ ಯೋಜನೆಗಳ ಬಗ್ಗೆ ಮಾಹಿತಿ ನೀಡಲು ಇಲ್ಲಿದ್ದೇನೆ. ನೀವು ಯಾವ ಯೋಜನೆಯ ಬಗ್ಗೆ ತಿಳಿಯಲು ಬಯಸುತ್ತೀರಿ?",
        "quick_questions": [
            "ರೈತ, ನನಗೇನು ಸಿಗುತ್ತದೆ?",
            "ಉಚಿತ ಆಸ್ಪತ್ರೆ ಚಿಕಿತ್ಸೆ?",
            "ಮಗಳಿಗೆ ಯೋಜನೆ?",
            "ಮನೆ ಕಟ್ಟಲು ಯೋಜನೆ?",
            "ಉದ್ಯೋಗ ಗ್ಯಾರಂಟಿ ಏನು?",
            "ಸಣ್ಣ ವ್ಯವಹಾರ ಸಾಲ?",
        ],
    },
    "mr-IN": {
        "badge": "🇮🇳 डिजिटल इंडिया उपक्रम",
        "title": "सरकार सहायक — शासकीय सहाय्यक",
        "subtitle": "सरकारी योजनांची माहिती आता तुमच्या भाषेत • व्हॉइस + टेक्स्ट सपोर्ट",
        "chat_title": "💬 एजंटशी चॅट करा",
        "schemes_title": "📋 लोकप्रिय सरकारी योजना",
        "voice_title": "व्हॉइस सपोर्ट उपलब्ध",
        "voice_desc": "व्हॉइससाठी, टर्मिनलमध्ये एजंट चालवा:",
        "voice_then": "नंतर जा:",
        "placeholder": "योजनेबद्दल विचारा...",
        "send_btn": "पाठवा →",
        "clear_btn": "🗑️ चॅट साफ करा",
        "lang_label": "🌐 भाषा",
        "quick_q_label": "⚡ त्वरित प्रश्न",
        "status_groq_ok": "Groq LLM ✓",
        "status_groq_miss": "GROQ_API_KEY नाही",
        "status_lk_ok": "LiveKit कॉन्फिगर ✓",
        "status_lk_miss": "LiveKit कॉन्फिगर नाही",
        "ask_btn": "विचारा",
        "footer": "Powered by <strong>Groq LLaMA 3.3</strong> + <strong>Sarvam AI</strong> + <strong>LiveKit</strong> &nbsp;|&nbsp; अचूक माहितीसाठी: <strong>india.gov.in</strong>",
        "welcome": "🙏 नमस्कार! मी तुमचा सरकार सहायक आहे. सरकारी योजनांबद्दल माहिती देण्यासाठी येथे आहे. तुम्हाला कोणत्या योजनेबद्दल जाणून घ्यायचे आहे?",
        "quick_questions": [
            "शेतकरी आहे, मला काय मिळेल?",
            "मोफत रुग्णालय उपचार?",
            "मुलीसाठी योजना?",
            "घर बांधण्याची योजना?",
            "रोजगार हमी काय आहे?",
            "लघु व्यवसाय कर्ज?",
        ],
    },
    "pa-IN": {
        "badge": "🇮🇳 ਡਿਜੀਟਲ ਇੰਡੀਆ ਪਹਿਲ",
        "title": "ਸਰਕਾਰ ਸਹਾਇਕ — ਸਰਕਾਰੀ ਸਹਾਇਕ",
        "subtitle": "ਸਰਕਾਰੀ ਯੋਜਨਾਵਾਂ ਦੀ ਜਾਣਕਾਰੀ ਹੁਣ ਤੁਹਾਡੀ ਭਾਸ਼ਾ ਵਿੱਚ • ਵੌਇਸ + ਟੈਕਸਟ ਸਪੋਰਟ",
        "chat_title": "💬 ਏਜੰਟ ਨਾਲ ਚੈਟ",
        "schemes_title": "📋 ਪ੍ਰਸਿੱਧ ਸਰਕਾਰੀ ਯੋਜਨਾਵਾਂ",
        "voice_title": "ਵੌਇਸ ਸਪੋਰਟ ਉਪਲਬਧ",
        "voice_desc": "ਵੌਇਸ ਲਈ, ਟਰਮੀਨਲ ਵਿੱਚ ਏਜੰਟ ਚਲਾਓ:",
        "voice_then": "ਫਿਰ ਜਾਓ:",
        "placeholder": "ਯੋਜਨਾ ਬਾਰੇ ਪੁੱਛੋ...",
        "send_btn": "ਭੇਜੋ →",
        "clear_btn": "🗑️ ਚੈਟ ਸਾਫ਼ ਕਰੋ",
        "lang_label": "🌐 ਭਾਸ਼ਾ",
        "quick_q_label": "⚡ ਤੇਜ਼ ਸਵਾਲ",
        "status_groq_ok": "Groq LLM ✓",
        "status_groq_miss": "GROQ_API_KEY ਨਹੀਂ",
        "status_lk_ok": "LiveKit ਕਨਫਿਗਰ ✓",
        "status_lk_miss": "LiveKit ਕਨਫਿਗਰ ਨਹੀਂ",
        "ask_btn": "ਪੁੱਛੋ",
        "footer": "Powered by <strong>Groq LLaMA 3.3</strong> + <strong>Sarvam AI</strong> + <strong>LiveKit</strong> &nbsp;|&nbsp; ਸਹੀ ਜਾਣਕਾਰੀ ਲਈ: <strong>india.gov.in</strong>",
        "welcome": "🙏 ਸਤ ਸ੍ਰੀ ਅਕਾਲ! ਮੈਂ ਤੁਹਾਡਾ ਸਰਕਾਰ ਸਹਾਇਕ ਹਾਂ। ਸਰਕਾਰੀ ਯੋਜਨਾਵਾਂ ਬਾਰੇ ਜਾਣਕਾਰੀ ਦੇਣ ਲਈ ਇੱਥੇ ਹਾਂ। ਤੁਸੀਂ ਕਿਸ ਯੋਜਨਾ ਬਾਰੇ ਜਾਣਨਾ ਚਾਹੁੰਦੇ ਹੋ?",
        "quick_questions": [
            "ਕਿਸਾਨ ਹਾਂ, ਮੈਨੂੰ ਕੀ ਮਿਲੇਗਾ?",
            "ਮੁਫ਼ਤ ਹਸਪਤਾਲ ਇਲਾਜ?",
            "ਧੀ ਲਈ ਕੋਈ ਯੋਜਨਾ?",
            "ਘਰ ਬਣਾਉਣ ਦੀ ਯੋਜਨਾ?",
            "ਰੁਜ਼ਗਾਰ ਗਾਰੰਟੀ ਕੀ ਹੈ?",
            "ਛੋਟੇ ਕਾਰੋਬਾਰ ਲਈ ਕਰਜ਼ਾ?",
        ],
    },
    "unknown": {
        "badge": "🇮🇳 Digital India Initiative",
        "title": "Sarkar Sahayak — सरकार सहायक",
        "subtitle": "Sarkari yojanaon ki jaankari ab aapki bhasha mein • Voice + Text Support",
        "chat_title": "💬 Chat with Agent",
        "schemes_title": "📋 Popular Government Schemes",
        "voice_title": "Voice Support Available",
        "voice_desc": "Voice ke liye agent terminal mein run karein:",
        "voice_then": "Phir jao:",
        "placeholder": "Yojana ke baare mein puchein...",
        "send_btn": "Send →",
        "clear_btn": "🗑️ Clear Chat",
        "lang_label": "🌐 Language / भाषा",
        "quick_q_label": "⚡ Quick Questions",
        "status_groq_ok": "Groq LLM ✓",
        "status_groq_miss": "GROQ_API_KEY missing",
        "status_lk_ok": "LiveKit Configured ✓",
        "status_lk_miss": "LiveKit not configured",
        "ask_btn": "Ask",
        "footer": "Powered by <strong>Groq LLaMA 3.3</strong> + <strong>Sarvam AI</strong> + <strong>LiveKit</strong> &nbsp;|&nbsp; Accurate info ke liye: <strong>india.gov.in</strong>",
        "welcome": "🙏 Namaste! Main aapka Sarkar Sahayak hoon. Sarkari yojanaon ke baare mein jaankari dene ke liye yahan hoon.",
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

# ---------- Scheme descriptions by language ----------
def get_schemes(lang):
    names = ["PM Kisan Samman Nidhi", "Ayushman Bharat", "PM Awas Yojana",
             "Sukanya Samriddhi", "PM Ujjwala Yojana", "MGNREGA",
             "PM Jan Dhan Yojana", "PM Mudra Yojana"]
    icons = ["🌾", "🏥", "🏠", "👧", "🔥", "💼", "🏦", "📈"]
    all_tags = {
        "hi-IN":  ["किसान", "स्वास्थ्य", "आवास", "बेटी", "ऊर्जा", "रोजगार", "वित्त", "व्यवसाय"],
        "en-IN":  ["Farmers", "Health", "Housing", "Girl Child", "Energy", "Employment", "Finance", "Business"],
        "ta-IN":  ["விவசாயி", "சுகாதாரம்", "வீட்டுவசதி", "பெண் குழந்தை", "ஆற்றல்", "வேலைவாய்ப்பு", "நிதி", "வணிகம்"],
        "te-IN":  ["రైతు", "ఆరోగ్యం", "గృహం", "ఆడపిల్ల", "శక్తి", "ఉపాధి", "ఆర్థికం", "వ్యాపారం"],
        "bn-IN":  ["কৃষক", "স্বাস্থ্য", "আবাসন", "কন্যাশিশু", "শক্তি", "কর্মসংস্থান", "অর্থ", "ব্যবসা"],
        "gu-IN":  ["ખેડૂત", "આरोগ્ય", "આवास", "દીકરી", "ઉर्जा", "રोजगार", "वित्त", "व्यवसाय"],
        "kn-IN":  ["ರೈತ", "ಆರೋಗ್ಯ", "ಮನೆ", "ಹೆಣ್ಣು ಮಗು", "ಶಕ್ತಿ", "ಉದ್ಯೋಗ", "ಹಣಕಾಸು", "ವ್ಯಾಪಾರ"],
        "mr-IN":  ["शेतकरी", "आरोग्य", "घरकुल", "मुलगी", "ऊर्जा", "रोजगार", "वित्त", "व्यवसाय"],
        "pa-IN":  ["ਕਿਸਾਨ", "ਸਿਹਤ", "ਘਰ", "ਧੀ", "ਊਰਜਾ", "ਰੁਜ਼ਗਾਰ", "ਵਿੱਤ", "ਕਾਰੋਬਾਰ"],
        "unknown":["Kisan", "Health", "Awas", "Beti", "Urja", "Rozgar", "Finance", "Vyapar"],
    }
    tags = all_tags.get(lang, all_tags["hi-IN"])
    queries = [
        "PM Kisan Samman Nidhi yojana ke baare mein batao aur kaise milega?",
        "Ayushman Bharat card kaise banwayein aur kya documents chahiye?",
        "PM Awas Yojana ke liye apply kaise karein?",
        "Sukanya Samriddhi Yojana ke baare mein batao aur account kaise kholein?",
        "Ujjwala Yojana ka free gas connection kaise milega?",
        "MGNREGA job card kaise banwayein aur kya eligibility hai?",
        "Jan Dhan account kaise kholein aur kya fayde hain?",
        "Mudra loan ke liye apply kaise karein aur kya eligibility hai?",
    ]
    descs = {
        "hi-IN": ["किसान परिवारों को ₹6000/वर्ष", "₹5 लाख तक मुफ़्त स्वास्थ्य बीमा", "गरीब परिवारों को पक्का घर", "बेटी के लिए बचत योजना", "BPL परिवारों को मुफ्त LPG", "100 दिन रोजगार गारंटी", "जीरो बैलेंस बैंक खाता + बीमा", "छोटे व्यवसाय के लिए ₹10 लाख लोन"],
        "en-IN": ["₹6000/year for farmer families", "Free health insurance up to ₹5 lakh", "Pucca house for BPL families", "Savings scheme for girl child", "Free LPG for BPL families", "100 days employment guarantee", "Zero balance account + insurance", "Business loans up to ₹10 lakh"],
        "ta-IN": ["விவசாயிகளுக்கு ₹6000/ஆண்டு", "₹5 லட்சம் வரை இலவச காப்பீடு", "ஏழைகளுக்கு வீடு", "பெண் குழந்தைக்கு சேமிப்பு", "BPL க்கு இலவச LPG", "100 நாள் வேலை உத்தரவாதம்", "ஜீரோ பேலன்ஸ் கணக்கு", "₹10 லட்சம் வணிக கடன்"],
        "te-IN": ["రైతులకు ₹6000/సంవత్సరం", "₹5 లక్షల ఉచిత భీమా", "BPL కుటుంబాలకు ఇల్లు", "ఆడపిల్లకు పొదుపు", "BPL కు ఉచిత LPG", "100 రోజుల ఉపాధి హామీ", "జీరో బ్యాలెన్స్ ఖాతా", "₹10 లక్షల వ్యాపార రుణం"],
        "bn-IN": ["কৃষকদের ₹6000/বছর", "₹5 লাখ বিনামূল্যে বীমা", "BPL পরিবারের বাড়ি", "মেয়ের জন্য সঞ্চয়", "BPL কে LPG", "১০০ দিনের কর্মসংস্থান", "জিরো ব্যালেন্স অ্যাকাউন্ট", "₹10 লাখ ব্যবসায়িক ঋণ"],
        "gu-IN": ["ખેડૂત ₹6000/વર્ષ", "₹5 લાખ મફત વીમો", "BPL ને ઘર", "દીકરી માટે બચત", "BPL ને LPG", "100 દિવસ રોજગારી", "ઝીરો બેલેન્સ ખાતું", "₹10 લાખ ધંધા લોન"],
        "kn-IN": ["ರೈತರಿಗೆ ₹6000/ವರ್ಷ", "₹5 ಲಕ್ಷ ಉಚಿತ ವಿಮೆ", "BPL ಕುಟುಂಬಗಳಿಗೆ ಮನೆ", "ಹೆಣ್ಣು ಮಗುವಿಗೆ ಉಳಿತಾಯ", "BPL ಗೆ ಉಚಿತ LPG", "100 ದಿನ ಉದ್ಯೋಗ", "ಶೂನ್ಯ ಬ್ಯಾಲೆನ್ಸ್ ಖಾತೆ", "₹10 ಲಕ್ಷ ವ್ಯಾಪಾರ ಸಾಲ"],
        "mr-IN": ["शेतकऱ्यांना ₹6000/वर्ष", "₹5 लाख मोफत विमा", "BPL ला घर", "मुलीसाठी बचत", "BPL ला LPG", "100 दिवस रोजगार", "शून्य शिल्लक खाते", "₹10 लाखांपर्यंत कर्ज"],
        "pa-IN": ["ਕਿਸਾਨਾਂ ਨੂੰ ₹6000/ਸਾਲ", "₹5 ਲੱਖ ਮੁਫ਼ਤ ਬੀਮਾ", "BPL ਨੂੰ ਘਰ", "ਧੀ ਲਈ ਬੱਚਤ", "BPL ਨੂੰ LPG", "100 ਦਿਨ ਰੁਜ਼ਗਾਰ", "ਜ਼ੀਰੋ ਬੈਲੇਂਸ ਖਾਤਾ", "₹10 ਲੱਖ ਕਾਰੋਬਾਰ ਕਰਜ਼ਾ"],
        "unknown": ["Kisan parivaaron ko ₹6000/year", "₹5 lakh tak free health insurance", "Garib parivaaron ko pucca ghar", "Beti ke liye savings scheme", "BPL parivaaron ko free LPG", "100 din ka rozgar guarantee", "Zero balance bank account", "Small business ke liye ₹10 lakh loan"],
    }
    d = descs.get(lang, descs["hi-IN"])
    return [{"icon": icons[i], "name": names[i], "desc": d[i], "tag": tags[i], "query": queries[i]} for i in range(len(names))]


LANGUAGES = {
    "Hindi (हिंदी)": "hi-IN",
    "English": "en-IN",
    "Tamil (தமிழ்)": "ta-IN",
    "Telugu (తెలుగు)": "te-IN",
    "Bengali (বাংলা)": "bn-IN",
    "Gujarati (ગુજરાતી)": "gu-IN",
    "Kannada (ಕನ್ನಡ)": "kn-IN",
    "Marathi (मराठी)": "mr-IN",
    "Punjabi (ਪੰਜਾਬੀ)": "pa-IN",
    "Auto Detect": "unknown",
}

# ---------- Session State ----------
if "selected_language" not in st.session_state:
    st.session_state.selected_language = "hi-IN"
if "prev_language" not in st.session_state:
    st.session_state.prev_language = "hi-IN"

lang = st.session_state.selected_language

# Detect language change → reset chat with new welcome message
if lang != st.session_state.prev_language:
    t = UI_TEXT.get(lang, UI_TEXT["hi-IN"])
    st.session_state.messages = [{"role": "agent", "content": t["welcome"], "time": "Now"}]
    st.session_state.prev_language = lang

if "messages" not in st.session_state:
    t = UI_TEXT.get(lang, UI_TEXT["hi-IN"])
    st.session_state.messages = [{"role": "agent", "content": t["welcome"], "time": "Now"}]

T = UI_TEXT.get(lang, UI_TEXT["hi-IN"])

# ---------- CSS ----------
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Tiro+Devanagari+Hindi&family=DM+Sans:wght@300;400;500;600;700&display=swap');
:root {
    --saffron: #FF6B1A; --deep-green: #0A6E3F; --white: #FAFAF8;
    --navy: #0D1B2A; --light-bg: #F4F1EB; --card-bg: #FFFFFF;
    --border: #E8E2D6; --text-primary: #1A1A1A; --text-muted: #6B6B6B;
}
html, body, [class*="css"] { font-family: 'DM Sans', sans-serif; background-color: var(--light-bg); }
#MainMenu, footer, header { visibility: hidden; }
.stDeployButton { display: none; }
.main .block-container { padding: 1.5rem 2rem; max-width: 1400px; }

.hero-header {
    background: linear-gradient(135deg, var(--navy) 0%, #1a3a5c 50%, var(--deep-green) 100%);
    border-radius: 20px; padding: 2rem 2.5rem; margin-bottom: 1.5rem;
    position: relative; overflow: hidden;
}
.hero-header::before { content: "🇮🇳"; position: absolute; right: 2rem; top: 50%; transform: translateY(-50%); font-size: 5rem; opacity: 0.12; }
.hero-header::after { content: ""; position: absolute; top: 0; left: 0; right: 0; height: 4px; background: linear-gradient(90deg, var(--saffron), var(--white), var(--deep-green)); }
.hero-title { color: white; font-size: 2rem; font-weight: 700; margin: 0; letter-spacing: -0.5px; }
.hero-subtitle { color: rgba(255,255,255,0.75); font-size: 1rem; margin-top: 0.4rem; font-weight: 300; }
.hero-badge { display: inline-block; background: rgba(255,107,26,0.2); border: 1px solid var(--saffron); color: #FFB347; font-size: 0.7rem; padding: 3px 10px; border-radius: 20px; margin-bottom: 0.8rem; letter-spacing: 1px; text-transform: uppercase; font-weight: 600; }

.scheme-card { background: var(--card-bg); border: 1px solid var(--border); border-radius: 14px; padding: 1.2rem; margin-bottom: 0.8rem; position: relative; overflow: hidden; }
.scheme-card::before { content: ""; position: absolute; left: 0; top: 0; bottom: 0; width: 3px; background: var(--saffron); border-radius: 3px 0 0 3px; }
.scheme-icon { font-size: 1.8rem; margin-bottom: 0.4rem; }
.scheme-name { font-weight: 600; font-size: 0.9rem; color: var(--text-primary); margin-bottom: 0.2rem; }
.scheme-desc { font-size: 0.75rem; color: var(--text-muted); line-height: 1.4; }
.scheme-tag { display: inline-block; background: #FFF3E8; color: var(--saffron); font-size: 0.65rem; padding: 2px 8px; border-radius: 10px; margin-top: 0.4rem; font-weight: 600; }

.chat-container { background: var(--card-bg); border: 1px solid var(--border); border-radius: 16px; height: 420px; overflow-y: auto; padding: 1.2rem; margin-bottom: 1rem; }
.chat-container::-webkit-scrollbar { width: 4px; }
.chat-container::-webkit-scrollbar-thumb { background: var(--border); border-radius: 2px; }
.msg-user { display: flex; justify-content: flex-end; margin-bottom: 0.8rem; }
.msg-agent { display: flex; justify-content: flex-start; margin-bottom: 0.8rem; align-items: flex-start; gap: 0.5rem; }
.bubble-user { background: linear-gradient(135deg, var(--saffron), #FF8C42); color: white; padding: 0.7rem 1rem; border-radius: 18px 18px 4px 18px; max-width: 75%; font-size: 0.88rem; line-height: 1.5; box-shadow: 0 2px 8px rgba(255,107,26,0.25); }
.bubble-agent { background: var(--light-bg); color: var(--text-primary); padding: 0.7rem 1rem; border-radius: 18px 18px 18px 4px; max-width: 75%; font-size: 0.88rem; line-height: 1.5; border: 1px solid var(--border); }
.agent-avatar { width: 32px; height: 32px; background: linear-gradient(135deg, var(--deep-green), #0ea05c); border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 0.9rem; flex-shrink: 0; }
.msg-time { font-size: 0.65rem; color: var(--text-muted); margin-top: 3px; text-align: right; }

.mic-section { background: var(--card-bg); border: 1px solid var(--border); border-radius: 16px; padding: 1.2rem; text-align: center; margin-bottom: 1rem; }

.stButton > button { background: linear-gradient(135deg, var(--saffron), #FF8C42) !important; color: white !important; border: none !important; border-radius: 12px !important; font-weight: 600 !important; font-size: 0.85rem !important; transition: all 0.2s !important; }
.stButton > button:hover { box-shadow: 0 4px 15px rgba(255,107,26,0.4) !important; transform: translateY(-1px) !important; }

section[data-testid="stSidebar"] { background: var(--navy) !important; }
section[data-testid="stSidebar"] * { color: rgba(255,255,255,0.85) !important; }

/* ===== DARK INPUT BOX FIX ===== */
.stTextInput > div > div > input,
div[data-baseweb="input"] input,
div[data-baseweb="base-input"] input,
[data-testid="stTextInput"] input {
    background-color: #1A1A2E !important;
    color: #FFFFFF !important;
    border: 1.5px solid #3a3a5c !important;
    border-radius: 12px !important;
    font-size: 0.9rem !important;
    caret-color: #FF6B1A !important;
}
.stTextInput > div > div > input:focus,
div[data-baseweb="input"] input:focus {
    border-color: #FF6B1A !important;
    box-shadow: 0 0 0 2px rgba(255,107,26,0.3) !important;
    outline: none !important;
}
.stTextInput > div > div > input::placeholder,
div[data-baseweb="input"] input::placeholder {
    color: #7a7a9a !important;
    opacity: 1 !important;
}
/* Form wrapper dark */
div[data-testid="stForm"] {
    background: #12121F !important;
    border: 1px solid #2a2a40 !important;
    border-radius: 14px !important;
    padding: 0.6rem !important;
}

.section-title { font-size: 0.75rem; font-weight: 700; color: var(--text-muted); text-transform: uppercase; letter-spacing: 1.5px; margin-bottom: 0.8rem; padding-bottom: 0.4rem; border-bottom: 1px solid var(--border); }
</style>
""", unsafe_allow_html=True)


# ---------- AI Response ----------
def get_ai_response(user_msg, language):
    try:
        from groq import Groq
        client = Groq(api_key=os.getenv("GROQ_API_KEY"))
        lang_names = {v: k for k, v in LANGUAGES.items()}
        lang_name = lang_names.get(language, "Hindi")
        system_prompt = f"""You are Sarkar Sahayak, a helpful government scheme awareness assistant for Indian citizens.
Respond in {lang_name} language. If auto-detect, use Hindi.
Keep responses concise (3-5 sentences), friendly and easy to understand.
Key schemes: PM Kisan (₹6000/year), Ayushman Bharat (₹5 lakh health), PM Awas (housing), Sukanya Samriddhi (girl child), Ujjwala (LPG), MGNREGA (100 day job), Jan Dhan (bank account), Mudra (business loan), Atal Pension, Skill India.
Always end with a friendly closing in the response language."""
        messages = [{"role": "system", "content": system_prompt}]
        for msg in st.session_state.messages[-6:]:
            role = "user" if msg["role"] == "user" else "assistant"
            messages.append({"role": role, "content": msg["content"]})
        messages.append({"role": "user", "content": user_msg})
        response = client.chat.completions.create(model="llama-3.3-70b-versatile", messages=messages, max_tokens=350, temperature=0.7)
        return response.choices[0].message.content
    except Exception as e:
        return f"Maafi chahta hoon, abhi response nahi de pa raha. Error: {str(e)[:100]}"


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
    <div style="padding:1rem 0 0.5rem;">
        <div style="font-size:1.5rem;font-weight:800;color:white;">🇮🇳 Sarkar Sahayak</div>
        <div style="font-size:0.75rem;color:rgba(255,255,255,0.4);margin-top:4px;">Government Scheme Assistant</div>
    </div>
    <hr style="border-color:rgba(255,255,255,0.1);margin:0.8rem 0;"/>
    """, unsafe_allow_html=True)

    st.markdown(f'<div style="font-size:0.7rem;color:rgba(255,255,255,0.4);text-transform:uppercase;letter-spacing:1.5px;margin-bottom:6px;">{T["lang_label"]}</div>', unsafe_allow_html=True)
    selected_lang_name = st.selectbox("Language", list(LANGUAGES.keys()), index=0, label_visibility="collapsed")
    new_lang = LANGUAGES[selected_lang_name]
    if new_lang != st.session_state.selected_language:
        st.session_state.selected_language = new_lang
        st.rerun()

    st.markdown('<hr style="border-color:rgba(255,255,255,0.1);margin:0.8rem 0;"/>', unsafe_allow_html=True)
    st.markdown(f'<div style="font-size:0.7rem;color:rgba(255,255,255,0.4);text-transform:uppercase;letter-spacing:1.5px;margin-bottom:8px;">{T["quick_q_label"]}</div>', unsafe_allow_html=True)

    for q in T["quick_questions"]:
        if st.button(f"→ {q}", key=f"qs_{q}", use_container_width=True):
            send_message(q)
            st.rerun()

    st.markdown('<hr style="border-color:rgba(255,255,255,0.1);margin:0.8rem 0;"/>', unsafe_allow_html=True)
    groq_key = os.getenv("GROQ_API_KEY", "")
    lk_url = os.getenv("LIVEKIT_URL", "")
    dot_ok = "width:8px;height:8px;background:#2ecc71;border-radius:50%;display:inline-block;box-shadow:0 0 5px #2ecc71;"
    dot_err = "width:8px;height:8px;background:#e74c3c;border-radius:50%;display:inline-block;"
    dot_warn = "width:8px;height:8px;background:#f39c12;border-radius:50%;display:inline-block;"
    st.markdown(f'<div style="display:flex;align-items:center;gap:8px;font-size:0.78rem;"><span style="{dot_ok if groq_key else dot_err}"></span>{T["status_groq_ok"] if groq_key else T["status_groq_miss"]}</div>', unsafe_allow_html=True)
    st.markdown(f'<div style="display:flex;align-items:center;gap:8px;font-size:0.78rem;margin-top:4px;"><span style="{dot_ok if lk_url else dot_warn}"></span>{T["status_lk_ok"] if lk_url else T["status_lk_miss"]}</div>', unsafe_allow_html=True)

    st.markdown('<hr style="border-color:rgba(255,255,255,0.1);margin:0.8rem 0;"/>', unsafe_allow_html=True)
    if st.button(T["clear_btn"], use_container_width=True):
        st.session_state.messages = [{"role": "agent", "content": T["welcome"], "time": "Now"}]
        st.rerun()

# =================== MAIN CONTENT ===================
st.markdown(f"""
<div class="hero-header">
    <div class="hero-badge">{T["badge"]}</div>
    <div class="hero-title">{T["title"]}</div>
    <div class="hero-subtitle">{T["subtitle"]}</div>
</div>
""", unsafe_allow_html=True)

col_chat, col_schemes = st.columns([3, 2], gap="large")

with col_chat:
    st.markdown(f'<div class="section-title">{T["chat_title"]}</div>', unsafe_allow_html=True)
    st.markdown(f"""
    <div class="mic-section">
        <div style="font-size:1.8rem;">🎙️</div>
        <div style="font-weight:600;font-size:0.85rem;color:#1A1A1A;margin:4px 0;">{T["voice_title"]}</div>
        <div style="font-size:0.78rem;color:#6B6B6B;">
            {T["voice_desc"]}<br>
            <code style="background:#F4F1EB;padding:2px 8px;border-radius:6px;display:inline-block;margin:4px 0;">python scheme_awareness_agent.py dev</code><br>
            {T["voice_then"]} <a href="https://agents-playground.livekit.io" target="_blank" style="color:#0A6E3F;font-weight:600;">agents-playground.livekit.io</a>
        </div>
    </div>
    """, unsafe_allow_html=True)

    chat_html = '<div class="chat-container">'
    for msg in st.session_state.messages:
        if msg["role"] == "user":
            chat_html += f'<div class="msg-user"><div><div class="bubble-user">{msg["content"]}</div><div class="msg-time">{msg.get("time","")}</div></div></div>'
        else:
            chat_html += f'<div class="msg-agent"><div class="agent-avatar">🤖</div><div><div class="bubble-agent">{msg["content"]}</div><div class="msg-time">{msg.get("time","")}</div></div></div>'
    chat_html += '</div>'
    st.markdown(chat_html, unsafe_allow_html=True)

    with st.form("chat_form", clear_on_submit=True):
        c1, c2 = st.columns([5, 1])
        with c1:
            user_input = st.text_input("msg", placeholder=T["placeholder"], label_visibility="collapsed")
        with c2:
            submitted = st.form_submit_button(T["send_btn"])
        if submitted and user_input:
            send_message(user_input)
            st.rerun()

with col_schemes:
    st.markdown(f'<div class="section-title">{T["schemes_title"]}</div>', unsafe_allow_html=True)
    schemes = get_schemes(lang)
    for scheme in schemes:
        c1, c2 = st.columns([4, 1])
        with c1:
            st.markdown(f"""
            <div class="scheme-card">
                <div class="scheme-icon">{scheme["icon"]}</div>
                <div class="scheme-name">{scheme["name"]}</div>
                <div class="scheme-desc">{scheme["desc"]}</div>
                <span class="scheme-tag">{scheme["tag"]}</span>
            </div>""", unsafe_allow_html=True)
        with c2:
            st.write("")
            if st.button(T["ask_btn"], key=f"sc_{scheme['name']}", use_container_width=True):
                send_message(scheme["query"])
                st.rerun()

st.markdown(f"""
<div style="text-align:center;padding:1.5rem 0 0.5rem;color:#9B9B9B;font-size:0.72rem;border-top:1px solid #E8E2D6;margin-top:1rem;">
    {T["footer"]}
</div>
""", unsafe_allow_html=True)
