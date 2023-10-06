#!/usr/bin/python
##-------------------------------##
## Junk Jack X: Server           ##
## Written By: Ryan Smith        ##
##-------------------------------##

## Imports
import logging
import sys

from protocol import Client, Message, Server

## Constants
HOST: str = "10.0.1.21"
PORT: int = 12345
LOGCOUNT: int = 0
LOGPATH: str | None = f"interaction-{LOGCOUNT:0>2}.log"

## Body
logging.basicConfig(filename=LOGPATH, level=logging.INFO, format="%(levelname)s:%(message)s")
if len(sys.argv) > 1 and sys.argv[1] in ("-c", "--client"):
    client = Client()
    try:
        client.run(HOST, PORT)
    except KeyboardInterrupt:
        client.close()
else:
    server = Server("Test")
    print(f"Running server '{server.name}' @ {HOST}:{PORT}")
    try:
        server.run(HOST, PORT)
    except KeyboardInterrupt:
        server.close()
