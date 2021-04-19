# -*- coding: utf-8 -*-
# @Time    : 2021/4/19 9:16
# @Author  : AA8j
# @FileName: Server.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/qq_44874645
import time

from 算法.加密算法.改造https.DES import des_decrypt
from 算法.加密算法.改造https.RSA import decrypt
from 算法.加密算法.改造https.createCertificate import create_certificate
from 算法.加密算法.改造https.sendAndRec import send, rec


def send_certificate():
    # 将生成的私钥和证书提取
    prv_key_and_certificate = create_certificate()
    prv_key = prv_key_and_certificate[0]
    certificate = prv_key_and_certificate[1]
    # 模拟发送数据
    send(certificate)

    # 将私钥保存
    with open('prv_key.txt', 'w') as f:
        f.write(prv_key)


def rev_key():  # 接收密钥
    print('正在接收密钥...')
    key = rec()
    print('对称密钥接收成功：', key)
    print('正在利用私钥解密...')
    # 读取私钥
    with open('prv_key.txt', 'r') as f:
        prv_key = f.read()
        print(prv_key)
    key = decrypt(key, prv_key)
    print('对称密钥解密成功：', key)
    # 将接收的客户端生成的对称加密密钥保存到属于客户端的文件
    with open('server_des_key.txt', 'w') as f:
        f.write(key)


def rev_msg():
    with open('server_des_key.txt', 'r') as f:
        key = f.read()
    msg = rec()
    msg_decrypt = des_decrypt(msg, key)
    print('解密成功：', msg_decrypt.decode())


if __name__ == '__main__':
    # send_certificate()
    rev_key()
