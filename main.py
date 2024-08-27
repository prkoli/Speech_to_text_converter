import streamlit as st
import speech_recognition as sr
from pydub import AudioSegment

# Step 1: Convert audio to wav format
def convert_audio_to_wav(audio_file):
    audio = AudioSegment.from_file(audio_file)
    wav_file = audio_file.name.split(".")[0] + ".wav"
    audio.export(wav_file, format="wav")
    return wav_file

# Step 2: Convert wav file to text
def speech_to_text(wav_file):
    recognizer = sr.Recognizer()
    with sr.AudioFile(wav_file) as source:
        audio = recognizer.record(source)
        try:
            text = recognizer.recognize_google(audio)
            return text
        except sr.UnknownValueError:
            return "Could not understand audio"
        except sr.RequestError as e:
            return f"Error: {str(e)}"

# Pipeline class to handle the steps
class SpeechToTextPipeline:
    def __init__(self):
        self.steps = []

    def add_step(self, function):
        self.steps.append(function)

    def execute(self, audio_file):
        for step in self.steps:
            audio_file = step(audio_file)  # Pass the output of one step as the input to the next
        return audio_file

def main():
    st.title("Speech to Text Converter")
    st.write("Upload an audio file and convert it to text.")

    uploaded_file = st.file_uploader("Choose an audio file", type=["wav", "mp3"])

    if uploaded_file is not None:
        file_details = {"Filename": uploaded_file.name, "FileType": uploaded_file.type}
        st.write(file_details)

        # Initialize the pipeline
        pipeline = SpeechToTextPipeline()

        # Add the necessary steps to the pipeline
        if uploaded_file.type == "audio/mp3":
            pipeline.add_step(convert_audio_to_wav)
        
        pipeline.add_step(speech_to_text)

        # Execute the pipeline
        text = pipeline.execute(uploaded_file)

        st.write("Converted Text:")
        st.write(text)

if __name__ == "__main__":
    main()
