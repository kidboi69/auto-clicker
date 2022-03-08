# importing modules
from selenium import webdriver
from pynput.mouse import Button, Controller
from time import sleep
from datetime import datetime, timedelta
from selenium.webdriver.common.by import By

print('''  
 ██████╗██╗     ██╗ ██████╗██╗  ██╗██████╗  ██████╗ ████████╗
██╔════╝██║     ██║██╔════╝██║ ██╔╝██╔══██╗██╔═══██╗╚══██╔══╝
██║     ██║     ██║██║     █████╔╝ ██████╔╝██║   ██║   ██║   
██║     ██║     ██║██║     ██╔═██╗ ██╔══██╗██║   ██║   ██║   
╚██████╗███████╗██║╚██████╗██║  ██╗██████╔╝╚██████╔╝   ██║   
 ╚═════╝╚══════╝╚═╝ ╚═════╝╚═╝  ╚═╝╚═════╝  ╚═════╝    ╚═╝                                                          
Credits to: https://github.com/xtekky

Available websites:
- [1] -- https://kohiclicktest.org/
- [2] -- https://cpstest.org/kohi-click-test.php
- [3] -- https://clickspeedtest.com/kohi-click-test.html
''')

mouse = Controller()
site = ()
website = input('Which website [1-3]: ')

if website == '1':
    site = "https://kohiclicktest.org/"
if website == '2':
    site = "https://cpstest.org/kohi-click-test.php"
if website == '3':
    site = "https://clickspeedtest.com/kohi-click-test.html"

# starting interface/driver
driver = webdriver.Chrome(executable_path="C:\Program Files (x86)\chromedriver.exe")  # linking chromedriver path
driver.get(site)  # loading site

if website == '1':
    sleep(1)
    mouse.position = (457, 658)
    sleep(1)

    def click():
        end_time = datetime.now() + timedelta(seconds=5)
        while datetime.now() < end_time:
            # Press and release
            mouse.press(Button.left)
            mouse.release(Button.left)
    click()

if website == '2':
    driver.execute_script("window.scrollBy(0,425)", "")
    sleep(1)
    mouse.position = (512, 611)
    sleep(1)

    def click():
        end_time = datetime.now() + timedelta(seconds=10)
        while datetime.now() < end_time:
            # Press and release
            mouse.press(Button.left)
            mouse.release(Button.left)
            sleep(0.0001)
    click()

if website == '3':
    driver.find_element(By.XPATH, '//*[@id="ez-accept-all"]').click()
    driver.execute_script("window.scrollBy(0,2350)", "")
    sleep(1)
    mouse.position = (480, 600)
    sleep(1)

    def click():
        global cps
        end_time = datetime.now() + timedelta(seconds=5)
        while datetime.now() < end_time:
            # Press and release
            mouse.press(Button.left)
            mouse.release(Button.left)
    click()
    
