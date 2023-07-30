import threading
import pygame
import utility

class Clock(threading.Thread):
    def __init__(self, name, duration):
        super().__init__()
        self.intial_duration, self.duration = duration
        self.name = name
        self.paused = False
        self.finished = False
        self.lock = threading.Lock()

    
    def run(self):
        while self.finished == False:
            with self.lock:
                if not self.paused:
                    self.duration  -= 1
                if self.duration <= 0:
                    try:
                        self.finished = True
                        return
                    except:
                        utility.error_message(f"error message in {self.name}")
            print(F"{self.name} as {self.duration}")
            pygame.time.wait(1000)  # Wait for 1 second
        
        self.finished = True
        self.duration = 0 

    
    # def pause(self):
    #     self.paused = True
    
    # def resume(self):
    #     self.paused = False

    def toggle(self):
        self.paused = not self.paused
    
    def reset(self):
        self.duration = self.intial_duration
        self.finished = False


class Timer(pygame.sprite.Sprite):
    def __init__(self, groups, name, duration):
        super().__init__(groups)
        self.clock = Clock(name, duration)
        
        