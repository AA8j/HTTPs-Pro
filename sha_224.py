# -*- coding: utf-8 -*-
# @Time    : 2021/4/19 9:55
# @Author  : AA8j
# @FileName: sha_224.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/qq_44874645
import hashlib


def sha_224(string):
    # 创建sha_224对象
    hl = hashlib.sha224()
    hl.update(bytes(string, encoding='utf-8'))
    sha_224_str = hl.hexdigest()
    return sha_224_str


if __name__ == '__main__':
    print(sha_224('admin'))
