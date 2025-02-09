import speech_recognition as sr
from flask import Flask, jsonify
from enum import Enum

# Enum to specify the language
class Language(Enum):
    ENGLISH = "en-US"

class SpeechToText:
    
    @staticmethod
    def print_mic_device_index():
        # Display all available microphones and their indices
        for index, name in enumerate(sr.Microphone.list_microphone_names()):
            print("{1}, device_index={0}".format(index, name))

    @staticmethod
    def speech_to_text(device_index, language=Language.ENGLISH):
        # Initialize recognizer
        recognizer = sr.Recognizer()

        # Use the microphone as the audio source
        with sr.Microphone(device_index=device_index) as source:
            print("Please say something...")

            # Recognize speech using Google Speech Recognition
            try:
                # Listen to the microphone and recognize speech
                audio = recognizer.listen(source, timeout=15, phrase_time_limit=20)
                text = recognizer.recognize_google(audio, language=language.value)
                print("You said: {}".format(text))  # If recognition is successful
                return text
            except sr.UnknownValueError:
                print("Google Speech Recognition could not understand the audio")
                return None
            except sr.RequestError as e:
                print(f"Could not request results; {e}")
                return None
            except TimeoutError:
                print("Listening timed out while waiting for phrase to start")
                return None
            except KeyboardInterrupt:
                print("Program interrupted by user.")
                return None

    @staticmethod
    def check_mic_device_index():
        # Check the available microphones
        SpeechToText.print_mic_device_index()

    @staticmethod
    def run_speech_to_text_english(device_index):
        # Run speech-to-text for English language using the given device index
        return SpeechToText.speech_to_text(device_index)

# Flask setup
app = Flask(__name__)

@app.route('/speech-to-text', methods=['GET'])
def speech_to_text_api():
    # List available microphones
    available_mics = sr.Microphone.list_microphone_names()
    
    # Check if there are available microphones
    if available_mics:
        device_index = 0  # Default to first available microphone
        print(f"Using microphone: {available_mics[device_index]}")

        try:
            # Run speech-to-text and return the transcription
            transcription = SpeechToText.run_speech_to_text_english(device_index)
            if transcription:
                return jsonify({"transcription": transcription})
            else:
                return jsonify({"error": "Speech not recognized."}), 500
        except Exception as e:
            return jsonify({"error": str(e)}), 500
    else:
        return jsonify({"error": "No microphones found."}), 400

if __name__ == "__main__":
    # Run the Flask app on the local server
    app.run(debug=True)
