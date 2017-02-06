# coding:utf-8

import socket

# TCP_client
# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# s.connect(('127.0.0.1', 9999))
# print s.recv(1024)
# for data in ['xly', 'xxx', 'wxy']:
#     s.send(data)
#     print s.recv(1024)
# s.send('exit')
# s.close()

# TCP_client practice
# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# s.connect(('127.0.0.1', 9999))
# print s.recv(1024)
# for data in ['xxx', 'xly', 'wxy']:
#     s.send(data)
#     print s.recv(1024)
# s.send('exit')
# s.close()
# -------------------------------------------------------------------------------------------------------------------#
# UDP_client

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
for data in ['xxx', 'xly', 'wxy']:
    s.sendto(data,('127.0.0.1', 9999))
    print s.recv(1024)

s.close()





