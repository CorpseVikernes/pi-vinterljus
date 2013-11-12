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
    GPIO_BUTTON = 6

    #print "PIR Module Holding Time Test (CTRL-C to exit)"

    # Set pin as input
    GPIO.setup(GPIO_BUTTON,GPIO.IN)      # Echo

    Current_State  = 0
    Previous_State = 0

    try:

      print "Button init"

      # Loop until PIR output is 0
      while GPIO.input(GPIO_BUTTON)==1:
        Current_State  = 0

      # Loop until users quits with CTRL-C
      while True :

        time.sleep(1)
        # Read PIR state
        Current_State = GPIO.input(GPIO_BUTTON)

        if Current_State==1 and Previous_State==0:
          # BUTTON is triggered
          print "Button pressed"
          #self.socketClient.connectUDP()
          #self.socketClient.send("Button pressed")
          #self.socketClient.close()
          # Record previous state
          Previous_State=1
        elif Current_State==0 and Previous_State==1:
          Previous_State=0

    except KeyboardInterrupt:
      print "  Quit"
      # Reset GPIO settings
      self.clean()

  def clean(self):
    GPIO.cleanup()
