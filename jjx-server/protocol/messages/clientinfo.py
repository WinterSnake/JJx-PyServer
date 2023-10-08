#!/usr/bin/python
##-------------------------------##
## Junk Jack X: Protocol         ##
## Written By: Ryan Smith        ##
##-------------------------------##
## Message: Client Info          ##
##-------------------------------##

## Imports
from __future__ import annotations
import struct
from typing import Any

from .base import Message
from ...version import Version


## Classes
class ClientInfoMessage(Message):
    """
    """

    # -Constructor
    def __init__(self, name: str, version: Version) -> None:
        self.name: str = name
        self.version: Version = version

    def __len__(self) -> int:
        return len(self.to_bytes())

    def __str__(self) -> str:
        return f"Player: {self.name}, Version: {self.version}"

    # -Instance Methods
    def to_args(self) -> tuple[str, Version]:
        return (self.name, self.version)

    def to_bytes(self) -> bytes:
        message = bytearray(struct.pack(">HB", ClientInfoMessage.opcode, 0x9f))
        name = bytearray(self.name.encode('ascii'))
        name.extend(bytearray(32 - len(name)))
        message.extend(name)
        assert isinstance(self.version.value, int)  # -mypy complains about tuple[int]
        message.extend(self.version.value.to_bytes(4, byteorder='little'))
        return bytes(message)

    # -Class Methods
    @classmethod
    def from_bytes(cls, data: bytes) -> ClientInfoMessage:
        return cls(
            data[1:data.find(0x00)].decode('ascii'),
            Version(int.from_bytes(data[33:], byteorder='little', signed=False))
        )

    # -Class Properties
    opcode = 0x0002
