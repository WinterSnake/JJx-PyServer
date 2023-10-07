#!/usr/bin/python
##-------------------------------##
## Junk Jack X: Protocol         ##
## Written By: Ryan Smith        ##
##-------------------------------##
## Message                       ##
##-------------------------------##

## Imports
from __future__ import annotations
from enum import Enum
import struct

from .chunk import Chunk


## Classes
class Message:
    """
    JJx: Message
        Contains information for communicating between JJx clients and server
    """

    # -Constructor
    def __init__(self, raw_data: bytes, tick: int = 0) -> None:
        self.tick: int = tick
        self._chunks: list[Chunk] = []
        self._raw_data: bytes = raw_data

    # -Dunder Methods
    def __len__(self) -> int:
        return len(self._raw_data)

    def __repr__(self) -> str:
        return ""

    def __str__(self) -> str:
        return ", ".join(f"0x{byte:0>2X}" for byte in self._raw_data)

    # -Instance Methods
    def to_bytes(self) -> bytes:
        '''Converts message back to bytes for sending across sockets'''
        message = bytearray()
        message.extend(self._raw_data)
        return bytes(message)

    # -Class Methods
    @classmethod
    def from_bytes(cls, data: bytes) -> Message:
        '''Parses socket byte data to produce a JJx message'''
        return cls(data)

    # -Client
    @classmethod
    def disconnect(cls, player_index: int, tick: int = 0) -> Message:
        ''''''
        ticks = struct.pack(">H", tick)
        raw_data = bytes([
            0x80, player_index, ticks[0], ticks[1],
            0x84, 0xFF, 0x00, 0x04,
            0x00, 0x00, 0x00, 0x00
        ])
        return cls(raw_data)

    @classmethod
    def join(cls, player_id: int, tick: int = 0) -> Message:
        ''''''
        _id = struct.pack(">I", player_id)
        raw_data = bytes([
            0x8F, 0xFF, 0x00, 0x00,
            0x82, 0x00, 0x00, 0x00,
            0x00, 0x00, 0x00, 0x00,
            0x00, 0x00, 0x00, 0x00,
            0x00, 0x00, 0x00, 0x00,
            0x00, 0x00, 0x00, 0x01,
            0x00, 0x00, 0x00, 0x00,
            0x00, 0x00, 0x00, 0x00,
            0x00, 0x00, 0x13, 0x88,
            0x00, 0x00, 0x00, 0x02,
            0x00, 0x00, 0x00, 0x02,
            _id[0], _id[1], _id[2], _id[3],
            0x00, 0x00, 0x00, 0x00
        ])
        return cls(raw_data)

    # -Server
    @classmethod
    def accept(cls, player_id: int, player_index: int, tick: int = 0) -> Message:
        ''''''
        _id = struct.pack(">I", player_id)
        raw_data = bytes([
            0x80, 0x00, 0x00, 0x00,
            0x83, 0x00, 0x00, 0x00,
            0x00, player_index, 0x00, 0x00,
            0x00, 0x00, 0x00, 0x00,
            0x00, 0x00, 0x00, 0x00,
            0x00, 0x00, 0x00, 0x01,
            0x00, 0x00, 0x00, 0x00,
            0x00, 0x00, 0x00, 0x00,
            0x00, 0x00, 0x13, 0x88,
            0x00, 0x00, 0x00, 0x02,
            0x00, 0x00, 0x00, 0x02,
            _id[0], _id[1], _id[2], _id[3],
        ])
        return cls(raw_data)

