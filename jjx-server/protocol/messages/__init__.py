#!/usr/bin/python
##-------------------------------##
## Junk Jack X: Message          ##
## Written By: Ryan Smith        ##
##-------------------------------##

## Imports
import struct

from .base import Message
from .clientinfo import ClientInfoMessage

## Constants
__all__: tuple[str, ...] = (
    "ClientInfoMessage",
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
        case _:
            p_data = _bytes_to_hex_string(data)
            raise NotImplementedError(f"Unknown header: {header} | data: {p_data}")
