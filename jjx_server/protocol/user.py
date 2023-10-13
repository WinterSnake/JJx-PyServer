#!/usr/bin/python
##-------------------------------##
## Junk Jack X: Protocol         ##
## Written By: Ryan Smith        ##
##-------------------------------##
## User                          ##
##-------------------------------##

## Imports
from ..player import Player


## Constants
__all__: tuple[str] = ("User",)


## Classes
class User:
    """
    JJx: User
    """

    # -Constructor
    def __init__(self, _id: int, character: Player) -> None:
        self.id: int = _id
        self.character: Player = character
