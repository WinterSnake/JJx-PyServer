#!/usr/bin/python
##-------------------------------##
## Junk Jack X: World            ##
## Written By: Ryan Smith        ##
##-------------------------------##
## Block Map                     ##
##-------------------------------##

## Imports
from __future__ import annotations

from .block import Block

## Constants
__all__: tuple[str] = ("BlockMap",)


## Classes
class BlockMap:
    """
    JJx: Block Map
    """

    # -Constructor
    def __init__(
        self, size: list[int], blocks: list[Block] | None = None
    ) -> None:
        self._size: list[int] = size
        # -Initialize blocks
        if not blocks:
            blocks = []
        self._blocks: list[Block] = blocks

    # -Dunder Methods

    # -Instance Methods
    def to_bytes(self, compressed: bool = False) -> bytes:
        return b''

    # -Class Methods
    def from_bytes(
            self, data: bytes, size: tuple[int, int], compressed: bool = True
    ) -> BlockMap:
        ''''''
        return BlockMap(
            [size[0], size[1]], None
        )
