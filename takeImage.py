#!/usr/bin/env python
from time import sleep
import cv2
import face_recognition
def imageCapture(write_image_file):
    '''
    captures the image and retuns its  base64 data
    '''
    camera = cv2.VideoCapture(0)
    sleep(2)
    return_value, image = camera.read()
    cv2.imwrite(write_image_file, image)
    del(camera)
    if checkImage(write_image_file) != True:
        imageCapture(write_image_file)
    else:
        print "Image Taken"

def checkImage(write_image_file):
    '''
    Check if the image is clearly available
    '''

    try:
        face = face_recognition.face_encodings(face_recognition.load_image_file(write_image_file))[0]
        return True
    except Exception as e:
        print "Cannot find a face, please bring your face closer to the camera or increase the lighting"
