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

    try:

      print "Button init"

      debugCounter = 0
      # Loop until Button output is 0
      while GPIO.input(GPIO_BUTTON)==1:
        debugCounter += 1
        buttonPressed  = 0
        if(debugCounter == 100000):
          debugCounter = 0
          print "Still in loop"

      # Loop until users quits with CTRL-C
      while True :

        time.sleep(1)
        # Read PIR state
        buttonPressed = GPIO.input(GPIO_BUTTON)
        
        print "Input: " + str(buttonPressed)

        if(buttonPressed == 1):
          # BUTTON is triggered
          print "Button pressed"
          #self.socketClient.connectUDP()
          #self.socketClient.send("Button pressed")
          #self.socketClient.close()
          # Record previous state

    except KeyboardInterrupt:
      print "  Quit"
      # Reset GPIO settings
      self.clean()

  def clean(self):
    GPIO.cleanup()
