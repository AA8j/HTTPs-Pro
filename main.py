# -*- coding: utf-8 -*-
# @Time    : 2021/4/19 17:36
# @Author  : AA8j
# @FileName: main.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/qq_44874645
from 算法.加密算法.改造https import Server, Client


def main():
    # 服务端生成证书，并向客户端发送
    Server.send_certificate()
    print('-' * 40)
    # 客户端接收证书，并验证
    # 验证成功就向服务端发送用公钥加密的对称密钥，验证失败就退出
    Client.main()
    print('-' * 40)
    # 服务端接收对称密钥，并用私钥解密，得到对称密钥
    Server.rev_key()
    # 客户端向服务端发送信息
    Client.send_msg()
    # 服务端接收消息
    Server.rev_msg()


if __name__ == '__main__':
    main()
