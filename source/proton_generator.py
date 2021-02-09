# ! python3

import pyautogui
import sys
import time
import random
import string

import requests
from proxyscrape import create_collector, get_collector
from selenium import webdriver
from selenium.common.exceptions import WebDriverException, TimeoutException
from selenium.webdriver.chrome.options import Options

### Chrome needs to be open before starting the program ###


# Printing funtion with 3 modes
# 1 : Normal message
# 2 : Information message
# 3 : Caution message


def proxy_connection():
    collector = create_collector('my-collector', 'https')
    proxy_status = "false"

    while proxy_status == "false":

        # Retrieve only 'us' proxies
        proxygrab = collector.get_proxy({'code': ('fr')})
        proxy = ("{}:{}".format(proxygrab.host, proxygrab.port))
        print('\033[31m' + "Proxy:", proxy + '\033[0m')

        try:
            proxy_host = proxygrab.host
            proxy_port = proxygrab.port
            proxy_auth = ":"
            proxies_file = {'http': 'http://{}@{}:{}/'.format(proxy_auth, proxy_host, proxy_port)}
            requests.get("http://protonmail.com/", proxies=proxies_file, timeout=3.5)

        except OSError:
            print('\033[31m' + "Proxy Connection error!" + '\033[0m')
            time.sleep(1)
            sys.stdout.write("\033[F")
            sys.stdout.write("\033[K")
            sys.stdout.write("\033[F")
            sys.stdout.write("\033[K")
            proxy_status = "false"
        else:
            print('\033[31m' + "Proxy is working..." + '\033[0m')
            time.sleep(1)
            sys.stdout.write("\033[F")
            sys.stdout.write("\033[K")
            sys.stdout.write("\033[F")
            sys.stdout.write("\033[K")
            proxy_status = "true"
            options = Options()
            options.add_argument('--proxy-server={}'.format(proxy))

    # Change Path to Chrome Driver Path (or move your ChromeDriver into the project folder)
    options = webdriver.ChromeOptions()
    options.add_experimental_option('detach', True)
    driver = webdriver.Chrome(executable_path='chromedriver', options=options)

    url = 'https://mail.protonmail.com/create/new?language=en'

    driver.get(url)
    driver.maximize_window()
    driver.implicitly_wait(3)


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


# Function used to generate the credential information
def generate_info(username):
    click_to_username()

    # Print message
    msg(1, 'Generating credentials...')

    # Username
    _username_ = username
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



def click_to_username():
    time.sleep(2)
    _username_box_ = pyautogui.locateOnScreen('images/choose_username_proton.png')
    _location_ = pyautogui.center(_username_box_)
    # Clicking the start button
    if not pyautogui.click(_location_):
        msg(1, 'Clicked to username box successfully !')
    else:
        msg(3, 'Failed to click on username box !')
        ext()


def close_chrome():
    _close_button_ = pyautogui.locateOnScreen('images/close_chrome_button.png')
    _location_ = pyautogui.center(_close_button_)
    # Clicking the start button
    if not pyautogui.click(_location_):
        msg(1, 'Chrome closed successfully !')
    else:
        msg(3, 'Failed to close Chrome !')
        ext()


# Main function
if __name__ == '__main__':

    # to increment email files
    email_counter = 0

    # open email names file
    f = open('email_names.txt', 'r')
    email_lines = f.read().splitlines()


    for i in range(1, 30):
        for j in range(1, 3):
            # connect to proxy, open ChromeDriver, launches ProtonMail signup page
            proxy_connection()

            while email_counter < len(email_lines):
                if generate_info(email_lines[email_counter]):
                    msg(3, 'Failed to execute "generate_info" command.')
                    ext()

                # close_chrome()

                exit()
                email_counter += 1



    msg(1, 'Done...')
    ext()
