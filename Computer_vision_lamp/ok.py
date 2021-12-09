import serial
import time
import cv2
import handtrackingModule as hm
import numpy as np
import math
arduinoData = serial.Serial('COM3', 9600)
time.sleep(8)
arduinoData.write(bytes("X90Y90", 'UTF-8'))