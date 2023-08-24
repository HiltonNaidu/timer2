import pygame
import sys 
import utility
import os 

# initialise pygame 
pygame.init()


# getting screen data and size 
screen_info = pygame.display.Info()
SCREEN_WIDTH = screen_info.current_w
SCREEN_HEIGHT = screen_info.current_h * 0.95


SLOTS = {
    1: (845, 220),
    2: (845, 470),
    3: (845, 715)
}

# font 
FONT = pygame.font.Font(None, 36)

# colours 
COLOURS = {
    "black": (0, 0, 0), 
    "white": (255, 255, 255),
    "inactive": (100, 100, 100),
    "active": (120, 300, 50)
}

# COLOR_INACTIVE = pygame.Color('lightskyblue3')
# COLOR_ACTIVE = pygame.Color('dodgerblue2')

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
# COLOUR_MODE = "light"

# home screens 

SCREENS = {
    "home": os.path.join(COLOUR_MODE, "home screen.png"),
    "main": os.path.join(COLOUR_MODE, "main screen.png"),
    "instructions": os.path.join(COLOUR_MODE, "instruction screen.png")
}


USERS = {
    "admin": "password", 
    "Maxwell": "123123"
}
