#!/usr/bin/python
# -*- coding: utf-8 -*-

import time
import RPi.GPIO as GPIO
from SocketClient import SocketClient

class PiButton():
  
  def __init__(self):
    self.HOST = '192.168.10.10'
    self.PORT = 50007
    self.socketClient = SocketClient(self.HOST, self.PORT)

  def start(self):   

    # Use BCM GPIO references
    # instead of physical pin numbers
    GPIO.setmode(GPIO.BCM)

    # Define GPIO to use on Pi
    GPIO_BUTTON = 8

    #print "PIR Module Holding Time Test (CTRL-C to exit)"

    # Set pin as input
    GPIO.setup(GPIO_BUTTON,GPIO.IN)      # Echo
    
    # Input states
    input = 0

    try:

      # Loop until users quits with CTRL-C
      while True :

        input = GPIO.input(GPIO_BUTTON)
        
        if(input):
          time.sleep(0.5)
          print "Button pressed"
        #print "Button pressed"
        #self.socketClient.connectUDP()
        #self.socketClient.send("Button pressed")
        #self.socketClient.close()
        #print "Button press sent!"

        time.sleep(0.01) 

    except KeyboardInterrupt:
      print "  Quit"
      # Reset GPIO settings
      self.clean()

  def clean(self):
    GPIO.cleanup()
