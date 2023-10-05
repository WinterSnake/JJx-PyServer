#!/usr/bin/python
##-------------------------------##
## Junk Jack X: Server           ##
## Written By: Ryan Smith        ##
##-------------------------------##
## Script Name                   ##
##-------------------------------##

## Imports
import sys
from server import Server

## Constants
HOST: str = "10.0.1.21"
PORT: int = 12345

## Body
server = Server()
try:
    server.run(HOST, PORT)
except KeyboardInterrupt as e:
    server.close()
