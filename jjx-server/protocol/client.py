#!/usr/bin/python
##-------------------------------##
## Junk Jack X: Protocol         ##
## Written By: Ryan Smith        ##
##-------------------------------##
## Client                        ##
##-------------------------------##

## Imports
from .connection import Address, Connection
import random

from .message import Message


## Classes
class User:
    """
    JJx: User Session
        Contains client gameplay and communication data
    """

    # -Constructor
    def __init__(self, _id: int, index: int, address: Address) -> None:
        self.id: int = _id
        self._index: int = index
        self.address: Address = address

    # -Properties
    @property
    def index(self) -> int:
        return self._index


class Client(Connection, User):
    """
    JJx: Client
        Contains client logic and protocols to interact with server
    """

    # -Constructor
    def __init__(self, _id: int = 0) -> None:
        Connection.__init__(self)
        if _id == 0:
            _id = random.randint(0x0001, 0xFFFF)
        User.__init__(self, _id, -1, None)  # type: ignore

    # -Instance Methods
    def run(self, ip: str, port: int) -> None:
        '''Run client listener and event handler'''
        self._socket.connect((ip, port))
        self.address = self._socket.getsockname()
        while True:
            message, address = self.recv()
            self._on_message(message, address)

    def on_message(cls, message: Message, address: Address) -> None:
        '''Client message event handler'''
        if address == self.remote_peer:
            print(f"[Server](Size={len(message)}): [{message}]")

    # -Properties
    @property
    def remote_peer(self) -> Address:
        return self._socket.getpeername()
