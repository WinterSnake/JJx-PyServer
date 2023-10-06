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
    Junk Jack X: Message
        Parser and builder for communication between client sockets
    """

    # -Constructor
    def __init__(self) -> None:
        pass

    # -Dunder Methods
    def __len__(self) -> int:
        return 1

    def __repr__(self) -> str:
        return ""

    def __str__(self) -> str:
        return ""

    # -Instance Methods
    def to_bytes(self) -> bytes:
        '''Transform message back into bytes for sending across sockets'''
        return bytes([0])

    # -Class Methods
    @classmethod
    def from_bytes(cls, data: bytes) -> Message:
        '''Parse JJx message from bytes'''
        return cls()
