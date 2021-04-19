# -*- coding: utf-8 -*-
# @Time    : 2021/4/19 9:20
# @Author  : AA8j
# @FileName: createCertificate.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/qq_44874645
import random

import rsa

from 算法.加密算法.改造https.RSA import sign
from 算法.加密算法.改造https.sendAndRec import send
from 算法.加密算法.改造https.sha_224 import sha_224


def rsa_create_key():
    print('正在生成密钥对...', end='')
    # 生成密钥对
    (public_key, private_key) = rsa.newkeys(1024)
    prv_key = private_key.save_pkcs1().decode()
    pub_key = public_key.save_pkcs1().decode()
    print('完成：', prv_key, pub_key)
    return prv_key, pub_key


def digital_signature(num, key):
    print('正在生成数字签名...', end='')
    # 摘要生成
    abstract = sha_224(num)
    # 私钥签名
    sign_bytes = sign(abstract, key)
    # 返回数字签名
    print('完成：', sign_bytes)
    return sign_bytes


def create_certificate():
    # 利用rsa算法生成密钥对
    prv_key, pub_key = rsa_create_key()
    # 10位伪随机数生成
    random_num = str(random.randint(1000000000, 10000000000))
    # 数字签名生成（私钥加密）
    digital_signature_result = digital_signature(random_num, prv_key)

    print('证书生成完成：', [prv_key, [pub_key, digital_signature_result, random_num]])
    # 私钥+证书（公钥+数字签名+随机数）
    return [prv_key, [pub_key, digital_signature_result, random_num]]


if __name__ == '__main__':
    a = create_certificate()
    for i in a:
        print(i)
    send(a[1])
