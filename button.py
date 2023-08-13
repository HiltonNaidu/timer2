from typing import Any
import pygame
#from pygame.sprite import Group 
from settings import * 
from log import change_log



class Button(pygame.sprite.Sprite):
    def __init__(self, size_factor, pos, image, action):
        super().__init__()

        self.action = action 
        # self.text_fuction = text
        # self.text = str(text)

        # loading the music to be played when pressed 
        self.click_sound = pygame.mixer.Sound("sound/mixkit-one-clap-481.wav")

        # self.font = FONT

        # loading the image via a given path 
        self.image = pygame.image.load(image)
        # transforming the size of the image via the ratio given 
        self.image = pygame.transform.scale(self.image, (self.image.get_size()[0]/size_factor, self.image.get_size()[1]/size_factor))
        

        # creating the rect of the button
        self.rect = self.image.get_rect()

        # making the position = to the center of a rect 
        self.rect.center = pos

    def pressed(self):
        self.click_sound.play()
        self.action()


    def update(self, event):
        # self.make_text()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(pygame.mouse.get_pos()):
                self.pressed()


class InputBox(pygame.sprite.Sprite):
    def __init__(self, pos, active, inactive, size_factor, text=''):
        super().__init__()

        self.size_factor = size_factor
        self.inactive_image = inactive
        self.active_image = active

        self.text = str(text)
        self.text_submit = self.text
        self.active = False
        self.screen = pygame.display.get_surface()

        self.image = pygame.image.load(self.inactive_image)
        self.image = pygame.transform.scale(self.image, (self.image.get_size()[0]/size_factor, self.image.get_size()[1]/size_factor))


        self.color = COLOURS["black"]
        self.text_surface = FONT.render(self.text, True, self.color)
        self.textrect = self.text_surface.get_rect(center=self.image.get_rect().center)
        
        
        self.rect = self.image.get_rect()
        self.rect.center = pos

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:

            # If the user clicked on the input_box rect.
            if self.rect.collidepoint(event.pos):
                # Toggle the active variable.
                self.active = not self.active
            else:
                self.active = False

            # Change the current color of the input box.
            # self.color = COLOR_ACTIVE if self.active else COLOR_INACTIVE


        if event.type == pygame.KEYDOWN:

            if self.active:

                if event.key == pygame.K_RETURN:
                    change_log.add_log_entry(f"{self.text_submit} into {self.text}")
                    self.text_submit = self.text
                    self.active = False

                elif event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]

                else:
                    if len(self.text) <= 10:
                        self.text += event.unicode

                # Re-render the text.
                self.text_surface = FONT.render(self.text, True, self.color)

    def update(self):
        # Resize the box if the text is too long.

        if self.active == False:
            self.text = self.text_submit

        if self.active:
            self.image = pygame.image.load(self.active_image)
        else:
            self.image = pygame.image.load(self.inactive_image)

        width = max(200, self.text_surface.get_width()+10)
        self.rect.w = width

        if self.active:
            self.image = pygame.transform.scale(self.image, (self.image.get_size()[0]/self.size_factor, self.image.get_size()[1]/self.size_factor))
            self.textrect = self.text_surface.get_rect(center=self.image.get_rect().center)
            self.image.blit(self.text_surface, self.textrect)
        else:
            self.text_surface = FONT.render(self.text_submit, True, self.color)
            self.image = pygame.transform.scale(self.image, (self.image.get_size()[0]/self.size_factor, self.image.get_size()[1]/self.size_factor))
            self.textrect = self.text_surface.get_rect(center=self.image.get_rect().center)
            self.image.blit(self.text_surface, self.textrect)
            self.text = self.text


