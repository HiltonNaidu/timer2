"""
The purpose of this file is to be the only file that the user interacts with 
it is designed so that the user can run one file and then it works 
"""



import pygame
import utility
from settings import * 

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
    
    def run(self):
        # Start the main application loop
        while True:

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    self.terminate()

                self.handle_input(event)
 
            self.screen.fill('black')
            # self.mode.run()
            pygame.display.flip()
            self.clock.tick(FPS)
    
    def handle_input(self, event):
        # Handle user input and events
        # if event.type == pygame.KEYDOWN:
        #     if event.key == pygame.K_a:
        #         self.mode.create_clock()
        pass
    
    def update_timers(self):
        # Update the timers and their states
        pass
    
    def display_timers(self):
        # Display the timers and their information on the UI
        pass

    def terminate(self):
        utility.error_log.create_log_recipt("error log")
        # end threads 
        pygame.quit()
        sys.exit()

# Create an instance of the application
app = ExamTimerApp()
app.run()
