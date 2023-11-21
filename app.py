import streamlit as st
import openai
import pyttsx3
import speech_recognition as sr
from dotenv import load_dotenv

load_dotenv() # take environment variables from .env.
import os

openai.api_key = os.getenv("OPENAI_API_KEY")


# Initialize text to speech
engine = pyttsx3.init()

def transcribe_audio_to_text(filename):
    recognizer = sr.Recognizer()
    with sr.AudioFile(filename) as source:
        audio = recognizer.record(source)
    try:
        return recognizer.recognize_google(audio)
    except:
        print('Skipping unknown error')

def generate_response(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-4-1106-preview",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ]
    )
    return response["choices"][0]["message"]["content"]

def speak_text(text):
    engine.say(text)
    engine.runAndWait()

def main():
    st.title("AI Powered Voice Assistant")

    while True:
        # Wait for the user to say "Genius"
        st.write("Say 'Genius' to start recording your question...")
        with sr.Microphone() as source:
            recognizer = sr.Recognizer()
            audio = recognizer.listen(source)
            try:
                transcription = recognizer.recognize_google(audio)
                if transcription.lower() == "genius":
                    # Record audio
                    filename = "input.wav"
                    st.write("Say your Question")
                    with sr.Microphone() as source:
                        recognizer = sr.Recognizer()
                        source.pause_threshold = 1
                        audio = recognizer.listen(source, phrase_time_limit=None, timeout=None)
                        with open(filename, "wb") as f:
                            f.write(audio.get_wav_data())

                    # Transcribe audio to text format
                    text = transcribe_audio_to_text(filename)
                    if text:
                        st.write(f"You Said: {text}")

                        # Generate response
                        response = generate_response(text)
                        st.write(f"Bot says: {response}")

                        # Read response using text-to-speech
                        speak_text(response)
            except Exception as e:
                st.write("".format(e))

if __name__ == "__main__":
    main()
