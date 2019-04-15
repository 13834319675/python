# 客户端
'''
client端流程
1, 建立通信socket
2, 发送内容到指定服务器
3, 接受服务器给定的反馈内容
'''
import socket

def clientFunc():
    sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    # 给服务器发送
    text = "i love china"

    # 发送的娥数据必须用bytes格式
    data = text.encode()

    # 发送 然后等待
    sock.sendto(data,("127.0.0.1",7852))

    # 服务器反馈的内容
    data,addr = sock.recvfrom(500)
    data = data.decode()
    print(data)
    print(addr)
if __name__ == '__main__':
    clientFunc()