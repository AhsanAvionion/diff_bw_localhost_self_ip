#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Nov  8 22:27:08 2020

@author: engineer
"""
import socket
import time

#IP='localhost'     # this ip was assigned by my router, it caused no internet usage / this data did not left the device and could be monitered on 'System Monitor' Utility
# 'localhost' and '127.0.0.1' are samethings
IP='192.168.1.28'    # this ip was assigned to my laptop by my router, it caused no internet usage / this data did not left the laptop and could be monitered on 'System Monitor' Utility


#IP='www.google.com'    # it caused internet usage / this data left the laptop and could be monitered on 'System Monitor' Utility
#IP='64.233.160.100'    # ip of google it caused internet usage / this data left the laptop and could be monitered on 'System Monitor' Utility
#IP='192.168.1.130'    # this ip does not exit in my local network (checked with fing android application) so no data was left my laptop

PORT=8888


socketUDP = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # Create socket
payload1='STARTofPkt The quick brown fox jumps over the lazy dog,The quick brown fox jumps over the lazy dog,The quick brown fox jumps over the lazy dog,ENDofPKT'
while True :
    socketUDP.sendto(payload1, (IP, PORT))
    time.sleep(0.001)   # data sent at 180kbytes per sec with payload1 and sleep(0.001)

