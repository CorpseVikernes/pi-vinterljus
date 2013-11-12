#!/usr/bin/python
# -*- coding: utf-8 -*-

import socket
import time


def main():
    
    HOST = '192.168.10.10'
    PORT = 50666

    alive = "PiAlive "
    command = /opt/vc/bin/vcgencmd measure_temp

    while(True):
        time.sleep(3)
        cpuTemp = (subprocess.check_output(command, shell=True))
        msg = alive + cpuTemp
        print msg
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect((HOST, PORT))
        s.send(msg)
        s.close()


main()

