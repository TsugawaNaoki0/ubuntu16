# -*- coding: utf-8 -*-

from PIL import Image
from PIL import ImageGrab
import pytesseract
import numpy as np
import matplotlib.pyplot as plt
import pyautogui as pyag
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import cv2

os.chdir(os.path.dirname(os.path.abspath(__file__)))
pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files (x86)/Tesseract-OCR/tesseract'

fig, ax = plt.subplots()
mngr = plt.get_current_fig_manager()
mngr.window.setGeometry(10,800,1300,250)
plt.pause(0.001)

url = "https://10fastfingers.com/typing-test/english"
chrome_driver_path = "chromedriver.exe"
chrome_options = Options()
chrome_options.add_argument("--window-position=0,0");
chrome_options.add_argument("--window-size=1000,600");
browser = webdriver.Chrome(chrome_driver_path, chrome_options=chrome_options)

print("Loading...")
browser.get(url)
time.sleep(3)

while(True):
    print("-----------------------------------------")
    print("Extracted words")
    print("-----------------------------------------")

    img = ImageGrab.grab(bbox=(120,308,1213,430))

    ax.imshow(img)
    plt.pause(0.001)

    img =  np.array(img)
    img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    img = cv2.threshold(img, 220, 255, cv2.THRESH_BINARY)[1]
    img = Image.fromarray(img)

    words  = pytesseract.image_to_string(img).split(" ")

    for word1 in words:
        if ("\n\n" in word1):
            word1 = word1.split("\n\n")
        elif ("\n" in word1):
            word1 = word1.split("\n")
        else:
            word1 = [word1]

        for word2 in word1:
            print(word2)
            pyag.typewrite(word2.replace(" ", "") + " ")
            time.sleep(0.2)

    if len(words) < 10:
        print("Done!")
        break

time.sleep(3)

browser.quit()
