import socket

def tcp_srv():
    # 1,建立socket负责具体的通信,这个socket只是负责连接对方的请求
    # 真正通信的是连接后建立的socket
    # AF_INET 含义与udp一致
    # SOCk_STREAM 表明的是使用tcp进行通信

    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    # 2,绑定端口和ip地址
    # 此地址信息是一个元祖类型内容
    addr = ("127.0.0.1",8888)
    sock.bind(addr)

    # 3,listen(监听)监视接入的访问socket
    sock.listen()

    while True:
        # 4,接受访问socket,乐意理解是建立一个通讯的连接通路
        # accept(接受) 返回的元祖第一个元素赋值给skt,第二个赋值给addr
        skt,addr = sock.accept()
        # 5,接受对方发送的内容,利用接受道德socket接受内容
        # 500代表接受使用的bufforsize(缓冲区大小)
        # msg = skt.receive收到(500)
        msg = skt.recv(500)
        # 接受到的事bytes格式内容
        # 要得到str需要进行转码
        msg = msg.decode()

        rst = "msg:{0} from {1}".format(msg,addr)
        print(rst)
        # 6,如果有必要,给对方发送反馈信息
        skt.send((rst.encode()))
        # 7,关闭链路通路
        skt.close()

if __name__ == '__main__':
    print("Starting tcp server,,,")
    tcp_srv()
    print("Ending tcp server,,,")