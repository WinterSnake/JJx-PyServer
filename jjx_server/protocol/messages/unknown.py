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
    def __init__(
            self,
            world_size: tuple[int, int],
            spawn_position: tuple[int, int],
            player_position: tuple[int, int]
    ) -> None:
        self.world_size: tuple[int, int] = world_size
        self.spawn_position: tuple[int, int] = spawn_position
        self.player_position: tuple[int, int] = player_position

    def __len__(self) -> int:
        return len(self.to_bytes())

    def __str__(self) -> str:
        return "Accept"

    # -Instance Methods
    def to_args(self) -> None:
        return None

    def to_bytes(self) -> bytes:
        message = bytearray(struct.pack(">H", self.opcode))
        message.extend(struct.pack("<HH", *self.world_size))
        message.extend(struct.pack("<HH", *self.spawn_position))
        message.extend(struct.pack("<HH", *self.player_position))
        print(message)
        return bytes(message)

    # -Class Methods
    @classmethod
    def from_bytes(cls, data: bytes) -> UnknownMessage:
        return cls(
            struct.unpack("<HH", data[0:4]),
            struct.unpack("<HH", data[4:8]),
            struct.unpack("<HH", data[8:12]),
        )

    # -Class Properties
    opcode = 0x0343
