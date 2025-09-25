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
import time
import webbrowser
import eel
import pygame
from Backend.config import ASSISSTANT_NAME
import os
from Backend.command import speak
import re
import pywhatkit as kit
import sqlite3

from Backend.helper import extract_yt_term
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