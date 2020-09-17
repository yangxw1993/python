import socket

def main():
  # creat Socket
  tcp_serve_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

  # 2. bind ip and port
  tcp_serve_socket.bind(('', 8888))

  # 3. listen
  tcp_serve_socket.listen(128)

  print('Waiting...')
  # 4. accept message
  new_client_socket,client_addr = tcp_serve_socket.accept()
  print('Waited')

  # sccept client request
  recv_data = new_client_socket.recv(1024)
  print('accept Msg:',recv_data)

  # accept message
  new_client_socket.send(f'serve has send message,OK, {recv_data}'.encode('utf-8'))

  # close two socket
  new_client_socket.close()
  tcp_serve_socket.close()






if __name__ == '__main__':
  main()