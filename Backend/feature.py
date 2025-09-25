'''from playsound import playsound
import eel

@eel.expose

def playAssistantSound():
    # Use '..' to go up one directory from 'Backend' to 'Jarvis'
    music_dir = "./Frontend/assets/audio/WOW.mp3"
    playsound(music_dir)
    
def say_what_again():
    music_dir2 = "./Frontend/assets/audio/SayWhatAgain.mp3"
    playsound(music_dir2)'''
    
    
import struct
import subprocess
import time
import webbrowser
import eel
import pvporcupine
import pyaudio
import pyautogui
import pygame
from Backend.config import ASSISSTANT_NAME
import os
from Backend.command import speak
import re
import pywhatkit as kit
import sqlite3

from Backend.helper import extract_yt_term, remove_words
conn = sqlite3.connect("jarvis.db")
cursor = conn.cursor()

pygame.mixer.init()

@eel.expose
def play_assistant_sound():
    sound_file = r"C:\Users\Anup0\Data Science Projects\Data Science\Jarvis\Frontend\assets\audio\WOW.mp3"
    pygame.mixer.music.load(sound_file)
    pygame.mixer.music.play()


def openCommand(query):
    query=query.replace(ASSISSTANT_NAME,"")
    query=query.replace("open","")
    query.lower()
    
    app_name=query.strip()
    
    if app_name!="":
        try:
            cursor.execute('SELECT path FROM sys_command WHERE name IN (?)',(app_name,))
            results = cursor.fetchall()
            

            if len(results)!=0:
                speak("Opening "+query)
                os.startfile(results[0][0]) 
            else:
                speak("Opening "+query)
                os.system('start '+query)

            '''elif len(results)==0:
                cursor.execute('SELECT url FROM web_command WHERE name IN (?)',(app_name,))
                results = cursor.fetchall()
                print(results)

                if len(results)!=0:
                    speak("Opening "+query)
                    webbrowser.open(results[0][0])

                else:
                    speak("Opening "+query)
                    try:
                        os.system('start '+query)
                    except:
                        speak("not found")'''
        except:
            speak("some thing went wrong")


    '''if query!="":
        speak("Opening " + query)
        os.system("start "+(query))
    else:
        speak("Please specify what to open.")'''
        
def PlayYoutube(query):
    search_term=extract_yt_term(query)
    speak("Playing "+search_term+" on Youtube")
    kit.playonyt(search_term)
    
def hotword():
    porcupine=None
    paud=None
    audio_stream=None
    try:
        #pre trained keyowrds
        porcupine=pvporcupine.create(keywords=["jarvis","alexa"])
        paud=pyaudio.PyAudio()
        audio_stream=paud.open(rate=porcupine.sample_rate,channels=1,format=pyaudio.paInt16,input=True,frames_per_buffer=porcupine.frame_length)
        
        #Loop for streaming
        while True:
            keyword=audio_stream.read(porcupine.frame_length)
            keyword=struct.unpack_from("h"*porcupine.frame_length,keyword)
            
            #preprocessing keyword comes from mic
            keyword_index=porcupine.process(keyword)
            
            #checking first keyword detected for not
            if keyword_index>=0:
                print("hotword detected")
                
                #pressing shortcut for win+j
                import pyautogui as autogui
                autogui.keyDown("win")
                autogui.press("j")
                time.sleep(2)
                autogui.keyUp("win")
                
    except:
        if porcupine is not None:
            porcupine.delete()
        if audio_stream is not None:
            audio_stream.close()
        if paud is not None:
            paud.terminate()
            
            
def findContact(query):
    words_to_remove = [ASSISSTANT_NAME, 'make', 'a', 'to', 'phone', 'call', 'send', 'message', 'whatsapp','video']
    query = remove_words(query, words_to_remove)
    
    try:
        query = query.strip().lower()
        # Fixed SQL query to use single LIKE pattern
        cursor.execute("SELECT phone FROM contacts WHERE LOWER(name) LIKE ?", ('%'+query+'%',))
        results = cursor.fetchall()
        
        if not results:
            speak('Contact not found')
            return 0, 0
            
        print(f"Found contact: {results[0][0]}")
        mobile_number_str = str(results[0][0])
        
        if not mobile_number_str.startswith('+91'):
            mobile_number_str = '+91' + mobile_number_str
            
        return mobile_number_str, query
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        speak('Error accessing contacts')
        return 0, 0
    except IndexError:
        print("No results found")
        speak('Contact not found')
        return 0, 0
    except Exception as e:
        print(f"Error: {e}")
        speak('Error finding contact')
        return 0, 0
    
    
def whatsapp(Phone, message, flag, name):
    if flag=='message':
        target_tab=16
        jarvis_message="Sending message to "+name
        
    elif flag=='call':
        target_tab=10
        message=''
        jarvis_message="Calling to "+name
        
    else:
        target_tab=11
        message=''
        jarvis_message="Video Calling to "+name
        
    #Encode the message for URL
    encoded_message=quote(message)
    speak(jarvis_message)
    print(jarvis_message)
    #Construct the URL
    whatsapp_url=f"https://web.whatsapp.com/send?phone={Phone}&text={encoded_message}"

    #Construct the full command
    full_command=f'start "" "{whatsapp_url}" '
    
    #open whatsapp with the contructed URL using cmd.exe
    subprocess.run(full_command, shell=True)
    time.sleep(5)
    subprocess.run(full_command, shell=True)
    
    pyautogui.hotkey('ctrl', 'f')

    for i in range(1, target_tab):
        pyautogui.hotkey('tab')
    pyautogui.hotkey('enter')
    speak(jarvis_message)