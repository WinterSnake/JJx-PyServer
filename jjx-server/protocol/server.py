#!/usr/bin/python
##-------------------------------##
## Junk Jack X: Protocol         ##
## Written By: Ryan Smith        ##
##-------------------------------##
## Server                        ##
##-------------------------------##

## Imports
from __future__ import annotations
import logging
import struct

from .connection import Address, Connection
from .client import User
from .message import Message

## Constants
LOGGER = logging.getLogger(__name__)


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
    def has_client(self, address: Address) -> bool:
        '''Check to see if server session contains user address'''
        for client in self._clients:
            if client.address == address:
                return True
        return False

    def on_message(self, message: Message, address: Address) -> None:
        '''Server message event handler'''
        LOGGER.info(f"[Remote](Size={len(message)}): [{message}] | @{address[1]}")
        if not self.has_client(address):
            user = User(
                struct.unpack(">I", message._raw_data[-8:-4])[0],
                len(self._clients),
                address
            )
            self.accept_user_join(user)


    def run(self, ip: str, port: int) -> None:
        '''Run server listener and event handler'''
        self._socket.bind((ip, port))
        while True:
            message, address = self.recv()
            self.on_message(message, address)

    # -Instance Methods: Protocol
    def accept_user_join(self, user: User) -> None:
        '''Accept user join request of client'''
        self._clients.append(user)
        msg = Message.accept(user.id, user.index)
        bytes_written = self.send(msg, user.address)
        LOGGER.info(
            f"[Server](Size={len(msg)}): [{msg}] | "
            f"Sent: {bytes_written} bytes @{user.address[1]}"
        )

    # -Properties
    @property
    def clients(self) -> tuple[User, ...]:
        return tuple(self._clients)
