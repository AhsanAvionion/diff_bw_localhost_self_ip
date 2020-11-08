#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Nov  8 22:27:08 2020

@author: engineer
"""

import socket

#IP='localhost'  # if udp_tx app is sending data to 'localhost' / '127.0.0.1' then this receiver gets data by binding this IP
# 'localhost' and '127.0.0.1' are samethings
PORT=8888

IP='192.168.1.28'  # if udp_tx app is sending data to '192.168.1.28' then this receiver gets data by binding this IP

socketUDP = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # Create socket
socketUDP.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  #If previously bind socket was not closed properly reuse it
socketUDP.bind((IP, PORT))
payload_size=500
while True :
    data = socketUDP.recv(payload_size)
    print data
