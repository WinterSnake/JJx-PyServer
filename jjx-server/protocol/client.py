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

from .connection import Connection
from .message import Message


## Classes
class Client(Connection):
    """Junk Jack X Client"""

    # -Constructor
    def __init__(self, _id: int, index: int, _socket: socket.socket) -> None:
        super().__init__(_socket)
        self.id: int = _id
        self.index: int = index

    # -Instance Methods
    def _on_message(self, message: Message) -> None:
        ''''''
        print("[Client] Handling message..")

    # -Class Methods
    @classmethod
    def connect(cls, _id: int) -> Client:
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        client = cls(_id, -1, sock)
        return client
