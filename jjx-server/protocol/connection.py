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
    def close(self) -> None:
        self._socket.close()

    @abstractmethod
    def _on_message(self, message: Message) -> None:
        ''''''
        pass
