#!/usr/bin/python
##-------------------------------##
## Junk Jack X: Message          ##
## Written By: Ryan Smith        ##
##-------------------------------##

## Imports
import logging
import struct

from .base import Message
from .accept import AcceptMessage
from .clientinfo import ClientInfoMessage
from .worlddata import WorldDataMessage
from .worldinfo import WorldInfoMessage
from .worldinforequest import WorldInfoRequestMessage
from .unknown import Unknown1Message

## Constants
__all__: tuple[str, ...] = (
    "AcceptMessage", "ClientInfoMessage",
    "parse",
)
LOGGER = logging.getLogger(__name__)


## Functions
def _bytes_to_hex_string(data: bytes) -> str:
    """Returns bytes to a comma separated hex string"""
    return '[' + ", ".join(f"0x{byte:0>2X}" for byte in data) + ']'


def parse(data: bytes) -> Message:
    """Parse a JJx packet into the correct message class"""
    header = struct.unpack(">H", data[0:2])[0]
    data = data[2:]
    match header:
        case ClientInfoMessage.opcode:  # -0x0002
            return ClientInfoMessage.from_bytes(data)
        case AcceptMessage.opcode:  # -0x0003
            return AcceptMessage.from_bytes(data)
        case WorldInfoRequestMessage.opcode:  # -0x0009
            return WorldInfoRequestMessage.from_bytes(data)
        case WorldInfoMessage.opcode:  # -0x0343
            return WorldInfoMessage.from_bytes(data)
        case WorldDataMessage.opcode:  # -0x0347
            return WorldDataMessage.from_bytes(data)
        case _:
            p_data = _bytes_to_hex_string(data)
            LOGGER.error(f"Unknown header: {header:0>4X} | data: {p_data} | len: {len(data)}")
            return None  # type: ignore
