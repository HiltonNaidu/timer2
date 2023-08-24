"""
The purpose of this file is to be the only file that the user interacts with 
it is designed so that the user can run one file and then it works 
"""

import pygame
import utility
from settings import * 
from colors import Background
from button import Button
from mode import MainScreen
from log import change_log
from login import LoginScreen

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

        self.main_screen = MainScreen(self.screen, self)

        self.buttons_instruction_screen.add(Button(11, (125, 805), os.path.join(COLOUR_MODE, "back button.png"), self.background.home))

        self.buttons_home_screen.add(Button(11, (395, 545), os.path.join(COLOUR_MODE, "instruction button.png"), self.background.instructions))
        self.buttons_home_screen.add(Button(11, (720, 545), os.path.join(COLOUR_MODE, "start button.png"), self.background.main))
        self.buttons_home_screen.add(Button(11, [1045, 545], os.path.join(COLOUR_MODE, "exit button (home).png"), self.terminate))

        self.login = LoginScreen(self.screen)



    def run(self):
        # Start the main application loop
        while True:

            for event in pygame.event.get():
                self.event = event

                if self.event.type == pygame.QUIT:
                    self.terminate() 
                
                self.main_screen.deal_with_events(self.event)

                if not self.login.logged_in:
                    self.login.deal_with_events(self.event)

                if self.event.type == pygame.MOUSEBUTTONDOWN:
                    print(pygame.mouse.get_pos())


            if self.login.logged_in:

            
                # filling the screen a basic black colour 
                self.screen.fill('black')
                # drawing the backround onto the screen 
                self.screen.blit(self.background.image, self.background.rect)

                self.mode = self.background.mode

                # draw all the buttons for the home screen
                if self.mode == "home":
                    self.buttons_home_screen.update(self.event)
                    self.buttons_home_screen.draw(self.screen)
                    self.main_screen.pause_all()

                if self.mode == "main":
                    self.main_screen.run(self.event)

                if self.mode == "instructions":
                    self.buttons_instruction_screen.update(self.event)
                    self.buttons_instruction_screen.draw(self.screen)
                
                

            else:
                self.login.run(event)

            pygame.display.flip()

            self.clock.tick(FPS)
        

    def terminate(self):
        utility.error_log.create_log_recipt("error log.txt")

        # end threads 
        self.main_screen.end()

        change_log.create_log_recipt("change_log.txt")

        pygame.quit()
        sys.exit()

    

# Create an instance of the application
if OS == "macos":
    
    app = ExamTimerApp()
    app.run()
