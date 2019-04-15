# socket模块负责socket编程

import socket

def serverFunc():
    # 建立socket
    sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

    # 绑定ip和端口哦
    addr = ("127.0.0.1",7852)
    sock.bind(addr)

    # 等待接受客户端消息
    data,addr = sock.recvfrom(500)

    print(data)
    # 转换为str根式

    text = data.decode()
    print(text)

    # 反馈的内容
    rsp = "这是服务器反馈的内容"
    data = rsp.encode()
    sock.sendto(data,addr)

if __name__ == '__main__':
    import time
    while True:
        try:
            serverFunc()
        except Exception as e:
            print(e)

        time.sleep(1)
