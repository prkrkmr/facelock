#!/usr/bin/env python
from subprocess import Popen
import os

def decrypt_file(file_name, password):
    '''
    Function takes argument as filename and password to encrypt the file using
    openssl application installed.
    '''
    decryption_process = Popen(['openssl', 'enc', '-pass', 'pass:' + str(password),
                                '-d', '-aes-256-cbc', '-in',
                                file_name, '-out', str(file_name).strip('.enc')])
    decryption_process.communicate()
    os.remove(file_name)
