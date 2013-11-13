#!/usr/bin/python
# -*- coding: utf-8 -*-


from Motion import Motion



def main():

    # Init motion detection and socketserver
    motion = Motion()
    socketClient = SocketClient()
    socketServer = SocketServer(motion)

    # Start program
    motion.start()
    socketClient.start()
    socketServer.start()

    # Wait until threads die
    motion.join()
    socketClient.join()
    socketServer.join()

main()
