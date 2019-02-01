# -*- coding:utf-8 -*-
__author__ = 'walkskyer'
"""
udp client demo
"""
import socket

target_ip = "127.0.0.1"
target_port = 9999

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

client.settimeout(5)

client.sendto("AABBCCDD", (target_ip, target_port))

data, addr = client.recvfrom(4096)

print "[*] Received data: %s" % data

if __name__ == "__main__":
    pass