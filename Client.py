# -*- coding: utf-8 -*-
# @Time    : 2021/4/19 12:28
# @Author  : AA8j
# @FileName: Client.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/qq_44874645
import random
import sys

from 算法.加密算法.RSA import verify, encrypt
from 算法.加密算法.改造https.DES import des_encrypt
from 算法.加密算法.改造https.sendAndRec import rec, send

# 验证证书
from 算法.加密算法.改造https.sha_224 import sha_224


def verification(certificate):
    # 公钥
    pub_key = certificate[0]
    # 数字签名
    digital_signature_result = certificate[1]
    # 随机数
    num = certificate[2]
    # 摘要生成
    abstract = sha_224(num)
    try:
        if verify(abstract, pub_key, digital_signature_result) == 'SHA-1':
            print('证书验证成功！')
    except Exception as e:
        if 'Verification failed' in e.__str__():
            print('证书验证失败！')
            # 证书验证失败直接退出程序
            sys.exit()


def send_des_key(certificate):  # 生成并发送对称加密密钥
    # 随机生成8位对称加密密钥
    key = str(random.randint(10000000, 100000000))
    pub_key = certificate[0]
    # 将客户端生成的对称加密密钥保存到属于客户端的文件
    with open('client_des_key.txt', 'w') as f:
        f.write(key)
    print('对称密钥生成成功：', key)

    print('正在使用公钥加密密钥...', end='')
    # 公钥加密
    encode = encrypt(key, pub_key)
    print('加密成功：', encode)
    print('正在发送密钥...')
    send(encode)


def main():
    # 模拟接收数据
    certificate = rec()
    print('正在验证证书...')
    verification(certificate)
    send_des_key(certificate)


def send_msg():
    msg = str(input('[客户端]请输入您要发送的信息：'))
    with open('client_des_key.txt', 'r') as f:
        key = f.read()
    msg_encrypt = des_encrypt(msg, key)
    send(msg_encrypt)
    print('发送成功：', msg_encrypt)


if __name__ == '__main__':
    main()
