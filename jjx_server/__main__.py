#!/usr/bin/python
##-------------------------------##
## Junk Jack X: Server           ##
## Written By: Ryan Smith        ##
##-------------------------------##

## Imports
import logging
import sys
from pathlib import Path

from .player import Player
from .protocol import Client, Server
from .world import World

## Constants
IP: str = "10.0.0.135"
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
# -Run client/server
if len(sys.argv) > 1 and sys.argv[1] in ("-c", "--client"):
    player = Player("Test Debug")
    client = Client(player)
    try:
        client.run(IP, PORT)
    except KeyboardInterrupt:
        client.close()
else:
    #world = World.load(Path("./data/worlds/Tiny-Empty.dat"))
    server = Server()
    try:
        server.run(IP, PORT)
    except KeyboardInterrupt:
        server.close()
