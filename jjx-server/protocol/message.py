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
import socket

from .chunk import Chunk
from version import Version


## Classes
class Message:
    """
    JJx: Message
        Contains information for communicating between JJx clients and server
    """

    # -Constructor
    def __init__(self, raw_data: bytes, tick: int | None = None) -> None:
        self.tick: int | None = tick
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
    def disconnect(cls, protocol_id: int, player_index: int, tick: int = 0) -> Message:
        ''''''
        raw_data = bytes([
            protocol_id, player_index, 0x00, 0x00,
            0x84, 0xFF, 0x00, 0x04,
            0x00, 0x00, 0x00, 0x00
        ])
        return cls(raw_data, tick)

    @classmethod
    def join(cls, player_id: int, tick: int = 0) -> Message:
        ''''''
        _id = struct.pack(">I", player_id)
        raw_data = bytes([
            0x8F, 0xFF, 0x00, 0x00,
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
        return cls(raw_data, tick)

    @classmethod
    def on_accepted_0(cls, protocol_id: int, player_index: int, tick: int = 0) -> Message:
        ''''''
        raw_data = bytes([
            protocol_id, player_index, 0x00, 0x00,
            0x01, 0xFF, 0x00, 0x01,
            0x00, 0x01, 0x00, 0x00,
            0x85, 0xFF, 0x00, 0x02
        ])
        return cls(raw_data, tick)

    @classmethod
    def on_accepted_1(cls, protocol_id: int, player_index: int, tick: int = 0) -> Message:
        ''''''
        raw_data = bytes([
            protocol_id, player_index, 0x00, 0x00,
            0x85, 0xFF, 0x00, 0x02
        ])
        return cls(raw_data, tick)

    @classmethod
    def client_info(
        cls, protocol_id: int, player_index: int,
        name: str, version: Version, tick: int = 0
    ) -> Message:
        data = bytearray([
            protocol_id, player_index, 0x00, 0x00,
            0x86, 0x00, 0x00, 0x01,
            0x00, 0x27, 0x00, 0x02,
            0xC2
        ])
        _name = bytearray(bytes(name, 'utf-8'))
        _name.extend(bytes(32 - len(_name)))
        data += _name
        data.extend(struct.pack("<I", version))
        return cls(bytes(data), tick)

    # -Server
    @classmethod
    def accept(cls, player_id: int, player_index: int, tick: int = 0) -> Message:
        ''''''
        _id = struct.pack(">I", player_id)
        raw_data = bytes([
            0x80, 0x00, 0x00, 0x00,
            0x83, 0xFF, 0x00, 0x01,
            0x00, player_index, 0x00, 0x00,
            0x00, 0x00, 0x05, 0x78,
            0x00, 0x00, 0x10, 0x00,
            0x00, 0x00, 0x00, 0x02,
            0x00, 0x00, 0x00, 0x00,
            0x00, 0x00, 0x00, 0x00,
            0x00, 0x00, 0x13, 0x88,
            0x00, 0x00, 0x00, 0x02,
            0x00, 0x00, 0x00, 0x02,
            _id[0], _id[1], _id[2], _id[3],
        ])
        return cls(raw_data, tick)

    @classmethod
    def broadcast(cls, ip: str, port: int, name: str) -> Message:
        msg = bytearray([0x4A, 0x4A, 0x41, 0x00, 0x00, 0x05])
        msg.extend(socket.inet_aton(ip))  # -IP
        msg.extend(struct.pack("<H", port))  # -Port
        msg.extend(bytes(name, 'utf-8'))  # -Name
        msg.extend(bytes(28 - len(msg)))
        return cls(bytes(msg))
