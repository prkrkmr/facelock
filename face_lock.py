#!/usr/bin/env python
from os import path
from os import remove
from os import mkdir
from os.path import expanduser
from sys import argv
from takeImage import imageCapture
from encode_image import encode_base64
from webCam import image_matching
from decode_image import decode_base
from pass_encryption import pass_enc
from encrypt import encrypt_file
from decrypt import decrypt_file

home = expanduser("~")
temp_image = '/tmp/facelock.png'
face_lock_image = home + '/.facelock/image'
face_lock_dir = home + '/.facelock/'

def check_dir():
    '''
    Checks if the directory assigned for facelock exists
    or not. If not it creates that directory.
    '''
    if path.exists(face_lock_image) == False:
        mkdir(face_lock_dir)

def file_read():
    '''
    Reads the file of the facelock image and returns 
    the content of it.
    '''
    with open(face_lock_image, 'rb') as returnData:
        return returnData.read()

def pass_value():
    '''
    Reads the content of the file and returns the password
    value.
    '''
    file_content = file_read()
    for i in file_content:
        if i.isdigit():
            return file_content.index(i)*file_content.index(i)

def rm_tmp_img():
    remove(temp_image)

if argv[1] == 'setup':
    check_dir()
    imageCapture(temp_image)
    encode_base64(temp_image, face_lock_image) 
    rm_tmp_img()

if argv[1] == 'encrypt':
    check_dir()
    decode_base(temp_image, face_lock_image)
    if image_matching(temp_image) == True:
        encrypt_file(argv[2], pass_enc(file_read()[pass_value():pass_value()+100]))
    rm_tmp_img()

if argv[1] == 'decrypt':
    check_dir()
    decode_base(temp_image, face_lock_image)
    if image_matching(temp_image) == True:
        decrypt_file(argv[2], pass_enc(file_read()[pass_value():pass_value()+100]))
    rm_tmp_img()
