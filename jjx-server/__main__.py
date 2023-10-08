#!/usr/bin/python
##-------------------------------##
## Junk Jack X: Server           ##
## Written By: Ryan Smith        ##
##-------------------------------##

## Imports
import logging
import sys
from pathlib import Path

from .protocol import Client, Server
from .version import Version

## Constants
HOST: str = "10.0.0.135"
PORT: int = 12345
USE_LOGGING: bool = True
LOGCOUNT: int = 0
LOGPATH: Path | None = None

## Body
# -Configure logging
while USE_LOGGING:
    LOGPATH = Path(f"logs/interaction-{LOGCOUNT:0>2}.log")
    if not LOGPATH.is_file():
        break
    LOGCOUNT += 1
logging.basicConfig(filename=LOGPATH, level=logging.DEBUG, format="[%(levelname)s]%(message)s")
# -Run client
if len(sys.argv) > 1 and sys.argv[1] in ("-c", "--client"):
    client = Client("Test Debug")
    try:
        client.run(HOST, PORT)
    except KeyboardInterrupt:
        client.close()
# -Run server
else:
    server = Server("Example Server")
    print(f"Running server '{server.name}' @ {HOST}:{PORT}")
    try:
        server.run(HOST, PORT)
    except KeyboardInterrupt:
        server.close()
