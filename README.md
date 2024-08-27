# Speech to Text Converter

This is a simple web application that allows users to upload an audio file (in `.wav` or `.mp3` format) and converts the speech in the audio to text using Google's Speech Recognition API. The application is built using Streamlit and utilizes a custom pipeline to handle the conversion process.

## Features

- Supports `.wav` and `.mp3` files**: If the uploaded file is in `.mp3` format, it is automatically converted to `.wav` before processing.
- Speech Recognition: Uses the `speech_recognition` library to convert speech in audio files to text.
- Custom Pipeline: The application uses a custom pipeline to handle the steps of converting audio and transcribing it.

## Prerequisites

Before running the application, you need to have the following installed:

- Python 3.x
- `pip` (Python package installer)
- `ffmpeg` (required by `pydub` for audio conversion)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/speech-to-text-converter.git
   cd speech-to-text-converter
