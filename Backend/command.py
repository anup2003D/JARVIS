import time
import pyttsx3
import speech_recognition as sr
import eel


def speak(text):
    text=str(text)
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    # Keep default voice but adjust rate for better clarity
    engine.setProperty('voice', voices[1].id)
    eel.displayMessage(text)
    engine.setProperty('rate', 200)  # Slower rate for better comprehension
    engine.say(text)
    engine.runAndWait()
    eel.receiverText(text)


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
def takeAllCommands(message=None):
    query = None
    
    if message is None:
        # Voice input path
        query = takeCommand()
        if not query:
            return
        print(query)
        eel.senderText(query)
    else:
        # Text input path
        query = message  # Use the message directly
        print(f"Message received: {query}")
        eel.senderText(query)
    
    try:
        # Remove this line - it's overwriting the text input with voice input
        # query = takeCommand()  
        print(query)
        if query:
            if "open" in query:
                from Backend.feature import openCommand # type: ignore
                openCommand(query)
                
            elif "send message" in query or "call" in query or "video call" in query:
                print("Hellooo")
                
                from Backend.feature import findContact, whatsapp 
                flag=""
                phone, name = findContact(query)
                if (phone != 0):
                    if "send message" in query:
                        flag='message'
                        speak("what message to send")
                        query=takeCommand()
                        
                    elif "call" in query:
                        flag='call'
                    else:
                        flag='video call'
    
                    whatsapp(phone, query, flag, name)
                        
            elif "Youtube" :
                from Backend.feature import PlayYoutube # type: ignore
                PlayYoutube(query)
    
            else:
                from Backend.feature import chatBot
                chatBot(query)
        else:
            print("I did not understand that command.")
            speak("I did not understand that command.")
        
    except Exception as e:
        print(f"Error: {str(e)}")
        speak("I did not catch that. Please try again.")
        
    eel.ShowHood()