# ! python3

import pyautogui
import sys
import time
import random
import string


# Printing funtion with 3 modes
# 1 : Normal message
# 2 : Information message
# 3 : Caution message


def msg(_option_, _message_):
    if _option_ == 1:
        print('\x1b[0;32;40m> %s\x1b[0m' % _message_)
    elif _option_ == 2:
        print('\x1b[0;32;40m>\x1b[0m %s' % _message_)
    elif _option_ == 3:
        print('\n\x1b[0;32;40m[\x1b[0m%s\x1b[0;32;40m]\x1b[0m' % _message_)
    else:
        print('\n\x1b[0;31;40m[ERROR]\x1b[0m')


# Exiting function
def ext():
    msg(1, 'Exiting...')
    sys.exit()


# Function used to open Firefox
def open_firefox():
    # Printing basic message
    msg(1, 'Opening Chrome...')

    # Location the start button
    _start_button_ = pyautogui.locateOnScreen('images/start_button.png')
    _location_ = pyautogui.center(_start_button_)

    # Clicking the start button
    if not pyautogui.click(_location_):
        msg(1, 'Opened start menu successfully!')
    else:
        msg(3, 'Failed to open start menu!')
        ext()

    time.sleep(2)

    # Search for Firefox in the menu search
    pyautogui.typewrite('chrome')
    pyautogui.typewrite('\n')

    # Print message
    msg(1, 'Firefox is now open and running.')


# Function used to locate GMail
def locate_gmail():
    # Sleep for a while and wait for Firefox to open
    time.sleep(1)

    # Printing message
    msg(1, 'Opening Private navigation...')

    _start_button_ = pyautogui.locateOnScreen('images/private_navigation.png')
    _location_ = pyautogui.center(_start_button_)
    # Clicking the start button
    if not pyautogui.click(_location_):
        msg(1, 'Opened start menu successfully!')
    else:
        msg(3, 'Failed to open start menu!')
        ext()

    _start_button_ = pyautogui.locateOnScreen('images/private_navigation_button.png')
    _location_ = pyautogui.center(_start_button_)
    # Clicking the start button
    if not pyautogui.click(_location_):
        msg(1, 'Opened start menu successfully!')
    else:
        msg(3, 'Failed to open start menu!')
        ext()

    # Printing message
    msg(1, 'Opening Gmail...')

    # Typing the website on the browser
    pyautogui.keyDown('ctrlleft');
    pyautogui.typewrite('a');
    pyautogui.keyUp('ctrlleft')
    pyautogui.typewrite('mail.protonmail.com/create/new?language=en')
    pyautogui.typewrite('\n')

    # Wait for a while until the website responds
    time.sleep(1)

    # Print a simple message
    msg(1, 'Locating the form...')


# Function used to randomize credentials
def randomize(_option_, _length_):
    if _length_ > 0:

        # Options:
        #       -p      for letters, numbers and symbols
        #       -l      for letters only
        #       -n      for numbers only
        #       -m      for month selection
        #       -d      for day selection
        #       -y      for year selection

        if _option_ == '-p':
            string._characters_ = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()_+'
        elif _option_ == '-l':
            string._characters_ = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
        elif _option_ == '-n':
            string._characters_ = '1234567890'
        elif _option_ == '-m':
            string._characters_ = 'JFMASOND'

        if _option_ == '-d':
            _generated_info_ = random.randint(1, 28)
        elif _option_ == '-y':
            _generated_info_ = random.randint(1950, 2000)
        else:
            _generated_info_ = ''
            for _counter_ in range(0, _length_):
                _generated_info_ = _generated_info_ + random.choice(string._characters_)

        return _generated_info_

    else:
        msg(3, 'No valid length specified...')
        ext()


# Function used to generate the credential information
def generate_info(email_line):
    time.sleep(3)

    _start_button_ = pyautogui.locateOnScreen('images/choose_username_proton.png')
    _location_ = pyautogui.center(_start_button_)
    # Clicking the start button
    if not pyautogui.click(_location_):
        msg(1, 'Opened start menu successfully!')
    else:
        msg(3, 'Failed to open start menu!')
        ext()

    # Print message
    msg(1, 'Generating credentials...')



    # Username
    _username_ = email_lines[email_counter]
    pyautogui.typewrite(_username_)
    pyautogui.press('tab')
    pyautogui.press('tab')
    msg(2, '\x1b[0;33;40mUsername:\x1b[0m %s' % _username_)

    # Password
    _password_ = 'Azerty123=:'
    pyautogui.typewrite(_password_)
    pyautogui.press('tab')
    pyautogui.press('tab')
    msg(2, '\x1b[0;33;40mPassword:\x1b[0m %s' % _password_)

    # Password confirmation
    pyautogui.typewrite(_password_)
    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.press('tab')

    # go next step
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(1)
    pyautogui.press('enter')


# Main function
if __name__ == '__main__':

    # open email names file
    f = open('email_names.txt', 'r')
    email_lines = f.read().splitlines()

    if open_firefox():
        msg(3, 'Failed to execute "open_firefox" command.')
        ext()

    if locate_gmail():
        msg(3, 'Failed to execute "locate_gmail" command.')
        ext()

    # to increment email files
    email_counter = 0

    if generate_info(email_lines[email_counter]):
        msg(3, 'Failed to execute "generate_info" command.')
        ext()

    msg(1, 'Done...')
    ext()
