# -*- coding:utf-8 -*-
__author__ = 'walkskyer'
"""
"""
import socket
import threading

bind_ip = "0.0.0.0"
bind_port = 9999

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((bind_ip, bind_port))
server.listen(5)

def handle_client(client_socket, client_addr):
    print "[*] Accepted connection from %s:%s" % (client_addr[0], client_addr[1])

    request = client_socket.recv(4096)

    print "[*] Received: %s" % request

    client_socket.send("ACK!")
    client_socket.close()

while True:
    print "[*] Waiting connection"
    client, addr = server.accept()

    handle = threading.Thread(target=handle_client, args=(client,addr))
    handle.start()
