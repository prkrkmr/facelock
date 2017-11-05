#!/usr/bin/env python
from time import sleep
import os
import cv2
import base64

def imageCapture(write_image_file):
    '''
    captures the image and retuns its  base64 data
    '''
    camera = cv2.VideoCapture(0)
    sleep(0.1)  
    return_value,image = camera.read()
    cv2.imwrite(write_image_file,image)
    del(camera)
