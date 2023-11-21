# Voice-Assistant-using-GPT4-model

This project implements an AI-powered voice assistant using Streamlit, OpenAI's GPT-4, and other Python libraries for speech recognition and synthesis.

## Getting Started

To run this voice assistant, follow these steps:

1. Install the required dependencies:

    ```bash
    pip install streamlit openai pyttsx3 SpeechRecognition python-dotenv
    ```

2. Set up your environment variables by creating a `.env` file with the following content:

    ```
    OPENAI_API_KEY=your_openai_api_key
    ```

    Replace `your_openai_api_key` with your actual OpenAI API key.

3. Run the application:

    ```bash
    streamlit run your_script_name.py
    ```

    Replace `your_script_name.py` with the name of the Python script containing the provided code.

## Usage

1. Launch the application, and you will see a Streamlit interface titled "AI Powered Voice Assistant."

2. To interact with the assistant, say "Genius" to start recording your question.

3. After saying "Genius," speak your question into the microphone.

4. The assistant will transcribe your speech into text, generate a response using the GPT-4 model, and read the response aloud.

5. The conversation continues until you stop the application or encounter an error.

## Dependencies

- [Streamlit](https://www.streamlit.io/): For building web applications with simple Python scripts.
- [OpenAI GPT-4](https://beta.openai.com/signup/): Powerful natural language processing model for generating responses.
- [pyttsx3](https://pypi.org/project/pyttsx3/): Text-to-speech conversion library.
- [SpeechRecognition](https://pypi.org/project/SpeechRecognition/): Library for performing speech recognition.
- [python-dotenv](https://pypi.org/project/python-dotenv/): For loading environment variables from a .env file.

## Configuration

Ensure you have set up the necessary environment variable:

- `OPENAI_API_KEY`: Your OpenAI GPT-4 API key.

## Note

- If any errors occur during the execution of the application, they will be displayed in the Streamlit interface.

Feel free to customize and extend the code according to your needs. Happy voice-assisting!
