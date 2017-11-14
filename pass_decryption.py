#!/usr/bin/env python


def pass_dec(password):
    '''
    decrypts password using this function
    '''

    enc_pass = ''
    for i in (password):
        enc_pass = enc_pass + str(chr(ord(i) - 1))
    return enc_pass
