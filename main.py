
import os
import eel
from Backend.feature import *
from Backend.command import *

def start():
    # Initialize eel
    eel.init('Frontend')
    os.system('start msedge.exe --app="http://127:0.0.1:5500/Frontend/index.html"')

    #play_assistant_sound()


    # Start the application - removed initial sound play and manual browser launch
    eel.start("index.html", 
            mode="edge",
            port=5500,
            host='localhost',
            block=True)

if __name__=="__main__":
    start()