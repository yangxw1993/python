import socket


def main(name):
  """" TCP Client Demo """
  # creat Socket
  tcp_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

  # 2.connect serve
  serve_ip = input('Please serve IP:')
  serve_port = int(input('Please input serve port:'))
  serve_addr = (serve_ip, serve_port)
  tcp_client.connect(serve_addr)

  # 3. send message
  send_msg = input('Please send message:')
  tcp_client.send(send_msg.encode('utf-8'))

  # 4.close cocket
  tcp_client.close()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
  main('PyCharm')
