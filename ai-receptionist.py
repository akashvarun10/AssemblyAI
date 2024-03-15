import assemblyai as aai
from elevenlabs import generate,stream
from openai import OpenAI
import os 
from dotenv import load_dotenv
load_dotenv()

assemblyai_api_key = os.getenv("ASSEMBLYAI_API_KEY")    
openai_api_key = os.getenv("OPENAI_API_KEY")
elevenlabs_api_key = os.getenv("ELEVENLABS_API_KEY")
class AI_Assistant:
    def __init__(self):
        aai.settings.api_key = assemblyai_api_key
        self.openai_client = OpenAI(api_key = openai_api_key)
        self.elevenlabs_api_key = elevenlabs_api_key

        self.transcriber = None
        # Prompt
        self.full_transcript = [
        { "role":"system","content": "You are a receptionist at a dental clinic. Be resourceful and efficient."}
        ]
        

 