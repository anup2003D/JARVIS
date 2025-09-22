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
    
    
import eel
import pygame
from Backend.config import ASSISSTANT_NAME
import os
from Backend.command import speak

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
    
    if query!="":
        speak("Opening " + query)
        os.system("start "+(query))
    else:
        speak("Please specify what to open.")