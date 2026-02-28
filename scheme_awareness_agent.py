import logging
from dotenv import load_dotenv
from livekit.agents import JobContext, WorkerOptions, cli
from livekit.agents.voice import Agent, AgentSession
from livekit.plugins import groq, sarvam, silero

load_dotenv()

logger = logging.getLogger("scheme-awareness-agent")
logger.setLevel(logging.INFO)

# Language code map — STT detected language → TTS language code
LANGUAGE_MAP = {
    "hi":    "hi-IN",   # Hindi
    "hi-IN": "hi-IN",
    "en":    "en-IN",   # English
    "en-IN": "en-IN",
    "ta":    "ta-IN",   # Tamil
    "ta-IN": "ta-IN",
    "te":    "te-IN",   # Telugu
    "te-IN": "te-IN",
    "bn":    "bn-IN",   # Bengali
    "bn-IN": "bn-IN",
    "gu":    "gu-IN",   # Gujarati
    "gu-IN": "gu-IN",
    "kn":    "kn-IN",   # Kannada
    "kn-IN": "kn-IN",
    "ml":    "ml-IN",   # Malayalam
    "ml-IN": "ml-IN",
    "mr":    "mr-IN",   # Marathi
    "mr-IN": "mr-IN",
    "pa":    "pa-IN",   # Punjabi
    "pa-IN": "pa-IN",
    "od":    "od-IN",   # Odia
    "od-IN": "od-IN",
}

DEFAULT_LANGUAGE = "hi-IN"  # fallback if detection fails


def get_tts_for_language(lang_code: str) -> sarvam.TTS:
    """Create a TTS instance for detected language"""
    tts_lang = LANGUAGE_MAP.get(lang_code, DEFAULT_LANGUAGE)
    logger.info(f"Creating TTS for language: {tts_lang} (detected: {lang_code})")
    return sarvam.TTS(
        target_language_code=tts_lang,
        model="bulbul:v3",
        speaker="shubh"
    )


class GovernmentSchemeAgent(Agent):
    def __init__(self) -> None:
        super().__init__(
            instructions="""
            You are Sarkar Sahayak, a helpful government scheme awareness assistant for Indian citizens.

            Your responsibilities:
            - Explain government schemes in simple language
            - Help citizens check eligibility
            - Guide through application process
            - Suggest schemes based on user situation

            Key schemes:
            - PM Kisan Samman Nidhi: Rs 6000 per year for farmers
            - Ayushman Bharat: Rs 5 lakh health insurance
            - PM Awas Yojana: House for poor families
            - Sukanya Samriddhi Yojana: Savings for girl child
            - PM Ujjwala Yojana: Free LPG connection
            - MGNREGA: 100 days job guarantee
            - PM Jan Dhan Yojana: Zero balance bank account
            - Atal Pension Yojana: Monthly pension scheme
            - PM Mudra Yojana: Business loans up to Rs 10 lakh
            - Skill India Mission: Free skill training

            LANGUAGE RULE — MOST IMPORTANT:
            - Detect which language the user is speaking
            - ALWAYS reply in the SAME language the user spoke
            - If user speaks Hindi   → reply in Hindi
            - If user speaks Tamil   → reply in Tamil
            - If user speaks Telugu  → reply in Telugu
            - If user speaks Bengali → reply in Bengali
            - If user speaks English → reply in English
            - NEVER use any Unicode/script characters (no Devanagari, no Tamil script etc.)
            - ALWAYS write ALL words in Roman/English letters only
            - Examples:
              Hindi:   "Namaste! PM Kisan mein aapko 6000 rupaye milte hain."
              Tamil:   "Vanakkam! PM Kisan thittathil 6000 rubai kidaikkum."
              Telugu:  "Namaskaram! PM Kisan lo 6000 rupayalu vasthayi."
              English: "Hello! PM Kisan gives Rs 6000 per year to farmers."

            OTHER RULES:
            - Max 3 sentences per response — this is a voice agent
            - No bullet points, speak naturally
            - Be warm, patient and supportive

            Opening message (in Hindi):
            "Namaste! Main aapka Sarkar Sahayak hoon. Aap Hindi, English, Tamil, Telugu ya kisi bhi Indian language mein baat kar sakte hain!"
            """,

            # STT — "unknown" tells Sarvam to auto-detect language
            stt=sarvam.STT(
                language="unknown",
                model="saaras:v3",
                mode="transcribe"
            ),

            # LLM — Groq LLaMA
            llm=groq.LLM(
                model="openai/gpt-oss-20b"
            ),

            # TTS — Default Hindi, will be swapped dynamically on first speech
            tts=sarvam.TTS(
                target_language_code=DEFAULT_LANGUAGE,
                model="bulbul:v3",
                speaker="shubh"
            ),

            vad=silero.VAD.load(),
        )
        self._current_tts_lang = DEFAULT_LANGUAGE

    async def on_enter(self):
        await self.session.generate_reply()

    async def on_user_turn_completed(self, turn_ctx, new_message):
        """
        Called after every user message.
        Detect language from STT and update TTS dynamically.
        """
        try:
            # Get detected language from STT transcript metadata
            detected_lang = getattr(new_message, "language", None)

            if detected_lang and detected_lang != "unknown":
                tts_lang = LANGUAGE_MAP.get(detected_lang, DEFAULT_LANGUAGE)

                # Only swap TTS if language changed
                if tts_lang != self._current_tts_lang:
                    logger.info(f"Language changed: {self._current_tts_lang} → {tts_lang}")
                    self._current_tts_lang = tts_lang
                    self.session.tts = get_tts_for_language(detected_lang)

        except Exception as e:
            logger.warning(f"Language detection failed, using default: {e}")

        await super().on_user_turn_completed(turn_ctx, new_message)


async def entrypoint(ctx: JobContext):
    logger.info(f"User connected: {ctx.room.name}")
    session = AgentSession()
    await session.start(
        agent=GovernmentSchemeAgent(),
        room=ctx.room
    )


if __name__ == "__main__":
    cli.run_app(WorkerOptions(entrypoint_fnc=entrypoint))
