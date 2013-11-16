#!/usr/bin/python
# -*- coding: utf-8 -*-

import socket
import threading

class SocketClient(threading.Thread):

    def __init__(self):

        # Threading init
        threading.Thread.__init__(self)
        self.setName = "SocketClient"
        self.daemon = True

        self.matrix = 0
        self.matrixSize = 0

        # Init socket
        self.HOST = '192.168.10.10'
        self.PORT = 50010
        self.sock = None

    def run(self):
        pass

    def connectUDP(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock.connect((self.HOST, self.PORT))

    def connectTCP(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((self.HOST, self.PORT))

    def send(self, msg):
        self.sock.send(msg + '\n') #ADD end sign

    def close(self):
        if(self.sock != None):
            self.sock.close()
            self.sock = None

    def recieve(self):
        return self.sock.recv(1024)

    def sendMatrix(self, matrix):
        self.matrix = matrix
        msg = ""

        # for x in xrange(self.matrixSize):
        #     for y in xrange(self.matrixSize):
        #         msg += "," + str(x) + "," + str(y) + "," + str(self.matrix[x][y])

        #Send only sides
        for x in xrange(self.matrixSize):
            msg += "," + str(0) + "," + str(x) + "," + str(self.matrix[0][x])
            msg += "," + str(self.matrixSize-1) + "," + str(x) + "," + str(self.matrix[self.matrixSize-1][x])

       
        msg = msg[1:]
        #print msg
        self.connectTCP()
        self.send(msg)
        self.close()


