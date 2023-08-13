import pygame
from settings import *

class ColorIntegration:
    def __init__(self):
        self.color_mode = "default"
    
    def detect_color_mode(self):
        # Detect the native color mode of the OS
        pass
    
    def set_color_mode(self, color_mode):
        self.color_mode = color_mode

class Background(pygame.sprite.Sprite):
    def __init__(self, image, location):
        pygame.sprite.Sprite.__init__(self)  #call Sprite initializer
        self.mode = image 
        self.image = pygame.image.load(SCREENS[image])
        self.image = pygame.transform.scale(self.image, (SCREEN_WIDTH, SCREEN_HEIGHT))
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location

    def toggle_bg(self):
        if self.mode == "home":
            self.image = SCREENS["main"]
            self.mode = "main"
        elif self.mode == "main":
            self.image = SCREENS["home"]
            self.mode = "home"

        self.image = pygame.image.load(SCREENS[self.mode])
        self.image = pygame.transform.scale(self.image, (SCREEN_WIDTH, SCREEN_HEIGHT))

    def make_image(self):
        self.image = pygame.image.load(SCREENS[self.mode])
        self.image = pygame.transform.scale(self.image, (SCREEN_WIDTH, SCREEN_HEIGHT))


    def instructions(self):
        self.mode = "instructions"
        self.make_image()
    def home(self):
        self.mode = "home"
        self.make_image()
    def main(self):
        self.mode = "main"
        self.make_image()