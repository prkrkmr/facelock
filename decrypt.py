#!/usr/bin/env python
from subprocess import Popen
import os

def decrypt_file(file_name, password):
    '''
    Function takes argument as filename and password to encrypt the file using
    openssl application installed.
    '''
    p =  Popen(['openssl', 'enc', '-pass', 'pass:' + str(password), '-d', '-aes-256-cbc', '-in',
        file_name, '-out', str(file_name).strip('.enc')])
    p.communicate() 
    os.remove(file_name)
