#!/usr/bin/python
##-------------------------------##
## Junk Jack X: Protocol         ##
## Written By: Ryan Smith        ##
##-------------------------------##
## Message: Unknown              ##
##-------------------------------##

## Imports
from __future__ import annotations
import struct

from .base import Message
from ...version import Version


## Classes
class UnknownMessage(Message):
    """
    """

    # -Constructor
    def __init__(self) -> None:
        pass

    def __len__(self) -> int:
        return len(self.to_bytes())

    def __str__(self) -> str:
        return "Unknown"

    # -Instance Methods
    def to_args(self) -> None:
        return None

    def to_bytes(self) -> bytes:
        message = bytearray(0)
        return bytes(message)

    # -Class Methods
    @classmethod
    def from_bytes(cls, data: bytes) -> UnknownMessage:
        return cls()

    # -Class Properties
    opcode = 0x0343
