import socket


# 发送数据
def main():
  # 创建一个udp
  udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
  dest_ip = input('请输入对方ip:')
  dest_port = input('请输入对方端口:')

  sendMsg = input('请输入需要发送的数据：')

  # send Msg
  # udp_socket.sendto(b'Hello Socket',('192.168.31.27', 8888))
  udp_socket.sendto(sendMsg.encode('utf-8'), (dest_ip, int(dest_port)))

  # 接收数据
  # localAddr = ('127.0.0.1', 8801)
  # udp_socket.bind(localAddr)
  receive_data = udp_socket.recvfrom(1024)
  print(receive_data)
  # 关闭
  udp_socket.close()


if __name__ == '__main__':
  main()
