import socket

# 发送数据
def main():
  # 创建一个udp
  udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
  while True:
    sendMsg = input('请输入需要发送的数据：')

    if sendMsg == 'exit':
      break
    # send Msg
    # udp_socket.sendto(b'Hello Socket',('192.168.31.27', 8888))
    udp_socket.sendto(sendMsg.encode('utf-8'),('192.168.31.27', 8888))
  # 关闭
  udp_socket.close()


if __name__ == '__main__':
  main()
