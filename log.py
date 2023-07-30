class ChangeLog:
    def __init__(self):
        self.log_entries = []
    
    def add_log_entry(self, entry):
        self.log_entries.append(entry)
    
    def view_log(self):
        # Display the change log
        pass

    def create_log_recipt(self, file_name):
        file = open(file_name, "w")
        for entry in self.log_entries:
            file.write(entry)
            file.write("\n")

        file.close()

change_log = ChangeLog()