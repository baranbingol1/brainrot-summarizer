from utils import load_env
import os

from elevenlabs.client import ElevenLabs
from elevenlabs import save

load_env()

client = ElevenLabs(api_key=os.getenv("ELEVENLABS_API_KEY"))

def create_audio(text: str, voice: str, file_path: str):
    audio = client.generate(text=text, voice=voice)
    save(audio, file_path)

if __name__ == "__main__": # for testing api
    create_audio("Hello, world!", "Brian", "hello_world.mp3")