class SpecialNeedsOptions:
    def __init__(self):
        self.high_contrast = False
        self.large_text = False
        self.no_sound = False
        self.high_sound = False
    
    def toggle_high_contrast(self):
        self.high_contrast = not self.high_contrast
    
    def toggle_large_text(self):
        self.large_text = not self.large_text
    
    def toggle_no_sound(self):
        self.no_sound = not self.no_sound
    
    def toggle_high_sound(self):
        self.high_sound = not self.high_sound
