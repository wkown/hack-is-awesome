# -*- coding:utf-8 -*-
__author__ = 'walkskyer'
"""
"""
import socket
import threading

bind_ip = "0.0.0.0"
bind_port = 9999

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind((bind_ip, bind_port))
#server.listen(5)

def handle_client(client_data, client_addr):
    global server
    print "[*] Accepted connection from %s:%s" % (client_addr[0], client_addr[1])
    print "[*] Received: %s" % client_data

    server.sendto("EEFFGGHH", client_addr)

while True:
    print "[*] Waiting for you..."

    data, addr = server.recvfrom(4096)
    handle = threading.Thread(target=handle_client, args=(data, addr))
    handle.start()

server.close()