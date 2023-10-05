#!/usr/bin/python
##-------------------------------##
## Junk Jack X: Server           ##
## Written By: Ryan Smith        ##
##-------------------------------##
## Client                        ##
##-------------------------------##

## Imports
from __future__ import annotations
import socket

## Constants


## Functions


## Classes
class Client:
    """Junk Jack X Client"""

    # -Constructor
    def __init__(self, _id: int) -> None:
        self.id: int = _id
        self._player_index: int | None = None
        self._socket: socket.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # -Dunder Methods

    # -Instance Methods
    def run(self, ip: str, port: int) -> None:
        ''''''
        while True:
            pass

    # -Class Methods

    # -Static Methods

    # -Properties
    @property
    def player_index(self) -> int:
        assert self._player_index != None
        return self._player_index


## Body
if __name__ == "__main__":
    pass
