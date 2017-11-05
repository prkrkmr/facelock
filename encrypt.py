#!/usr/bin/env python
import os
from subprocess import Popen

def encrypt_file(file_name, password):
    '''
    Function takes argument as filename and password to encrypt the file using
    openssl application installed.
    '''
    process_encrypt = Popen(['openssl', 'aes-256-cbc', '-salt', '-in', file_name, '-out',
                             str(file_name)+".enc", '-pass', 'pass:'+str(password)])
    process_encrypt.communicate()
    os.remove(file_name)
