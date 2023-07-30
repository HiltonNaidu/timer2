class ExamNotification:
    def __init__(self):
        self.start_notification = False
        self.middle_notification = False
        self.end_notification = False
    
    def set_start_notification(self, enabled):
        self.start_notification = enabled
    
    def set_middle_notification(self, enabled):
        self.middle_notification = enabled
    
    def set_end_notification(self, enabled):
        self.end_notification = enabled
    
    def send_notification(self, notification_type):
        # Send the specified notification
        pass
