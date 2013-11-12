#!/usr/bin/python
# -*- coding: utf-8 -*-


from Motion import Motion
from SocketServer import SocketServer


def main():

    # Init motion detection and socketserver
    motion = Motion()
    PORT = 50010
    socketServer = SocketServer(motion, PORT)

    # Start program
    motion.start()
    socketServer.start()

    # Wait until threads die
    motion.join()
    socketServer.join()


main()
