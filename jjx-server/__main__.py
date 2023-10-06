#!/usr/bin/python
##-------------------------------##
## Junk Jack X: Server           ##
## Written By: Ryan Smith        ##
##-------------------------------##

## Imports
import sys
from protocol import Client, Server

## Constants
HOST: str = "10.0.1.21"
PORT: int = 12345

## Body
if len(sys.argv) > 1 and sys.argv[1] in ("-c", "--client"):
    client = Client.connect("10.0.1.21", 12345)
else:
    server = Server()
    print(f"Running server @{HOST}:{PORT}")
    server.run(HOST, PORT)
