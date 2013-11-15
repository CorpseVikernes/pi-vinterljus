#!/usr/bin/python
# -*- coding: utf-8 -*-


from Motion import Motion
from SocketClient import SocketClient
from SocketServer import SocketServer
from Capture import Capture


def main():

    # Init motion detection and socketserver
    #socketClient = SocketClient()
    #motion = Motion(socketClient)
    capture = Capture()

    # Start program
    #motion.start()
    #socketClient.start()
    capture.start()
    
    # Wait until threads die
    #motion.join()
    #socketClient.join()
    capture.join()

main()
