#!/usr/bin/python
# -*- coding: utf-8 -*-

import socket
import threading
import sys
import time

class SocketServer(threading.Thread):

    def __init__(self, motion, PORT):
        # Init motion
        self.motion = motion

        # Threading init
        threading.Thread.__init__(self)
        self.setName = "SocketServer"
        self.daemon = True

        # Init socket
        self.HOST = ''
        self.PORT = PORT
        self.sock = None
        self.client = None
        self.clientAddr = None

    def run(self):
        self.listenToSocket()

    def clean(self):
        if(self.sock != None):
            self.sock.close()
            self.sock = None
        if(self.client != None):
            self.client.close()
            self.client = None
        
    # Listens to the socket for client connections
    def listenToSocket(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            self.sock.bind((self.HOST, self.PORT))
            self.sock.listen(1)
        except socket.error, msg:
            self.clean()
            sys.exit(1)

        while(True):
            self.client, self.clientAddr = self.sock.accept()
            clientData = self.client.recv(1024)
            time.sleep(1)
            serverData = self.handleClientData(clientData)
            self.client.send(serverData)
            self.client.close()
            self.client = None

            
    # Handles Client messages
    def handleClientData(self, clientData):
        
        if(clientData == "Request Camera Info"):
            return self.fetchCameraInfo()
        else:
            return "Unknown message"

    # Fetching motion detection information
    def fetchCameraInfo(self):
        matrix = self.motion.matrix

        output = ""
        dataCount = 0

        # Fetch any motion detected
        for x in xrange(self.motion.matrixSize):
            for y in xrange(self.motion.matrixSize):
                if(matrix[x][y] > 0):
                    dataCount = dataCount + 1
                    output = output + str(x) + ", " + str(y) + ", " + str(matrix[x][y]) + "\n"
        
        if(dataCount > 0):
            output = dataCount + "\n" + output
        else:
            output = dataCount + "\n"
        
        return output
