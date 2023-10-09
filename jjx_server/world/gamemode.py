#!/usr/bin/python
##-------------------------------##
## Junk Jack X: World            ##
## Written By: Ryan Smith        ##
##-------------------------------##
## Gamemode                      ##
##-------------------------------##

## Imports
from enum import IntEnum

## Constants
__all__: tuple[str] = ("Gamemode",)


## Classes
class Gamemode(IntEnum):
    """JJx Gamemodes"""
    Survival = 0x0
    Creative = 0x1
    Flat = 0x2
    Adventure = 0x3
