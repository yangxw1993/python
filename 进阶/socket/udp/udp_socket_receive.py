import socket

def main():
  udp_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
  # 不指定ip，空字符串代表自身Ip
  localAddr = ('', 8801)
  udp_socket.bind(localAddr)
  while True:
    # 最大接受值
    receive_data = udp_socket.recvfrom(1024)
    receive_msg = receive_data[0].decode('gbk')
    print(receive_msg)
  udp_socket.close()

if __name__ == '__main__':
  main()