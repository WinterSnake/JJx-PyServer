#!/usr/bin/python
##-------------------------------##
## Junk Jack X: Protocol         ##
## Written By: Ryan Smith        ##
##-------------------------------##
## Client                        ##
##-------------------------------##

## Imports
import logging
import random

from .connection import Address, Connection
from .message import Message


## Constants
LOGGER = logging.getLogger(__name__)


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

    # -Dunder Methods
    def __str__(self) -> str:
        return f"User[{self.index}]: 0x{self.id:0>8X} @ {self.address}"

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
            _id = random.randint(0x00000001, 0xFFFFFFFF)
        User.__init__(self, _id, -1, None)  # type: ignore
        self._remote_address: Address | None = None

    # -Instance Methods
    def on_message(self, message: Message, address: Address) -> None:
        '''Client message event handler'''
        log_string = f"(Size={len(message)}): [{message}]"
        if address == self.remote:
            log_string = "[Server]" + log_string
        else:
            log_string = "[Remote]" + log_string
        LOGGER.info(log_string)

    def run(self, ip: str, port: int) -> None:
        '''Run client listener and event handler'''
        self.join(ip, port)
        while True:
            message, address = self.recv()
            self.on_message(message, address)

    # -Instance Methods: Protocol
    def join(self, ip: str, port: int) -> None:
        '''Send user join request to JJx server'''
        self._remote_address = (ip, port)
        msg = Message.join(self.id)
        bytes_written = self.send(msg, self.remote)
        self.address = self._socket.getsockname()
        LOGGER.info(f"[Client](Size={len(msg)}): [{msg}] | Sent: {bytes_written} bytes @{self.address[1]}")

    # -Properties
    @property
    def remote(self) -> Address:
        assert self._remote_address is not None
        return self._remote_address
