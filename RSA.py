# -*- coding: utf-8 -*-
# @Time    : 2021/4/17 1:18
# @Author  : AA8j
# @FileName: RSA.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/qq_44874645
import time

import rsa


def encrypt(string, key):  # 公钥加密
    key = rsa.PublicKey.load_pkcs1(key.encode())
    return rsa.encrypt(string.encode(), key).decode()
    # 加密后的密文（bytes）


def decrypt(string, key):  # 私钥解密
    key = rsa.PrivateKey.load_pkcs1(key.encode())
    return rsa.decrypt(string, key).decode()


def sign(string, key):  # 私钥签名
    key = rsa.PrivateKey.load_pkcs1(key.encode())
    return rsa.sign(string.encode(), key, 'SHA-1')


def verify(string, key, sign_code):  # 公钥验签
    key = rsa.PublicKey.load_pkcs1(key.encode())
    return rsa.verify(string.encode(), sign_code, key)


if __name__ == '__main__':
    # 生成密钥对
    (public_key, private_key) = rsa.newkeys(1024)
    pub_key = public_key.save_pkcs1().decode('utf-8')
    pri_key = private_key.save_pkcs1().decode('utf-8')

    String = 'admin'
    # 公钥加密私钥解密
    encode = encrypt(String, pub_key)
    print('公钥加密后：', encode)
    decode = decrypt(encode, pri_key)
    print('私钥解密后：', decode)

    # 私钥签名，公钥验签
    Sign = sign(String, pri_key)
    verify(String, pub_key, Sign)
