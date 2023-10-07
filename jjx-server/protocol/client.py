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
from version import Version

## Constants
LOGGER = logging.getLogger(__name__)


## Classes
class User:
    """
    JJx: User Session
        Contains client gameplay and communication data
    """

    # -Constructor
    def __init__(
        self, _id: int, address: Address, index: int, protocol_id: int
    ) -> None:
        self.id: int = _id
        self.address: Address = address
        self._index: int = index
        self._protocol_id: int = protocol_id

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
        User.__init__(self, _id, None, None, None)  # type: ignore
        self._remote_address: Address | None = None
        self.connected: bool = False
        self.name: str = "Test"
        self.version: Version = Version.Latest

    # -Instance Methods
    def close(self) -> None:
        if self.connected:
            self.disconnect()
        Connection.close(self)

    def on_message(self, message: Message, address: Address) -> None:
        '''Client message event handler'''
        if self._index is None:
            self._protocol_id = message._raw_data[0]
            self._index = message._raw_data[9]
            LOGGER.info(f"[Client<Index:{self._index}>] Protocol: 0x{self._protocol_id:0>2X}")
            self._on_accepted()

    def run(self, ip: str, port: int) -> None:
        '''Run client listener and event handler'''
        self.join(ip, port)
        while True:
            message, address = self.recv()
            self.on_message(message, address)

    def _on_accepted(self) -> None:
        ''''''
        self.connected = True
        msg = Message.on_accepted_0(self._protocol_id, self.index)
        self.send(msg, self.remote)
        #self.send_info()
        #msg = Message.on_accepted_1(self._protocol_id, self.index)
        #self.send(msg, self.remote)

    # -Instance Methods: Protocol
    def disconnect(self) -> None:
        '''Send user disconnect message'''
        msg = Message.disconnect(self._protocol_id, self.index)
        self.send(msg, self.remote)
        self.connected = False

    def join(self, ip: str, port: int) -> None:
        '''Send user join request to JJx server'''
        self._remote_address = (ip, port)
        msg = Message.join(self.id)
        self.send(msg, self.remote)
        self.address = self._socket.getsockname()

    def send_info(self) -> None:
        '''Send client name and version'''
        msg = Message.client_info(self._protocol_id, self.index, self.name, self.version)
        self.send(msg, self.remote)

    # -Properties
    @property
    def remote(self) -> Address:
        assert self._remote_address is not None
        return self._remote_address

    # -Class Properties
    origin_name = "Client"
