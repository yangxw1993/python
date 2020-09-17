import socket

def main():
  # creat Socket
  tcp_client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

  # Get serve IP and port
  # dest_ip = input('Please input serve IP:')
  # dest_port = int(input('Please Port:'))
  
  tcp_client_socket.connect(('192.168.31.27', 8088))
  
  # Get file name
  download_file_name = input('Please input file name:')
  
  # send file name to Serve
  tcp_client_socket.send(download_file_name.encode('utf-8'))
  
  # receive data
  recv_data = tcp_client_socket.recv(1024)
  if recv_data:
    print(recv_data)
    # save receive data to file
    with open('新' + download_file_name, 'wb') as f:
      f.write(recv_data)
  
  # close
  tcp_client_socket.close()


if __name__ == '__main__':
  main()