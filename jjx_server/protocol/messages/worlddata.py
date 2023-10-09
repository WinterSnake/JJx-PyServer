#!/usr/bin/python
##-------------------------------##
## Junk Jack X: Protocol         ##
## Written By: Ryan Smith        ##
##-------------------------------##
## Message: World Data           ##
##-------------------------------##

## Imports
from __future__ import annotations
import struct
from typing import cast

from .base import Message
from ...world import (
    Gamemode, InitSize, Planet, Season, TileMap, Time, World
)


## Classes
class WorldDataMessage(Message):
    """
    JJx Message: World Data
    """

    # -Constructor
    def __init__(self, data: bytes) -> None:
        self.world_data: bytes = data

    def __len__(self) -> int:
        return len(self.to_bytes())

    def __str__(self) -> str:
        return "WorldData"

    # -Instance Methods
    def to_args(self) -> tuple[bytes]:
        return (self.world_data,)


    def to_bytes(self) -> bytes:
        return self.world_data

    # -Class Methods
    @classmethod
    def from_bytes(cls, data: bytes) -> WorldDataMessage:
        return cls(data)

    # -Class Properties
    opcode = 0x0347
