# -*- coding:utf-8 -*-
__author__ = 'walkskyer'
"""
"""

import socket

#target_address = "www.baidu.com"
#target_port = 80

target_address = "127.0.0.1"
target_port = 9999

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect((target_address, target_port))

client.send("GET / HTTP/1.1\r\nHost: www.baidu.com\r\n\r\n")

response = client.recv(4096)

print "[*] Received: %s" % response

if __name__ == "__main__":
    pass