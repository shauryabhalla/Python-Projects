from selenium import webdriver
from random import randint
import keyboard

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

def anasd():
    return randint(100000,1000000)



while True:
    if keyboard.is_pressed('space'):
        a = anasd()
        b = str(a)
        driver.get('https://prnt.sc/' + b)
    if keyboard.is_pressed('esc'):
        break



