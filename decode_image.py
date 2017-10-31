#!/usr/bin/env python
import base64
from pass_decryption import pass_dec

def decode_base():
    '''
    Converts the encrypted base64  file to image
    '''
    with open('/home/prakhar/.facelock/image', 'rb') as base64_file:
        base64_data = pass_dec(base64_file.read())
    with open("/tmp/facelock.png", "wb") as image_file:
        image_file.write(base64_data.decode('base64'))
