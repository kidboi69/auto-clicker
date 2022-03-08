# importing modules
from selenium import webdriver
from pynput.mouse import Button, Controller
from time import sleep
from datetime import datetime, timedelta
mouse = Controller()

# starting interface/driver
driver = webdriver.Chrome(executable_path="C:\Program Files (x86)\chromedriver.exe")  # linking chromedriver path
driver.get("https://kohiclicktest.org/")  # loading site
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
