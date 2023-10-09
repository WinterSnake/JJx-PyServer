#!/usr/bin/python
##-------------------------------##
## Junk Jack X: World            ##
## Written By: Ryan Smith        ##
##-------------------------------##

## Imports
from __future__ import annotations

from .gamemode import Gamemode
from .sizes import InitSize
from .planet import Planet
from .season import Season
from .time import Time
from .tilemap import TileMap

## Constants
__all__: tuple[str, ...] = (
    "Gamemode", "InitSize", "Planet",
    "Season", "TileMap", "Time", "World"
)


## Classes
class World:
    """
    JJx: World
    """

    # -Constructor
    def __init__(
        self, init_size: InitSize, sky_size: InitSize, size: tuple[int, int],
        spawn: tuple[int, int], player: tuple[int, int], gamemode: Gamemode,
        time: Time, planet: Planet, season: Season, blocks: TileMap,
        language: str | None = "en"
    ) -> None:
        self.init_size: InitSize = init_size
        self.sky_size: InitSize = sky_size
        self._size: tuple[int, int] = size
        self.spawn: tuple[int, int] = spawn
        self.player: tuple[int, int] = player
        self.gamemode: Gamemode = gamemode
        self.time: Time = time
        self.planet: Planet = planet
        self.season: Season = season
        self.blocks: TileMap = blocks
        self.language: str | None = language


    # -Dunder Methods
    def __len__(self) -> int:
        return 0

    # -Instance Methods
    def resize(self, width: int, height: int) -> bool:
        '''Resize world to new dimensions'''
        if self.blocks.resize((width, height)):
            self._size = (width, height)
            return True
        return False

    def to_bytes(self) -> bytes:
        return b''

    # -Class Methods
    @classmethod
    def from_bytes(cls, data: bytes) -> World:
        return cls(
            InitSize.Tiny, InitSize.Tiny, (0, 0), (0, 0), (0, 0),
            Gamemode.Flat, Time(0, Time.Phase.Dusk), Planet.Terra,
            Season.Null, TileMap((0, 0))
        )

    # -Properties
    @property
    def height(self) -> int:
        return 0

    @property
    def size(self) -> tuple[int, int]:
        return self._size

    @property
    def width(self) -> int:
        return 0
