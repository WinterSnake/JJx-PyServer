#!/usr/bin/python
##-------------------------------##
## Junk Jack X: Message          ##
## Written By: Ryan Smith        ##
##-------------------------------##

## Imports
import struct

from .base import Message
from .accept import AcceptMessage
from .clientinfo import ClientInfoMessage
from .worldinfo import WorldInfoMessage
from .worldinforequest import WorldInfoRequestMessage
from .unknown import UnknownMessage

## Constants
__all__: tuple[str, ...] = (
    "AcceptMessage", "ClientInfoMessage",
    "parse",
)


## Functions
def _bytes_to_hex_string(data: bytes) -> str:
    """Returns bytes to a comma separated hex string"""
    return '[' + ", ".join(f"0x{byte:0>2X}" for byte in data) + ']'


def parse(data: bytes) -> Message:
    """Parse a JJx packet into the correct message class"""
    header = struct.unpack(">H", data[0:2])[0]
    data = data[2:]
    match header:
        case ClientInfoMessage.opcode:
            return ClientInfoMessage.from_bytes(data)
        case AcceptMessage.opcode:
            return AcceptMessage.from_bytes(data)
        case WorldInfoMessage.opcode:
            return WorldInfoMessage.from_bytes(data)
        case WorldInfoRequestMessage.opcode:
            return WorldInfoRequestMessage.from_bytes(data)
        case UnknownMessage.opcode:
            return UnknownMessage.from_bytes(data)
        case _:
            p_data = _bytes_to_hex_string(data)
            raise NotImplementedError(f"Unknown header: {header:0>4X} | data: {p_data}")
