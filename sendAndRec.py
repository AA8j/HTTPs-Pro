# -*- coding: utf-8 -*-
# @Time    : 2021/4/19 12:10
# @Author  : AA8j
# @FileName: sendAndRec.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/qq_44874645
def send(send_data):
    print('正在发送数据...', end='')
    with open('send_data.txt', 'w') as f:
        f.write(str(send_data))
    print('发送成功：', send_data)


def rec():
    print('正在接收数据...', end='')
    with open('send_data.txt', 'r') as f:
        data = f.read()
        print('接收成功：', data)
    # 反序列化
    return eval(data)


if __name__ == '__main__':
    Send = 'aaa'
    send(Send)

    Rec = rec()
