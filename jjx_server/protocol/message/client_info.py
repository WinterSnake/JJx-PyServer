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
__all__: tuple[str, str] = ("ClientInfoData", "ClientInfoResponseData")


## Classes
class ClientInfoData(MessageData):
    """
    JJx Message: Client Info
    """

    # -Constructor
    def __init__(self, _id: int, name: str, version: Version) -> None:
        self.player_id: int = _id
        self.player_name: str = name
        self.game_version: Version = version

    # -Dunder Methods
    def __str__(self) -> str:
        return f"ClientInfo {{Id: {self.player_id}, Name: {self.player_name}, Version: {self.game_version.name}}}"

    # -Instance Methods
    def to_bytes(self) -> bytes:
        return (
            self.player_id.to_bytes(1) +
            self.player_name.encode('ascii') +
            b'\0' * (32 - len(self.player_name)) +
            self.game_version.to_bytes(4, byteorder='little')
        )

    # -Class Methods
    @classmethod
    def from_bytes(cls, data: bytes) -> ClientInfoData:
        return cls(
            data[0],  # -Player Id
            data[1: data.find(0x00, 1)].decode('ascii'),  # -Player Name
            Version(int.from_bytes(data[33:], byteorder='little'))  # -Game Version
        )


class ClientInfoResponseData(MessageData):
    """
    JJx Message: Client Info Response
    """

    # -Constructor
    def __init__(self, code: ClientInfoResponseData.Code) -> None:
        self.code: ClientInfoResponseData.Code = code

    # -Dunder Methods
    def __str__(self) -> str:
        return f"Client Info Response: {self.code.name}"

    # -Instance Methods
    def to_bytes(self) -> bytes:
        return self.code.value.to_bytes(2, byteorder='little')

    # -Class Methods
    @classmethod
    def from_bytes(cls, data: bytes) -> ClientInfoResponseData:
        return cls(ClientInfoResponseData.Code(
            int.from_bytes(data, byteorder='little')
        ))

    # -Sub-Classes
    class Code(IntEnum):
        """Client Response Code for connecting to server"""
        Success = 1
