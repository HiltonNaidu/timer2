"""
The purpose of this file is to be the only file that the user interacts with 
it is designed so that the user can run one file and then it works 
"""

import pygame
import utility
from settings import * 
from colors import Background
from button import Button
from timer import Timer
from mode import main_screen
from log import change_log

class ExamTimerApp:
    def __init__(self):

        # Initialize the application and user interface
        pygame.init()

        # creates screen acording to settings 
        self.screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

        # names the window acording to setting 
        pygame.display.set_caption(WINDOW_NAME)

        # sets a pygame clock 
        self.clock = pygame.time.Clock()

        # setting the mode as "home" which is default 
        self.mode = 'home'

        # making the background from the class 
        self.background = Background(self.mode, [0,0])

        # setting all the pygame sprite groups 
        self.buttons_home_screen = pygame.sprite.Group()
        self.buttons_main_scrren = pygame.sprite.Group()
        self.buttons_instruction_screen = pygame.sprite.Group()
        # self.timers = pygame.sprite.Group()

        self.main_screen = main_screen(self.screen, self)

        self.buttons_instruction_screen.add(Button(11, (125, 805), "images/back button.png", self.background.home))

        self.buttons_home_screen.add(Button(11, (395, 545), "images/instruction button.png", self.background.instructions))
        self.buttons_home_screen.add(Button(11, (720, 545), "images/start button.png", self.background.main))
        self.buttons_home_screen.add(Button(11, [1045, 545], "images/exit button (home).png", self.terminate))

    def run(self):
        # Start the main application loop
        while True:

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    self.terminate() 
                
                self.main_screen.deal_with_events(event)

                if event.type == pygame.MOUSEBUTTONDOWN:
                    print(pygame.mouse.get_pos())

                # self.handle_input(event)
            




            
            # filling the screen a basic black colour 
            self.screen.fill('black')
            # drawing the backround onto the screen 
            self.screen.blit(self.background.image, self.background.rect)

            self.mode = self.background.mode

            # draw all the buttons for the home screen
            if self.mode == "home":
                self.buttons_home_screen.update(event)
                self.buttons_home_screen.draw(self.screen)

            if self.mode == "main":
                self.main_screen.run(event)

            if self.mode == "instructions":
                self.buttons_instruction_screen.update(event)
                self.buttons_instruction_screen.draw(self.screen)

            
            pygame.display.flip()

            self.clock.tick(FPS)
    
    # def handle_input(self, event):
    #     pass
    

    def terminate(self):
        utility.error_log.create_log_recipt("error log")

        # end threads 
        self.main_screen.end()

        change_log.create_log_recipt("change_log.txt")

        pygame.quit()
        sys.exit()

    

# Create an instance of the application
if OS == "macos":
    app = ExamTimerApp()
    app.run()
