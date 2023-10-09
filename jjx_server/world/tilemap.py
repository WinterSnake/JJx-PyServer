#!/usr/bin/python
##-------------------------------##
## Junk Jack X: World            ##
## Written By: Ryan Smith        ##
##-------------------------------##
## TileMap                       ##
##-------------------------------##

## Imports
from __future__ import annotations

## Constants
__all__: tuple[str] = ("TileMape",)


## Classes
class TileMap:
    """
    JJx World: Tilemap
    """

    # -Constructor
    def __init__(self, size: tuple[int, int]) -> None:
        self.size: tuple[int, int] = size

    # -Dunder Methods
    def __len__(self) -> int:
        return self.width * self.height * 12

    # -Instance Methods
    def resize(self, size: tuple[int, int]) -> bool:
        return False

    def to_bytes(self, compressed: bool = True) -> bytes:
        return b''

    @classmethod
    def from_bytes(cls, compressed: bool = True) -> TileMap:
        return cls((0, 0))

    # -Properties
    @property
    def height(self) -> int:
        return self.size[0]

    @property
    def width(self) -> int:
        return self.size[1]
