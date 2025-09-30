import speech_recognition as sr
import pyttsx3
import webbrowser
from datetime import datetime

recognizer = sr.Recognizer()
recognizer.pause_threshold = 1.0  # helps if you speak slowly
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def main():
    with sr.Microphone() as source:
        print("Listening... Speak now!")
        try:
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)
        except sr.WaitTimeoutError:
            print("No speech detected. Please speak clearly!")
            return None

    try:
        command = recognizer.recognize_google(audio)
        print("You said: " + command)
        return command.lower()

    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
        return None
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")
        return None

if __name__ == "__main__":
    # Adjust for ambient noise once at the start
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source, duration=1)

    print("Voice Assistant Started. Say 'exit' to stop.")
    while True:
        command = main()
        if command:
            if "hello" in command:
                speak("Hello! How can I help you?")
            elif "what is your name" in command:
                speak("I am a voice assistant built with Python.")
            elif "open google" in command:
                webbrowser.open("https://www.google.com")
                current_time = datetime.now().strftime("%H:%M:%S")
                print("Current time is:", current_time)
                speak("The current time is " + current_time)
            elif "exit" in command:
                speak("Goodbye!")
                break
            else:
                speak("Sorry, I didn't understand that command.")
