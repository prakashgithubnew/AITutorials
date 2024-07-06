from openai import OpenAI

client = OpenAI(
     #defaults to os.environ.get("OPENAI_API_KEY")
     api_key="sk-proj-QVQH75tXCtd9u4X55tPjT3BlbkFJANWDKEquWuz7PeN8fHAK",
)
from docx import Document
audio_file_path="C:\\Users\\prakshar\\Downloads\\Recording.wav"


def callAudio(audio_file_path):
    with open(audio_file_path, 'rb') as audio_file:
        transcription = client.audio.transcriptions.create(model="whisper-1", file=audio_file,response_format="text")
    return transcription


print(callAudio(audio_file_path))
