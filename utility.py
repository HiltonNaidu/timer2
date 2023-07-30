import subprocess
import log

# function used to check the appearacne of a macos operating system 

def check_appearance():
    """Checks DARK/LIGHT mode of macos."""
    cmd = 'defaults read -g AppleInterfaceStyle'
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE,
                         stderr=subprocess.PIPE, shell=True)
    return bool(p.communicate()[0])

### error log section 

error_log = log.ChangeLog()

def error_message(message):
    print(message)
    error_log.add_log_entry(message)

def message(message):
    print(message)

###
