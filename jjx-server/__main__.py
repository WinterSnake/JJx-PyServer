#!/usr/bin/python
##-------------------------------##
## Junk Jack X: Server           ##
## Written By: Ryan Smith        ##
##-------------------------------##

## Imports
import sys

from protocol import Client, Message, Server

## Constants
HOST: str = "10.0.1.21"
PORT: int = 12345

## Body
if len(sys.argv) > 1 and sys.argv[1] in ("-c", "--client"):
    client = Client()
    client.run(HOST, PORT)
else:
    server = Server("Test")
    print(f"Running server '{server.name}' @ {HOST}:{PORT}")
    server.run(HOST, PORT)
