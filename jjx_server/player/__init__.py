#!/usr/bin/python
##-------------------------------##
## Junk Jack X: Player           ##
## Written By: Ryan Smith        ##
##-------------------------------##

## Imports
from __future__ import annotations
from pathlib import Path

from ..version import Version
from ..world.planet import Planet

## Constants
__all__: tuple[str, ...] = ("Player",)


## Classes
class Player:
    """
    JJx: Player
    """

    # -Constructor
    def __init__(self, name: str, version: Version | None = None) -> None:
        self.name: str = name
        self.version = version if version else Version.Latest

    # -Instance Methods
    def save(self, file_path: Path) -> None:
        '''Save player to a file using archiver stream'''
        pass

    # -Class Methods
    @classmethod
    def load(cls, file_path: Path) -> Player:
        '''Load file as a player'''
        return cls()  # type: ignore
