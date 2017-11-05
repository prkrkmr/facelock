#!/usr/bin/env python
import base64
import os
from pass_encryption import pass_enc

def encode_base64(read_image_file, write_image_file):
    '''
    Converts the image file to base64 file ,
    encrypts it and save into file
    '''

    with open(read_image_file, "rb") as image_file:
        encoded_string = pass_enc(base64.b64encode(image_file.read()))
    base64file = open(write_image_file, 'wb')
    base64file.write(encoded_string)
    base64file.close()
