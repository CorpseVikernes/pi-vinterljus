#!/usr/bin/python
# -*- coding: utf-8 -*-


from Motion import Motion



def main():

    # Init motion detection and socketserver
    socketClient = SocketClient()
    motion = Motion(socketClient)
    
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
