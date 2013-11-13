#!/usr/bin/python
# -*- coding: utf-8 -*-


from Motion import Motion
from SocketClient import SocketClient
from SocketServer import SocketServer



def main():

    # Init motion detection and socketserver
    socketClient = SocketClient()
    motion = Motion(socketClient)

    # Start program
    motion.start()
    socketClient.start()
    
    # Wait until threads die
    motion.join()
    socketClient.join()

main()
