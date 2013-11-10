#!/usr/bin/python
# -*- coding: utf-8 -*-


from Motion import Motion
from SocketServer import SocketServer


def main():

    motion = Motion()
    socketServer = SocketServer()

    motion.start()
    socketServer.start()

    motion.join()
    socketServer.join()


main()
