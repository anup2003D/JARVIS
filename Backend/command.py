import time
import pyttsx3
import speech_recognition as sr
import eel


def speak(text):
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    # Keep default voice but adjust rate for better clarity
    engine.setProperty('voice', voices[1].id)
    eel.displayMessage(text)
    engine.setProperty('rate', 200)  # Slower rate for better comprehension
    engine.say(text)
    engine.runAndWait()


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        # Corrected call
        eel.displayMessage("Listening...")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source, timeout=10, phrase_time_limit=8)
        
    try:
        print("Recognizing...")
        # Corrected call
        eel.displayMessage("Recognizing...")
        query = r.recognize_google(audio, language='en-US')
        print(f"User said: {query}\n")
        # Corrected call
        eel.displayMessage(query)
        #time.sleep(3)
        
        
        speak(query)
        eel.ShowHood()
        #return query.lower()
    except Exception as e:
        print("Say that again please...")
        return "None"
    return query.lower()

#speak("Voice assistant is now online.")
#speak("Hello Anup, I am your voice assistant. How can I help you today?")
#takeCommand()

@eel.expose
def takeAllCommands():
    query = takeCommand()
    print(query)
    
    if "open" in query:
        from Backend.feature import openCommand # type: ignore
        openCommand(query)
    elif "Youtube" :
        from Backend.feature import PlayYoutube # type: ignore
        PlayYoutube(query)
    else:
        print("I did not understand that command.")
        speak("I did not understand that command.")
        
    eel.ShowHood()