#!/usr/bin/env python
import base64
from pass_decryption import pass_dec

def decode_base(temp_image, face_lock_image):
    '''
    Converts the encrypted base64  file to image
    '''
    with open(face_lock_image, 'rb') as base64_file:
        base64_data = pass_dec(base64_file.read())
    with open(temp_image, "wb") as image_file:
        image_file.write(base64_data.decode('base64'))
