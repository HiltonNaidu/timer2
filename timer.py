import threading
import pygame
from settings import *
import datetime
import os

# Define a class to represent a clock thread
class Clock(threading.Thread):
    def __init__(self, duration):
        super().__init__()

        self.initial_duration = self.duration = duration

        self.duration_min = duration // 60

        self.reading_time = self.initial_reading_time = 0

        self.reading_time_min = 0

        self.paused = True
        self.finished = False

        self.lock = threading.Lock()

        self.current_time = 0
        # self.cooldown = 0

        self.click_sound = pygame.mixer.Sound(os.path.join("sound","mixkit-one-clap-481.wav"))

    def run(self):
        while not self.finished:
            with self.lock:
                if not self.paused:
                    if self.reading_time > 0:
                        self.reading_time -= 1
                    else:
                        self.duration -= 1

                    if self.duration <= 0:
                        self.paused = True
                        self.duration = 0

            self.duration_min = self.duration // 60
            self.reading_time_min = self.reading_time // 60
            pygame.time.wait(1000)

        self.finished = True
        self.duration = 0

    def pause(self):
        with self.lock:
            self.paused = True

    def play(self):
        with self.lock:
            self.paused = False

    def reset(self):
        with self.lock:
            self.duration = self.initial_duration
            self.reading_time = self.initial_reading_time
            self.finished = False

    def end(self):
        with self.lock:
            self.finished = True

# Define a class to represent a timer sprite
class Timer(pygame.sprite.Sprite):
    def __init__(self, name, duration, pos):
        super().__init__()

        # Create a clock instance inside the timer
        self.clock = Clock(duration)

        self.image_inactive = os.path.join(COLOUR_MODE, "timer base inactive.png")
        self.image_active = os.path.join(COLOUR_MODE, "timer base active.png")
        self.active = False

        self.name = name

        self.time_font = pygame.font.Font(None, 170)
        self.name_font = pygame.font.Font(None, 120)
        self.notes_font = pygame.font.Font(None, 30)

        self.colour = pygame.Color(0, 0, 0)
        self.colour.hsva = (195, 25, 90, 100)

        self.notes = ""

        self.update(True)

        self.rect = self.image.get_rect(center=pos)  # Use center directly during rect creation

        self.clock.start()

    def update(self, event):
        if self.active:
            self.image = pygame.image.load(self.image_active)
        else:
            self.image = pygame.image.load(self.image_inactive)
        self.image = pygame.transform.scale(self.image, (1100, 210))

        if event or (event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN):
            self.name_surface = self.name_font.render(self.name.upper(), 1, COLOURS["black"])
            self.name_rect = self.name_surface.get_rect(topleft=(self.image.get_rect().left + 30, self.image.get_rect().top + 30))

            self.notes_surface = self.notes_font.render(self.notes.upper(), 1, COLOURS["black"])
            self.notes_rect = self.notes_surface.get_rect(center=self.image.get_rect().center)
            self.notes_rect[0] += 0
            self.notes_rect[1] += -30

        functional_duration = self.clock.duration + self.clock.reading_time
        timedelta_obj = datetime.timedelta(seconds=functional_duration)
        self.text_surface = self.time_font.render(str(timedelta_obj), 1, COLOURS["black"])
        self.text_rect = self.text_surface.get_rect(left=(self.image.get_rect().left + 650), top=(self.image.get_rect().top + 40))

        self.image.blit(self.text_surface, self.text_rect)
        self.image.blit(self.name_surface, self.name_rect)
        self.image.blit(self.notes_surface, self.notes_rect)

        if self.clock.reading_time == 0:
            self.bar_surface = pygame.image.load(os.path.join(COLOUR_MODE, "bar.png"))
            self.bar_surface = pygame.transform.scale(self.bar_surface, (600, 70))
            self.bar_rect = self.bar_surface.get_rect(center=self.image.get_rect().center)
            self.bar_rect[0] += -220
            self.bar_rect[1] += 45
            self.image.blit(self.bar_surface, self.bar_rect)

            try:
                self.width = 595 - (self.clock.duration / self.clock.initial_duration * 595)
            except ZeroDivisionError:
                pass

            self.colour.hsva = (int(self.clock.duration / self.clock.initial_duration * 118), 100, 100, 100)
            pygame.draw.rect(self.image, self.colour, pygame.Rect(33, 119, self.width, 62), 0)
        else:
            self.bar_surface = pygame.image.load(os.path.join(COLOUR_MODE, "reading time.png"))
            self.bar_surface = pygame.transform.scale(self.bar_surface, (600, 70))
            self.bar_rect = self.bar_surface.get_rect(center=self.image.get_rect().center)
            self.bar_rect[0] += -220
            self.bar_rect[1] += 45
            self.image.blit(self.bar_surface, self.bar_rect)
