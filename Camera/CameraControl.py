### Camera Control

# Imports
import cv2
import numpy as np
from simple_camera import *

# width = 640
# height = 480
# cap = cv2.VideoCapture("/dev/video0")

# while True:
#     success, img = cap.read()
#     img = cv2.resize(img, (width, height))
#     cv2.imshow("Camera", img)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

show_camera()
