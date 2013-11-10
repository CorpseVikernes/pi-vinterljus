#!/usr/bin/python
# -*- coding: utf-8 -*-

import socket

class SocketClient:

    def __init__(self, HOST, PORT):
        # Init socket
        self.HOST = HOST
        self.PORT = PORT
        self.sock = None

    def connectUDP(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock.connect((self.HOST, self.PORT))


    def connectTCP(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            self.sock.connect((self.HOST, self.PORT))
        except socket.error, msg:
            self.close()

    def send(self, msg):
        self.sock.send(msg + '\n') #ADD end sign

    def close(self):
        if(self.sock != None):
            self.sock.close()
            self.sock = None

    def recieve(self):
        return self.sock.recv(1024)
