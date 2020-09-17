import socket

def main():
  # creat Socket
  tcp_serve_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

  # 2. bind ip and port
  tcp_serve_socket.bind(('', 7890))

  # 3. listen
  tcp_serve_socket.listen(128)
  while True:
    print('Waiting Client...')
    # 4. accept message
    new_client_socket,client_addr = tcp_serve_socket.accept()

    # 为同一个客户端服务多次
    while True:
      print('Have Connect...')

      # sccept client request
      recv_data = new_client_socket.recv(1024)

      if recv_data:
        print('accept Msg:',recv_data)
        # accept message
        new_client_socket.send(f'serve has send message,OK, {recv_data}'.encode('utf-8'))
      else:
        break

    # close two socket
    new_client_socket.close()
    print('Serve is Close...')
  tcp_serve_socket.close()


if __name__ == '__main__':
  main()