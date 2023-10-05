#!/usr/bin/python
##-------------------------------##
## Junk Jack X: Server           ##
## Written By: Ryan Smith        ##
##-------------------------------##
## Server                        ##
##-------------------------------##

## Imports
from __future__ import annotations
import socket

## Constants


## Functions


## Classes
class Server:
    """Junk Jack X Server"""

    # -Constructor
    def __init__(self, max_players: int = 4) -> None:
        self._socket: socket.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self._users: list[User] = []

    # -Dunder Methods

    # -Instance Methods
    def close(self) -> None:
        ''''''
        print("Closing socket..")
        self._socket.close()

    def run(self, ip: str, port: int) -> None:
        ''''''
        self._socket.bind((ip, port))
        while True:
            pass

    # -Class Methods

    # -Static Methods

    # -Properties

    # -Class Properties
