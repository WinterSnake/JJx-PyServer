#!/usr/bin/python
##-------------------------------##
## Junk Jack X: Protocol         ##
## Written By: Ryan Smith        ##
##-------------------------------##
## Connection                    ##
##-------------------------------##

## Imports
import logging
import socket
from abc import ABC, abstractmethod
from typing import ClassVar

from .message import Message

## Constants
Address = tuple[str, int]
LOGGER = logging.getLogger(__name__)


## Classes
class Connection(ABC):
    """
    JJx: Base Connection
        Holds the socket and methods to interact between clients and server
    """

    # -Constructor
    def __init__(self) -> None:
        self._socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # -Instance Methods
    def close(self) -> None:
        self._socket.close()

    @abstractmethod
    def on_message(self, message: Message, address: Address) -> None:
        '''Connection message event handler'''
        pass

    def recv(self, buffer: int = 1024) -> tuple[Message, Address]:
        '''Returns parsed JJx message and address of peer'''
        msg, address = self._socket.recvfrom(buffer)
        message = Message.from_bytes(msg)
        LOGGER.debug(f"[Remote](Size={len(message):>3}): [{message}] | @{address}")
        return (message, address)

    @abstractmethod
    def run(self, ip: str, port: int) -> None:
        '''Runs connection's listener and event handler'''
        pass

    def send(self, message: Message, address: Address) -> int:
        '''Send JJx message to peer address'''
        bytes_written = self._socket.sendto(message.to_bytes(), address)
        LOGGER.debug(
                f"[{self.origin_name}](Size={len(message):>3}): [{message}] "
            f"| Sent {bytes_written} bytes @{address}"
        )
        return bytes_written

    # -Class Properties
    origin_name: ClassVar[str]
