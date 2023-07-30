import pygame
import sys 
import utility

# initialise pygame 
pygame.init()


# getting screen data and size 
screen_info = pygame.display.Info()
SCREEN_WIDTH = screen_info.current_w
SCREEN_HEIGHT = screen_info.current_h

# font 
FONT = pygame.font.Font(None, 36)

# colours 
COLOURS = {
    "black": (0, 0, 0), 
    "white": (255, 255, 255)
}

# frame rate of game 
FPS = 60 

# window name 
WINDOW_NAME = "Timer Program"

# determining the operating system 
systems = {
    "darwin": "macos",
    "win32": "windows",
    "linux" and "linux2": "linux"
}
try:
    OS = systems[sys.platform]
except:
    utility.error_message("""invalid OS
    default --> MacOS
    """)

    OS = systems["darwin"]


# system colour mode 
try:
    if utility.check_appearance():
        COLOUR_MODE = "dark"
    else:
        COLOUR_MODE = "light"
except:
    utility.error_message("""no detected colour mode
    default --> light  """)
    COLOUR_MODE = "light"




# class TimerSettings:
#     def __init__(self):
#         self.timer_duration = 0
#         self.reading_time = 0
#         self.time_warnings = []
    
#     def set_timer_duration(self, duration):
#         self.timer_duration = duration
    
#     def set_reading_time(self, time):
#         self.reading_time = time
    
#     def set_time_warnings(self, warnings):
#         self.time_warnings = warnings
