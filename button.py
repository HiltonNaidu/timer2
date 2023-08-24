import pygame
from settings import *
from log import change_log

class Button(pygame.sprite.Sprite):
    def __init__(self, size_factor, pos, image, action, cooldown_time=500):
        super().__init__()

        self.action = action
        self.click_sound = pygame.mixer.Sound("sound/mixkit-one-clap-481.wav")
        self.cooldown_time = cooldown_time  # Cooldown time in milliseconds
        self.last_pressed_time = 0  # Initialize the time of the last press as 0

        # Load the button image and scale it
        self.image = pygame.image.load(image)
        self.image = pygame.transform.scale(self.image, (self.image.get_size()[0] // size_factor, self.image.get_size()[1] // size_factor))

        # Create the button's rectangular hitbox
        self.rect = self.image.get_rect()
        self.rect.center = pos

    def pressed(self):
        # Get the current time
        current_time = pygame.time.get_ticks()

        # Check if the button can be pressed (cooldown period elapsed)
        if current_time - self.last_pressed_time >= self.cooldown_time:
            # Play the click sound and perform the associated action
            self.click_sound.play()
            self.action()

            # Update the time of the last press
            self.last_pressed_time = current_time

    def update(self, event):
        # Check for a mouse click event and collision with the button
        if event.type == pygame.MOUSEBUTTONDOWN and self.rect.collidepoint(pygame.mouse.get_pos()):
            self.pressed()

class InputBox(pygame.sprite.Sprite):
    def __init__(self, pos, active_image, inactive_image, size_factor, text=''):
        super().__init__()

        self.size_factor = size_factor
        self.inactive_image = inactive_image
        self.active_image = active_image

        # Initialize text, submitted text, and activation status
        self.text = str(text)
        self.text_submit = self.text
        self.active = False
        self.first_enter_press = True

        # Load and scale the inactive image as the initial appearance
        self.image = pygame.image.load(self.inactive_image)
        self.image = pygame.transform.scale(self.image, (self.image.get_size()[0] // size_factor, self.image.get_size()[1] // size_factor))

        # Configure the text rendering
        self.color = COLOURS["black"]
        self.text_surface = FONT.render(self.text, True, self.color)
        self.textrect = self.text_surface.get_rect(center=self.image.get_rect().center)

        # Create the hitbox for the input box
        self.rect = self.image.get_rect()
        self.rect.center = pos

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Toggle activation when clicking on the input box
            if self.rect.collidepoint(event.pos):
                self.active = not self.active
                # if not self.active:
                self.first_enter_press = True
            else:
                self.active = False

        if event.type == pygame.KEYDOWN and self.active:
            if self.first_enter_press:
                # Clear text on first Enter press
                self.text = ""
                self.first_enter_press = False

            if event.key == pygame.K_RETURN:
                if self.text != "":
                    # Log changes and update submitted text
                    change_log.add_log_entry(f"{self.text_submit} into {self.text}")
                self.text_submit = self.text
                self.active = False
                self.first_enter_press = True
            elif event.key == pygame.K_BACKSPACE:
                # Handle Backspace key
                self.text = self.text[:-1]
            else:
                # Add typed characters to the text (limited to 10 characters)
                if len(self.text) <= 10:
                    self.text += event.unicode

            self.text_surface = FONT.render(self.text, True, self.color)

    def update(self):
        if not self.active:
            # Display submitted text when not active
            self.text = self.text_submit

        # Update the image based on activation status
        if self.active:
            self.image = pygame.image.load(self.active_image)
        else:
            self.image = pygame.image.load(self.inactive_image)

        # Adjust the width of the input box based on text length
        width = max(200, self.text_surface.get_width() + 10)
        self.rect.w = width

        # Update the input box image with text
        if self.active:
            self.image = pygame.transform.scale(self.image, (self.image.get_size()[0] // self.size_factor, self.image.get_size()[1] // self.size_factor))
            self.textrect = self.text_surface.get_rect(center=self.image.get_rect().center)
            self.image.blit(self.text_surface, self.textrect)
        else:
            self.text_surface = FONT.render(self.text_submit, True, self.color)
            self.image = pygame.transform.scale(self.image, (self.image.get_size()[0] // self.size_factor, self.image.get_size()[1] // self.size_factor))
            self.textrect = self.text_surface.get_rect(center=self.image.get_rect().center)
            self.image.blit(self.text_surface, self.textrect)
