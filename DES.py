# -*- coding: utf-8 -*-
# @Time    : 2021/4/19 16:20
# @Author  : AA8j
# @FileName: DES.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/qq_44874645
from pyDes import des, CBC, PAD_PKCS5
import binascii


def des_encrypt(string, key):
    secret_key = key
    iv = secret_key
    k = des(secret_key, CBC, iv, pad=None, padmode=PAD_PKCS5)
    en = k.encrypt(string, padmode=PAD_PKCS5)
    return binascii.b2a_hex(en)


def des_decrypt(string, key):
    secret_key = key
    iv = secret_key
    k = des(secret_key, CBC, iv, pad=None, padmode=PAD_PKCS5)
    de = k.decrypt(binascii.a2b_hex(string), padmode=PAD_PKCS5)
    return de


if __name__ == '__main__':
    KEY = '12345678'
    s = 'admin'
    encode = des_encrypt(s, KEY)
    print(encode)
    decode = des_decrypt(encode, KEY)
    print(decode)
