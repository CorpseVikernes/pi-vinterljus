#!/usr/bin/python
# -*- coding: utf-8 -*-

import time
import RPi.GPIO as GPIO
from SocketClient import SocketClient

class Pir():
  
  def __init__(self):
    self.HOST = '192.168.10.10'
    self.PORT = 50007
    self.socketClient = SocketClient(self.HOST, self.PORT)

  def start(self):   

    # Use BCM GPIO references
    # instead of physical pin numbers
    GPIO.setmode(GPIO.BCM)

    # Define GPIO to use on Pi
    GPIO_PIR = 7

    #print "PIR Module Holding Time Test (CTRL-C to exit)"

    # Set pin as input
    GPIO.setup(GPIO_PIR,GPIO.IN)      # Echo

    Current_State  = 0
    Previous_State = 0

    try:

      #print "Waiting for PIR to settle ..."

      # Loop until PIR output is 0
      while GPIO.input(GPIO_PIR)==1:
        Current_State  = 0

      #print "  Ready"

      data = 0
      # Loop until users quits with CTRL-C
      while True :

        time.sleep(0.01)
        # Read PIR state
        Current_State = GPIO.input(GPIO_PIR)

        if Current_State==1 and Previous_State==0:
          # PIR is triggered
          print "  Motion detected!"
          self.socketClient.connectUDP()
          self.socketClient.send("Motion")
          #print "motion sent"
          #data = self.socketClient.recieve()
          #time.sleep(1)
          #print "Recieved ", data
          self.socketClient.close()
          # Record previous state
          time.sleep(1)
          Previous_State=1
        elif Current_State==0 and Previous_State==1:
          time.sleep(1)
          Previous_State=0

    except KeyboardInterrupt:
      print "  Quit"
      # Reset GPIO settings
      self.clean()

  def clean(self):
    GPIO.cleanup()
