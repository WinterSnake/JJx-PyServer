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
from ...version import Version

## Constants
__all__: tuple[str, str] = ("ClientInfoResponseCode", "ClientInfoResponseData")


## Classes
class ClientInfoResponseCode(IntEnum):
    """Client Response Code for connecting to server"""
    Success = 1


class ClientInfoResponseData(MessageData):
    """
    JJx Message: Client Response
    """

    # -Constructor
    def __init__(self, code: ClientInfoResponseCode) -> None:
        self.code: ClientInfoResponseCode = code

    # -Dunder Methods
    def __str__(self) -> str:
        return f"Response: {self.code.name}"

    # -Instance Methods
    def to_bytes(self) -> bytes:
        return self.code.value.to_bytes(2, byteorder='little')

    # -Class Methods
    @classmethod
    def from_bytes(cls, data: bytes) -> ClientInfoResponseData:
        return cls(ClientInfoResponseCode(
            int.from_bytes(data, byteorder='little')
        ))
