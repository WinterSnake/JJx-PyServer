#!/usr/bin/python
##-------------------------------##
## Junk Jack X: Protocol         ##
## Written By: Ryan Smith        ##
##-------------------------------##
## Message                       ##
##-------------------------------##

## Imports
from __future__ import annotations
import struct
from enum import Enum, auto


## Classes
class Message:
    """
    Junk Jack X: Message
        Parser and builder for communication between client sockets
    """

    # -Constructor
    def __init__(
        self, _type: Message.Type, *,
        player_id: int | None = None, raw_data: bytes | None = None
    ) -> None:
        self.type: Message.Type = _type
        self.tick: int = 0
        self.player_id: int | None = player_id
        self._raw_data: bytes | None = raw_data

    # -Dunder Methods
    def __len__(self) -> int:
        return len(self.to_bytes())

    def __repr__(self) -> str:
        return '[' + ", ".join(f"0x{byte:0>2X}" for byte in self._raw_data) + ']'

    def __str__(self) -> str:
        return f"{self.type.name}"

    # -Instance Methods
    def to_bytes(self) -> bytes:
        '''Transform message back into bytes for sending across sockets'''
        ticks = self.tick_bits
        match self.type:
            case Message.Type.Unknown:
                return self._raw_data
            case Message.Type.Join:
                _id = self.player_id_bits
                return bytes([
                    0x8F, 0xFF, ticks[0], ticks[1],
                    0x82, 0xFF, 0x00, 0x01,
                    0x00, 0x00, 0xFF, 0xFF,
                    0x00, 0x00, 0x05, 0x78,
                    0x00, 0x00, 0x10, 0x00,
                    0x00, 0x00, 0x00, 0x02,
                    0x00, 0x09, 0xC4, 0x00,
                    0x00, 0x01, 0xF4, 0x00,
                    0x00, 0x00, 0x13, 0x88,
                    0x00, 0x00, 0x00, 0x02,
                    0x00, 0x00, 0x00, 0x02,
                    _id[0], _id[1], _id[2], _id[3],
                    0x00, 0x00, 0x00, 0x00
                ])

    # -Class Methods
    @classmethod
    def from_bytes(cls, data: bytes) -> Message:
        '''Parse JJx message from bytes'''
        return cls(Message.Type.Unknown, raw_data=data)

    # -Properties
    @property
    def player_id_bits(self) -> bytes:
        '''Gets packed player id if applicable'''
        assert self.player_id is not None
        return struct.pack(">I", self.player_id)

    @property
    def tick_bits(self) -> bytes:
        '''Gets packed tick'''
        return struct.pack(">H", self.tick)

    # -Sub-Classes
    class Type(Enum):
        """Message Type"""
        Unknown = auto()
        Join = auto()
