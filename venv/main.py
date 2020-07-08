# Harry potter theme invisible cloak project.
# Akshay JS Upadhyay

# import libraries
import numpy as np
import cv2

import time

cap = cv2.VideoCapture(0)           # to select the webcam.
time.sleep(2)

background = 0

# capturing the background
for i in range(30):
    ret, background = cap.read()

while(cap.isOpened()):
    ret, img = cap.read()
