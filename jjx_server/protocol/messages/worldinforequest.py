#!/usr/bin/python
##-------------------------------##
## Junk Jack X: Protocol         ##
## Written By: Ryan Smith        ##
##-------------------------------##
## Message: World Info Request   ##
##-------------------------------##

## Imports
from __future__ import annotations
import struct

from .base import Message


## Classes
class WorldInfoRequestMessage(Message):
    """
    JJx Message: World Info Request
    """

    # -Constructor
    def __init__(self) -> None:
        pass

    def __len__(self) -> int:
        return len(self.to_bytes())

    def __str__(self) -> str:
        return "WorldInfoRequest"

    # -Instance Methods
    def to_args(self) -> None:
        return None

    def to_bytes(self) -> bytes:
        message = bytearray(struct.pack(">H", self.opcode))
        message.extend(0x0000.to_bytes(2, byteorder='big'))
        return bytes(message)

    # -Class Methods
    @classmethod
    def from_bytes(cls, data: bytes) -> WorldInfoRequestMessage:
        return cls()

    # -Class Properties
    opcode = 0x0009
