import logging
from dotenv import load_dotenv
from livekit.agents import JobContext, WorkerOptions, cli
from livekit.agents.voice import Agent, AgentSession
from livekit.plugins import groq, sarvam, silero

load_dotenv()

logger = logging.getLogger("scheme-awareness-agent")
logger.setLevel(logging.INFO)


class GovernmentSchemeAgent(Agent):
    def __init__(self) -> None:
        super().__init__(
            instructions="""
            You are a helpful government scheme awareness assistant for Indian citizens.

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

            CRITICAL RULES - MUST FOLLOW:
            - NEVER use Hindi/Devanagari Unicode script like (नमस्ते, योजना, आवास)
            - ALWAYS write Hindi words using English/Roman letters only
            - Good: "Namaste, PM Kisan yojana mein aapko 6000 rupaye milenge"
            - Bad: "नमस्ते, पीएम किसान योजना में आपको 6000 रुपये मिलेंगे"
            - Keep all responses under 3 sentences - this is a voice agent
            - Speak naturally, no bullet points or lists
            - Mix Hindi and English naturally (Hinglish is fine)

            Opening message: "Namaste! Main aapka Sarkar Sahayak hoon. Aap kaunsi sarkari yojana ke baare mein jaanna chahte hain?"
            """,

            # STT - Hindi fixed (not unknown) for stable connection
            stt=sarvam.STT(
                language="hi-IN",
                model="saaras:v3",
                mode="transcribe"
            ),

            # Groq LLM
            llm=groq.LLM(
                model="openai/gpt-oss-120b"
            ),

            # TTS - Sarvam Bulbul
            tts=sarvam.TTS(
                target_language_code="hi-IN",
                model="bulbul:v3",
                speaker="simran"
            ),

            # VAD for voice detection
            vad=silero.VAD.load(),
        )

    async def on_enter(self):
        await self.session.generate_reply()


async def entrypoint(ctx: JobContext):
    logger.info(f"User connected: {ctx.room.name}")
    session = AgentSession()
    await session.start(
        agent=GovernmentSchemeAgent(),
        room=ctx.room
    )


if __name__ == "__main__":
    cli.run_app(WorkerOptions(entrypoint_fnc=entrypoint))