import socket


def serve_client(sk):
    # 接收浏览器发来的请求，http
    request = sk.recv(1024)
    print(request)
    # 发送请求头
    response = 'HTTP/1.1 200 OK \r\n'
    response += '\r\n'
    # 发送请求内容
    response += '<h1>hello world</h1>'
    sk.send(response.encode('utf-8'))

    sk.close()


def main():
    # 创建套接字
    tcp_serve = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    tcp_serve.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    # 绑定
    tcp_serve.bind(('', 8890))
    # 变为监听套接字
    tcp_serve.listen(128)

    while True:
        # 等待客户端链接
        new_socket, client_addr = tcp_serve.accept()
        # 为客户端服务
        serve_client(new_socket)

    tcp_serve.close()

if __name__ == '__main__':
    main()