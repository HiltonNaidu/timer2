from timer import Timer
from button import Button, InputBox
import pygame
from settings import *
import datetime

class MainScreen:
    def __init__(self, screen, main):
        self.timers = pygame.sprite.Group()
        self.buttons = pygame.sprite.Group()
        self.selected = pygame.sprite.Group()
        
        self.main = main
        self.font = pygame.font.Font(None, 56)
        self.screen = screen
        self.click_sound = pygame.mixer.Sound("sound/mixkit-one-clap-481.wav")

        if COLOUR_MODE == "dark":
            self.time_colour = COLOURS["white"]
        else:
            self.time_colour = COLOURS["black"]

        self.timers.add(Timer("None", 60, SLOTS[1]))
        self.active_timer = self.timers.sprites()[0]

        self.name = InputBox((125, 90), os.path.join(COLOUR_MODE, "text box active.png"), os.path.join(COLOUR_MODE, "text box inactive.png"), 11, self.active_timer.name)
        self.duration = InputBox((125, 195), os.path.join(COLOUR_MODE, "text box active.png"), os.path.join(COLOUR_MODE, "text box inactive.png"), 11, self.active_timer.clock.duration_min)
        self.pause = Button(11, (65, 287), os.path.join(COLOUR_MODE, "pause button.png"), self.active_timer.clock.pause)
        self.play = Button(11, (185, 287), os.path.join(COLOUR_MODE, "play button.png"), self.active_timer.clock.play)
        self.reading_time = InputBox((185, 378), os.path.join(COLOUR_MODE, "reading time active.png"), os.path.join(COLOUR_MODE, "reading time inactive.png"), 11, 0)
        self.notes = InputBox((165, 450), os.path.join(COLOUR_MODE, "notes active.png"), os.path.join(COLOUR_MODE, "notes inactive.png"), 11, '')
        self.delete = Button(11, (72, 519), os.path.join(COLOUR_MODE, "delete button.png"), self.delete_active_timer)
        self.reset = Button(11, (185, 519), os.path.join(COLOUR_MODE, "reset button.png"), self.active_timer.clock.reset)
        self.new_timer = Button(11, (125, 605), os.path.join(COLOUR_MODE, "new timer button.png"), self.add_timer)
        self.playall = Button(11, (125, 675), os.path.join(COLOUR_MODE, "play all button.png"), self.play_all)
        self.pauseall = Button(11, (125, 740), os.path.join(COLOUR_MODE, "pause all button.png"), self.pause_all)
        self.exit = Button(11, (125, 805), os.path.join(COLOUR_MODE, "exit button.png"), self.main.background.home)

        self.buttons.add(self.pause, self.play, self.delete, self.reset, self.new_timer, self.exit, self.playall, self.pauseall)
        self.selected.add(self.name, self.duration, self.reading_time, self.notes)

        self.link()

    def delete_active_timer(self):
        self.active_timer.clock.end()
        self.timers.remove(self.active_timer)

    def link(self):
        self.pause.action = self.active_timer.clock.pause
        self.play.action = self.active_timer.clock.play
        self.delete.action = self.delete_active_timer
        self.reset.action = self.active_timer.clock.reset

        self.duration.text_submit = str(self.active_timer.clock.initial_duration // 60)
        self.name.text_submit = self.active_timer.name
        self.reading_time.text_submit = str(self.active_timer.clock.initial_reading_time // 60)
        self.notes.text_submit = self.active_timer.notes

        self.active_timer.active = True

        for timer in self.timers:
            if timer != self.active_timer:
                timer.active = False

    def pause_all(self):
        for timer in self.timers:
            timer.clock.pause()

    def play_all(self):
        for timer in self.timers:
            timer.clock.play()

    def add_timer(self):
        for i, slot in enumerate(SLOTS):
            i += 1
            if not any(timer.rect.collidepoint(SLOTS[i]) for timer in self.timers):
                self.timers.add(Timer("None", 60, SLOTS[i]))
                return

    def deal_with_events(self, event):
        for box in self.selected:
            box.handle_event(event)

        for timer in self.timers:
            if event.type == pygame.MOUSEBUTTONDOWN and timer.rect.collidepoint(event.pos):
                self.active_timer = timer
                self.link()
                self.click_sound.play()

        if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
            try:
                for box in self.selected:
                    if box.active:
                        pass

                self.active_timer.clock.duration = self.active_timer.clock.initial_duration = int(self.duration.text_submit) * 60
                self.active_timer.name = self.name.text_submit
                self.active_timer.clock.reading_time = self.active_timer.clock.initial_reading_time = int(self.reading_time.text_submit) * 60
                self.active_timer.notes = self.notes.text_submit
                
            except ValueError:
                pass

    def end(self):
        for thread in self.timers:
            thread.clock.end()

    def run(self, event):
        try:
            self.name.text_submit = self.active_timer.name
            self.notes.text_submit = self.active_timer.notes
        except AttributeError:
            pass

        self.timers.update(event)
        self.timers.draw(self.screen)
        self.buttons.update(event)
        self.buttons.draw(self.screen)

        self.time = str(datetime.datetime.now())[10:19]
        self.time_surface = self.font.render(self.time, True, self.time_colour)
        self.screen.blit(self.time_surface, (1250, 25))

        try:
            self.selected.update()
            self.selected.draw(self.screen)
        except AttributeError:
            pass
