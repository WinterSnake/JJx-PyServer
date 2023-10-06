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
    """
    Junk Jack X: Client
        Implementation for holding client information and communication for server
    """

    # -Constructor
    def __init__(
        self, _id: int, index: int,
        ip: str, port: int, _socket: socket.socket,
    ) -> None:
        super().__init__(_socket)
        self.id: int = _id
        self.index: int = index
        self.ip: str = ip
        self.port: int = port

    # -Dunder Methods
    def __repr__(self) -> str:
        return "Client(_id={self.id}, _socket={repl(self._socket}, address={self.address})"

    def __str__(self) -> str:
        return f"Player:{self.index} [Id: {self.id:0>4X}, Address: '{self.address[0]}:{self.address[1]}'"

    # -Instance Methods
    def _on_message(self, message: Message) -> None:
        '''Underlying connection message handler'''
        print("[Client] Handling message..")

    def run(self) -> None:
        '''Run client message listener'''
        from threading import Thread

        # -Internal Functions
        def _run(self) -> None:
            while True:
                msg = self.recv_message()[0]
                self._on_message(msg)

        # -Body
        task = Thread(target=_run, args=(self, ))
        task.start()

    def _send_message(self, message: Message) -> None:
        '''Send message to client's given address'''
        super().send_message(message, self.ip, self.port)

    # -Instance Methods: Protocol
    def join(self) -> None:
        '''Broadcast JOIN message to address'''
        msg = Message(Message.Type.Join, player_id=self.id)
        self._send_message(msg)

    # -Class Methods
    @classmethod
    def connect(cls, ip: str, port: int, _id: int = -1) -> Client:
        '''Returns a client for use with connecting to a JJx Server'''
        from random import randint
        if _id < 0:
            _id = randint(0x0001, 0xFFFF)
        return cls(
            _id, -1, ip, port, socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        )

    # -Properties
    @property
    def address(self) -> tuple[str, int]:
        return (self.ip, self.port)
