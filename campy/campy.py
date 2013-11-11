#!/usr/bin/python
# -*- coding: utf-8 -*-


from Motion import Motion
from SocketServer import SocketServer


def main():

    motion = Motion()
    PORT = 50010
    socketServer = SocketServer(motion, PORT)

    motion.start()
    socketServer.start()

    motion.join()
    socketServer.join()


main()
