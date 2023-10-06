#!/usr/bin/python
##-------------------------------##
## Junk Jack X: Protocol         ##
## Written By: Ryan Smith        ##
##-------------------------------##
## Connection                    ##
##-------------------------------##

## Imports
import socket
from abc import ABC, abstractmethod

from .message import Message


## Classes
class Connection(ABC):
    """Junk Jack X Connection"""

    # -Constructor
    def __init__(self, _socket: socket.socket) -> None:
        self._socket: socket.socket = _socket

    # -Instance Methods
    @abstractmethod
    def _on_message(self, message: Message) -> None:
        '''Underlying connection message handler'''

    def close(self) -> None:
        self._socket.close()

    @abstractmethod
    def run(self) -> None:
        '''Connection runner implementation'''

    def send_message(self, message: Message, ip: str, port: int) -> None:
        '''Send message to specified address'''
        bytes_written: int = self._socket.sendto(message.to_bytes(), (ip, port))
        print(f"Message: {message} | Written: {bytes_written} | Expected: {len(message)}")
