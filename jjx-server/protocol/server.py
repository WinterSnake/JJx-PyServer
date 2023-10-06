#!/usr/bin/python
##-------------------------------##
## Junk Jack X: Protocol         ##
## Written By: Ryan Smith        ##
##-------------------------------##
## Server                        ##
##-------------------------------##

## Imports
from __future__ import annotations

from .connection import Address, Connection
from .client import User
from .message import Message


## Classes
class Server(Connection):
    """
    JJx: Server
        Contains server logic and protocols to interact with clients.
        Holds server gameplay data and client communications
    """

    # -Constructor
    def __init__(self, name: str, max_players: int = 4) -> None:
        super().__init__()
        self.name: str = name
        self.max_players: int = max_players
        self._clients: list[User] = []

    # -Instance Methods
    def on_message(self, message: Message, address: Address) -> None:
        '''Server message event handler'''
        print(f"[Remote](Size={len(message)}): [{message}]")

    def run(self, ip: str, port: int) -> None:
        '''Run server listener and event handler'''
        self._socket.bind((ip, port))
        while True:
            message, address = self.recv()
            self.on_message(message, address)

    # -Properties
    @property
    def clients(self) -> tuple[User, ...]:
        return tuple(self._clients)
