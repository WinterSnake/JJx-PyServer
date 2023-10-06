#!/usr/bin/python
##-------------------------------##
## Junk Jack X: Protocol         ##
## Written By: Ryan Smith        ##
##-------------------------------##
## Message                       ##
##-------------------------------##

## Imports
from __future__ import annotations


## Classes
class Message:
    """
    JJx: Message
        Contains information for communicating between JJx clients and server
    """

    # -Constructor
    def __init__(self, raw_data: bytes) -> None:
        self._raw_data: bytes = raw_data

    # -Dunder Methods
    def __len__(self) -> int:
        return len(self._raw_data)

    def __str__(self) -> str:
        return ", ".join(f"0x{byte:0>2X}" for byte in self._raw_data)

    # -Instance Methods
    def to_bytes(self) -> bytes:
        '''Converts message back to bytes for sending across sockets'''
        message = bytearray()
        message.extend(self._raw_data)
        return bytes(message)

    # -Class Methods
    @classmethod
    def from_bytes(cls, data: bytes) -> Message:
        '''Parses socket byte data to produce a JJx message'''
        return cls(data)
