#!/usr/bin/python
# -*- coding: utf-8 -*-

import socket
import time


def main():
    
    HOST = '192.168.10.10'
    PORT = 50666



    while(True):
        time.sleep(3)
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect((HOST, PORT))
        s.send('PiAlive')
        s.close()


main()

