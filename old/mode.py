from timer import Timer
from old.button import Button, InputBox
import pygame
from settings import *
from colors import Background
import datetime


class main_screen:
    def __init__(self, screen, main):
        self.timers = pygame.sprite.Group()
        self.buttons = pygame.sprite.Group()
        self.selected = pygame.sprite.Group()
        # self.input_boxes = []
        
        self.main = main 

        self.font = pygame.font.Font(None, 56)

        self.screen = screen 

        self.click_sound = pygame.mixer.Sound("sound/mixkit-one-clap-481.wav")

        self.timers.add(Timer("None", 60, SLOTS[1]))
        # self.timers.add(Timer("math", 20, SLOTS[2]))

        self.active_timer = self.timers.sprites()[0]

        self.name = InputBox((125, 90), "images/text box active.png", "images/text box inactive.png", 11, self.active_timer.name) # .name 
        self.duration = InputBox((125, 195), "images/text box active.png", "images/text box inactive.png", 11, self.active_timer.clock.duration_min) # .duration 
        self.pause = Button(11, (65, 287), "images/pause button.png", self.active_timer.clock.pause) # . pause()
        self.play = Button(11, (185, 287), "images/play button.png", self.active_timer.clock.play)  # .play()
        self.reading_time = InputBox((185, 378), "images/reading time active.png", "images/reading time inactive.png", 11, 0) # .reading time
        self.notes = InputBox((165, 450), "images/notes active.png", "images/notes inactive.png", 11, '') # . text
        self.delete = Button(11, (72, 519), "images/delete button.png", self.delete_active_timer) # .terminate() 
        self.reset = Button(11, (185, 519), "images/reset button.png", self.active_timer.clock.reset) # . reset()

        self.new_timer = Button(11, (125, 605), "images/new timer button.png", self.add_timer)
        self.playall = Button(11, (125, 675), "images/play all button.png", self.play_all)
        self.pauseall = Button(11, (125, 740), "images/pause all button.png", self.pause_all)
        self.exit = Button(11, (125, 805), "images/exit button.png", self.main.background.home)



        self.buttons.add(self.pause, self.play, self.delete, self.reset, self.new_timer, self.exit, self.playall, self.pauseall)
        self.selected.add(self.name, self.duration, self.reading_time, self.notes)

        self.link()

        self.time = str(datetime.datetime.now())

        self.time_surface = self.font.render(self.time, True, COLOURS["black"])
        # self.time_rect = self.time_surface.get_rect(center=self.image.get_rect().center)

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
        for i in range(3):
            full = False
            for timer in self.timers:
                if timer.rect.collidepoint(SLOTS[i+1]):
                    full = True 

            if full == False:
                self.timers.add(Timer("None", 60, SLOTS[i+1]))
                return
                    
                

    def deal_with_events(self, event):
        for box in self.selected:
             box.handle_event(event)

        for timer in self.timers:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if timer.rect.collidepoint(event.pos):
                    self.active_timer = timer
                    self.link()
                    self.click_sound.play()

        if event.type == pygame.KEYDOWN:
                
                if event.key == pygame.K_RETURN:

                    try:


                        for box in self.selected:
                            if box.active:
                                pass

                    
                        self.active_timer.clock.duration = self.active_timer.clock.initial_duration = int(self.duration.text_submit) * 60
                        
                        self.active_timer.name = self.name.text_submit
                        self.active_timer.clock.reading_time = self.active_timer.clock.initial_reading_time = int(self.reading_time.text_submit) * 60
                        self.active_timer.notes = self.notes.text_submit
                        print(self.active_timer.clock.initial_reading_time)
                        
                    except:
                        pass


             
    def end(self):
        for thread in self.timers:
            thread.clock.end()


    def run(self, event):

        # self.deal_with_events(event)
        try:
            # self.duration.text_submit = str(self.active_timer.clock.duration_min)
            self.name.text_submit = self.active_timer.name
            # self.reading_time.text_submit = str(self.active_timer.clock.reading_time_min)
            self.notes.text_submit = self.active_timer.notes
        except:
            pass


        self.timers.update(event)
        self.timers.draw(self.screen)
        self.buttons.update(event)
        self.buttons.draw(self.screen)


        self.time = str(datetime.datetime.now())[10:19]
        self.time_surface = self.font.render(self.time, True, COLOURS["black"])
        self.screen.blit(self.time_surface, (1250, 25))


        try:

            self.selected.update()
            self.selected.draw(self.screen)

        except:
            pass

        # for box in self.input_boxes:
        #     box.update()
        #     box.draw(self.screen)

