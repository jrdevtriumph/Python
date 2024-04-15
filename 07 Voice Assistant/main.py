import speech_recognition as sr
import pyttsx3
import subprocess
from qa_database import qa_database
from fuzzywuzzy import fuzz

# Function to recognize speech
def recognize_speech():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        query = recognizer.recognize_google(audio)
        print("You said:", query)
        return query.lower()
    except sr.UnknownValueError:
        print("Sorry, I didn't get that.")
        return ""
    except sr.RequestError:
        print("Sorry, I couldn't request results. Check your internet connection.")
        return ""

# Function to respond
def respond(text):
    engine = pyttsx3.init()
    # Set properties for female voice
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)  # Female voice index may vary, you can check available voices
    engine.say(text)
    engine.runAndWait()

# Function to find the closest matching question
def find_matching_question(query):
    best_match = None
    best_ratio = 0
    for question in qa_database.keys():
        ratio = fuzz.ratio(query, question.lower())
        if ratio > best_ratio:
            best_ratio = ratio
            best_match = question
    return best_match

# Function to open Calculator
def open_calculator():
    subprocess.Popen(["calc.exe"])

# Function to open Notebook (Notepad)
def open_notebook():
    subprocess.Popen(["notepad.exe"])

# Function to open Skype
def open_skype():
    subprocess.Popen(["skype.exe"])

# Main function
def main():
    while True:
        query = recognize_speech()
        if query:
            if query == "exit":
                break
            elif query == "open calculator":
                open_calculator()
                respond("Calculator is now opened.")
            elif query == "open skype":
                open_skype()
                respond("Calculator is now opened.")
            elif query == "open notebook" or query == "open notepad":
                open_notebook()
                respond("Notebook (Notepad) is now opened.")
            else:
                matched_question = find_matching_question(query)
                if matched_question is not None:
                    respond(qa_database[matched_question])
                else:
                    respond("Sorry, I don't have an answer for that.")

if __name__ == "__main__":
    main()
