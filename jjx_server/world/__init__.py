#!/usr/bin/python
##-------------------------------##
## Junk Jack X: World            ##
## Written By: Ryan Smith        ##
##-------------------------------##

## Imports
from __future__ import annotations
from pathlib import Path
from typing import cast

from .block import Block
from .blockmap import BlockMap
from .gamemode import Gamemode
from .planet import Planet
from .season import Season
from .size import Size
from .time import Time
from .weather import Weather

## Constants
__all__: tuple[str, ...] = (
    "Block", "BlockMap", "Gamemode", "Planet",
    "Season", "Size", "Time", "Weather", "World"
)


## Classes
class World:
    """
    JJx: World
    """

    # -Constructor
    def __init__(
        self, init_size: Size, sky_size: Size, gamemode: Gamemode,
        planet: Planet, season: Season, time: Time, borders: list[int] | None = None,
        blockmap: BlockMap | None = None, size: list[int] | None = None
    ) -> None:
        self.init_size: Size = init_size
        self.sky_size: Size = sky_size
        self.gamemode: Gamemode = gamemode
        self.planet: Planet = planet
        self.season: Season = season
        self.time: Time = time
        # -Initiate world borders
        _borders = borders if borders else []
        self.borders: list[int] = _borders
        # -Initiate world blocks
        if not blockmap:
            _size = size
            if init_size is not Size.Custom:
                _size = init_size.get_world_size()
            assert _size is not None
            blockmap = BlockMap(_size, None)
        self.blocks: BlockMap = blockmap

    # -Instance Methods
    def save(self, file_path: Path) -> None:
        '''Save world to a file using archiver stream'''
        pass

    # -Class Methods
    @classmethod
    def load(cls, file_path: Path) -> World:
        '''Load file as a world'''
        return World()  # type: ignore

    # -Properties
    @property
    def height(self) -> int:
        return self.blocks._size[0]

    @property
    def size(self) -> tuple[int, int]:
        _size = tuple(self.blocks._size)
        return cast(tuple[int, int], _size)

    @property
    def width(self) -> int:
        return self.blocks._size[0]
