#!/usr/bin/python
# -*- coding: utf-8 -*-

import time
import RPi.GPIO as GPIO
from SocketClient import SocketClient

class Pir():
  
  def __init__(self):
    self.HOST = ''
    self.PORT = 50007
    self.socketClient = SocketClient(self.HOST, self.PORT)

  def start(self):   

    # Use BCM GPIO references
    # instead of physical pin numbers
    GPIO.setmode(GPIO.BCM)

    # Define GPIO to use on Pi
    GPIO_PIR = 7

    print "PIR Module Holding Time Test (CTRL-C to exit)"

    # Set pin as input
    GPIO.setup(GPIO_PIR,GPIO.IN)      # Echo

    Current_State  = 0
    Previous_State = 0

    try:

      print "Waiting for PIR to settle ..."

      # Loop until PIR output is 0
      while GPIO.input(GPIO_PIR)==1:
        Current_State  = 0

      print "  Ready"

      data = 0
      # Loop until users quits with CTRL-C
      while True :

        time.sleep(3)
        # Read PIR state
        Current_State = GPIO.input(GPIO_PIR)

        if Current_State==1 and Previous_State==0:
          # PIR is triggered
          print "  Motion detected!"
          self.socketClient.connectTCP()
          self.socketClient.send("Motion")
          time.sleep(1)
          data = self.socketClient.recieve()
          print "Recieved ", data
          self.close()
          # Record previous state
          Previous_State=1
        elif Current_State==0 and Previous_State==1:
          # PIR has returned to ready state
          self.socketClient.connectTCP()
          self.socketClient.send("Motionless")
          time.sleep(1)          
          data = self.socketClient.recieve()
          print "Recieved ", data
          self.close()
          Previous_State=0

    except KeyboardInterrupt:
      print "  Quit"
      # Reset GPIO settings
      self.clean()

  def clean(self):
    GPIO.cleanup()
