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
import socket
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
    def __init__(
        self, name: str, max_players: int = 4
    ) -> None:
        super().__init__()
        self.name: str = name
        self.max_players: int = max_players
        self._clients: list[User] = []
        self._socket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

    # -Instance Methods
    def has_client(self, address: Address) -> bool:
        '''Check to see if server session contains user address'''
        for client in self._clients:
            if client.address == address:
                return True
        return False

    def on_message(self, message: Message, address: Address) -> None:
        '''Server message event handler'''
        if not self.has_client(address):
            user = User(
                struct.unpack(">I", message._raw_data[-8:-4])[0],
                address, 0x80, len(self._clients)
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
        msg = Message.accept(user.id, 3)
        self.send(msg, user.address)

    def broadcast(self) -> None:
        '''Broadcast server to JJx WAN/LAN list'''
        addr = self._socket.getsockname()
        msg = bytearray([0x4A, 0x4A, 0x41, 0x00, 0x00, 0x05])
        msg.extend(socket.inet_aton(addr[0]))  # -IP
        msg.extend(struct.pack("<H", addr[1]))  # -Port
        msg.extend(bytes(self.name[0:15], 'utf-8'))  # -Name
        msg.extend(bytes(28 - len(msg)))
        self._socket.sendto(bytes(msg), ("255.255.255.255", 12346))

    # -Properties
    @property
    def clients(self) -> tuple[User, ...]:
        return tuple(self._clients)

    # -Class Properties
    origin_name = "Server"
