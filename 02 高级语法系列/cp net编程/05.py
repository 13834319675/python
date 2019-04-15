import socket

def tcp_clt():
    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    addr = ("127.0.0.1",8888)
    # 链接对方 请求建立链接通路
    sock.connect(addr)

    msg = "I Love China"
    # 发送内容到服务器
    sock.send(msg.encode())

    # 接受对方的反馈
    rst = sock.recv(500)
    print(rst.decode())
    # 关闭链接通路
    sock.close()

if __name__ == '__main__':
    tcp_clt()