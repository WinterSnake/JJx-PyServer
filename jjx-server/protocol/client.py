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
        self._remote_address: Address | None = None

    # -Instance Methods
    def on_message(self, message: Message, address: Address) -> None:
        '''Client message event handler'''
        if address == self.remote:
            print(f"[Server](Size={len(message)}): [{message}]")
        else:
            print(f"[Remote](Size={len(message)}): [{message}]")

    def run(self, ip: str, port: int) -> None:
        '''Run client listener and event handler'''
        self.join(ip, port)
        while True:
            message, address = self.recv()
            self.on_message(message, address)

    # -Instance Methods: Protocol
    def join(self, ip: str, port: int) -> None:
        '''Send join request to JJx server'''
        self._remote_address = (ip, port)
        self.send(Message(b''), self.remote)
        self.address = self._socket.getsockname()

    # -Properties
    @property
    def remote(self) -> Address:
        assert self._remote_address is not None
        return self._remote_address
