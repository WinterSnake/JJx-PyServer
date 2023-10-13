#!/usr/bin/python
##-------------------------------##
## Junk Jack X: Message          ##
## Written By: Ryan Smith        ##
##-------------------------------##

## Imports
from __future__ import annotations
from enum import IntEnum

from .message_data import MessageData
from .client_info import ClientInfoData
from ...version import Version

## Constants
__all__: tuple[str] = ("Message",)


## Classes
class Message:
    """
    JJx: Message
    """

    # -Constructor
    def __init__(
            self, _type: Message.Type,
            subtype: Message.SubType, data: MessageData
    ) -> None:
        self.type: Message.Type = _type
        self.subtype: Message.SubType = subtype
        self.data: MessageData = data

    # -Dunder Methods
    def __str__(self) -> str:
        return f"{self.type.name}:{self.subtype.name} || Data: [{self.data}]"

    # -Instance Methods
    def to_bytes(self) -> bytes:
        '''Returns message as bytes to be sent through enet packet'''
        message = bytearray([self.type.value, self.subtype.value])
        message.extend(self.data.to_bytes())
        return bytes(message)

    # -Class Methods
    @classmethod
    def from_bytes(cls, data: bytes) -> Message:
        '''Parses enet packet data and returns a valid JJx Message'''
        _type = Message.Type(data[0])
        subtype = Message.SubType(data[1])
        # -Create appropriate data class
        msg_data: MessageData
        match subtype:
            case Message.SubType.ClientInfo:
                msg_data = ClientInfoData.from_bytes(data[2:])
        return cls(_type, subtype, msg_data)

    @classmethod
    def client_info(cls, _id: int, name: str, version: Version) -> Message:
        '''Create a client info message to send across socket'''
        return cls(
            Message.Type.Management, Message.SubType.ClientInfo,
            ClientInfoData(_id, name, version)
        )

    # -Sub-Classes
    class Type(IntEnum):
        '''JJx Packet Master Type'''
        Management = 0x00

    class SubType(IntEnum):
        '''JJx Packet Subtype'''
        ClientInfo = 0x02
