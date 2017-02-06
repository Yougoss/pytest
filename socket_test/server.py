# coding:utf-8

import socket
import threading
import time


# TCP_server
# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)   # 创建基于ipv4和TCP的socket对象
# s.bind(('127.0.0.1', 9999))   # 绑定监听的地址和端口
# s.listen(5)     # 监听端口,并设定最大连接数
#
#
# def tcplink(sock, addr):
#     print 'Accept new connection from %s:%s ' % addr + 'in Thread %s' % threading.current_thread().name
#     sock.send('Welcome')
#     while True:
#         data = sock.recv(1024)
#         time.sleep(1)
#         if data == 'exit' or not data:
#             break
#         sock.send('Hello,%s!' % data)
#     sock.close()
#     print 'Connection from %s:%s closed' % addr
#
# while True:
#     sock, addr = s.accept()     # accept返回一个客户端的连接
#     t = threading.Thread(target=tcplink, args=(sock, addr))
#     t.start()

# TCP_server practice
# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# s.bind(('127.0.0.1', 9999))
# s.listen(5)
#
#
# def tcplink(sock, addr):
#     print 'Accept new connection from %s:%s' % addr
#     sock.send('Welcome!')
#     while True:
#         data = sock.recv(1024)
#         if data == 'exit' or not data:
#             break
#         sock.send('Helle,%s' % data)
#         time.sleep(1)
#     sock.close()
#     print 'Connection from %s:%s closed' % addr
#
# while True:
#     cliet_sock, client_addr = s.accept()
#     t = threading.Thread(target=tcplink, args=(cliet_sock, client_addr))
#     t.start()


# -------------------------------------------------------------------------------------------------------------------#
# UDP_server

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(('127.0.0.1', 9999))
while True:
    data, addr = s.recvfrom(1024)
    print 'Received from %s:%s' % addr
    s.sendto('Hello, %s!' % data, addr)





