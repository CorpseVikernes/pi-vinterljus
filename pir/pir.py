#!/usr/bin/python
# -*- coding: utf-8 -*-


from Pir import Pir

def main():

    # Setup PIR PINS
    PIR1 = 7
    PIR2 = 9
    PIR3 = 11

    # Init PIRS
    pir1 = Pir(PIR1)
    pir2 = Pir(PIR2)
    pir3 = Pir(PIR3)

    # Start detection
    pir1.start()
    pir2.start()
    pir3.start()

    # Wait until threads die
    pir1.join()
    pir2.join()
    pir3.join()

main()
