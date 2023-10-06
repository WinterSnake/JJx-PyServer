#!/usr/bin/python
##-------------------------------##
## Junk Jack X: Protocol         ##
## Written By: Ryan Smith        ##
##-------------------------------##
## Message Chunk                 ##
##-------------------------------##

## Imports
from __future__ import annotations
from enum import Enum
import struct


## Classes
class Chunk:
    """
    JJx: Message Chunk
    """

    # -Constructors
    def __init__(self, _type: Chunk.Type) -> None:
        self.type: Chunk.Type = _type

    # -Dunder Methods
    def __len__(self) -> int:
        return 0

    def __repr__(self) -> str:
        return ""

    def __str__(self) -> str:
        return ""

    # -Instance Methods
    def to_bytes(self) -> bytes:
        chunk = bytearray()
        return bytes(chunk)

    # -Sub-Classes
    class Type(Enum):
        """
        Message Chunk Type
        """
