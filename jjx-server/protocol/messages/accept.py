#!/usr/bin/python
##-------------------------------##
## Junk Jack X: Protocol         ##
## Written By: Ryan Smith        ##
##-------------------------------##
## Message: Accept               ##
##-------------------------------##

## Imports
from __future__ import annotations
import struct
from typing import Any

from .base import Message
from ...version import Version


## Classes
# -Possible SuccessMessage
# - where Code=1 = server accepted
class AcceptMessage(Message):
    """
    """

    # -Constructor
    def __init__(self, code: int) -> None:
        self.code: int = code

    def __len__(self) -> int:
        return len(self.to_bytes())

    def __str__(self) -> str:
        return f"Accept({self.code})"

    # -Instance Methods
    def to_args(self) -> tuple[int]:
        return (self.code,)

    def to_bytes(self) -> bytes:
        message = bytearray(struct.pack(">H", self.opcode))
        message.extend(self.code.to_bytes(2, byteorder='little'))
        return bytes(message)

    # -Class Methods
    @classmethod
    def from_bytes(cls, data: bytes) -> AcceptMessage:
        return cls(
            int.from_bytes(data, byteorder='little')
        )

    # -Class Properties
    opcode = 0x0003
