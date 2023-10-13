#!/usr/bin/python
##-------------------------------##
## Junk Jack X: World            ##
## Written By: Ryan Smith        ##
##-------------------------------##
## Block                         ##
##-------------------------------##

## Imports
from __future__ import annotations

## Constants
__all__: tuple[str] = ("Block",)


## Classes
class Block:
    """
    JJx: Block
    """

    # -Constructor
    def __init__(self) -> None:
        pass

    # -Dunder Methods

    # -Instance Methods
    def to_bytes(self) -> bytes:
        return b''

    # -Class Methods
    def from_bytes(self, data: bytes) -> Block:
        return Block()
