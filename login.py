import pygame
from settings import *
from button import Button, InputBox

class LoginScreen:
    def __init__(self, screen):
        self.screen = screen

        self.username_box = InputBox((SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 30), os.path.join(COLOUR_MODE, "text box active.png"), os.path.join(COLOUR_MODE, "text box inactive.png"), 11, "Username")
        self.password_box = InputBox((SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 30), os.path.join(COLOUR_MODE, "text box active.png"), os.path.join(COLOUR_MODE, "text box inactive.png"), 11, "Password")
        self.login_button = Button(11, (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 100), os.path.join(COLOUR_MODE, "start button.png"), self.login_attempt)

        self.input_boxes = pygame.sprite.Group(self.username_box, self.password_box)
        self.buttons = pygame.sprite.Group(self.login_button)

        self.logged_in = False

    def login_attempt(self):

        try:
            if self.password_box.text_submit == USERS[self.username_box.text_submit]:
                self.logged_in = True
                pygame.time.wait(1000)

        except:
            pass


    def deal_with_events(self, event):
        for box in self.input_boxes:
            box.handle_event(event)


    def run(self, event):
       
        
        self.input_boxes.update()
        self.input_boxes.draw(self.screen)

        self.buttons.update(event)
        self.buttons.draw(self.screen)

