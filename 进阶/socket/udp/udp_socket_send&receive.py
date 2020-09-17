import socket

# 发送数据
def sendMsg(udp_socket):
  """"send Msg"""
  send_data = input('Please input need send msg:')
  dest_ip = input('Please IP:')
  dest_port = input('Please input Port:')
  udp_socket.sendto(send_data.encode('utf-8'), (dest_ip, int(dest_port)))

def receive_msg(udp_socket):
  """" receive Msg """
  recv_data = udp_socket.recvfrom(1024)
  print(f'{str(recv_data[1])}: {recv_data[0].decode("utf-8")}')

def main():
  # 创建一个udp
  udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
  # 绑定信息
  udp_socket.bind(('', 8888))

  while True:
    print('-------udp 聊天器--------')
    print('1:发送消息')
    print('2:接收消息')
    print('0:退出系统')
    print('-------udp 聊天器--------')
    op = input('请输入功能：')
    if op == '1':
      sendMsg(udp_socket)
    elif op == '2':
      receive_msg(udp_socket)
    elif op == '0':
      break
    else:
      print('输入有误，请重新输入...')

  # send Msg
  # udp_socket.sendto(b'Hello Socket',('192.168.31.27', 8888))

  # 接收数据
  # localAddr = ('127.0.0.1', 8801)
  # udp_socket.bind(localAddr)
  receive_data = udp_socket.recvfrom(1024)
  print(receive_data)
  # 关闭
  udp_socket.close()


if __name__ == '__main__':
  main()
