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

from .client import Client
from .connection import Connection
from .message import Message


## Classes
class Server(Connection):
    """Junk Jack X Server"""

    # -Constructor
    def __init__(self, max_players: int | None = 4) -> None:
        super().__init__(socket.socket(socket.AF_INET, socket.SOCK_DGRAM))
        self._clients: list[Client] = []

    # -Instance Methods
    def _on_message(self, message: Message) -> None:
        ''''''
        print("[Server] Handling message..")

    def run(self, ip: str, port: int) -> None:
        ''''''
        self._socket.bind((ip, port))
        while True:
            pass

    # -Properties
    @property
    def player_count(self) -> int:
        ''''''
        return len(self._clients)
