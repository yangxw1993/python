import socket
import threading


def recv_msg(udp_so):
    """ 接收数据 """
    while True:
        rec_data = udp_so.recvfrom(1024)
        print('recv Msg',rec_data)


def send_msg(udp_so, dest_ip, dest_port):
    """"send msg"""
    while True:
        send_data = input('send msg:')
        udp_so.sendto(send_data.encode('utf-8'), (dest_ip, dest_port))


def main():
    """" udp 聊天器"""
    udp_so = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    #   bind
    udp_so.bind(('', 7890))
    #     get he ip
    dest_ip = input('pleas IP：')
    dest_port = int(input('please port:'))

    t_recv = threading.Thread(target=recv_msg, args=(udp_so,))
    t_send = threading.Thread(target=send_msg, args=(udp_so, dest_ip, dest_port))

    t_recv.start()
    t_send.start()

if __name__ == '__main__':
    main()