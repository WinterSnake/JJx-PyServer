#!/usr/bin/python
##-------------------------------##
## Junk Jack X: Message          ##
## Written By: Ryan Smith        ##
##-------------------------------##
## Client Info Data              ##
##-------------------------------##

## Imports
from __future__ import annotations
from enum import IntEnum

from .message_data import MessageData

## Constants
__all__: tuple[str, str] = ("WorldInfoData", "WorldInfoRequestData")


## Classes
class WorldInfoData(MessageData):
    """
    JJx Message: World Info
    """

    # -Constructor
    def __init__(self) -> None:
        pass

    # -Dunder Methods
    def __str__(self) -> str:
        return "WorldInfo"

    # -Instance Methods
    def to_bytes(self) -> bytes:
        return b''

    # -Class Methods
    @classmethod
    def from_bytes(cls, data: bytes) -> WorldInfoData:
        return cls()


class WorldInfoRequestData(MessageData):
    """
    JJx Message: World Info Request
    """

    # -Constructor
    def __init__(self) -> None:
        pass

    # -Dunder Methods
    def __str__(self) -> str:
        return "World Info Request"

    # -Instance Methods
    def to_bytes(self) -> bytes:
        return bytes(2)

    # -Class Methods
    @classmethod
    def from_bytes(cls, data: bytes) -> WorldInfoRequestData:
        return cls()
