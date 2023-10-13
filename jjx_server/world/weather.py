#!/usr/bin/python
##-------------------------------##
## Junk Jack X: World            ##
## Written By: Ryan Smith        ##
##-------------------------------##
## Weather                       ##
##-------------------------------##

## Imports
from __future__ import annotations
from enum import IntFlag

## Constants
__all__: tuple[str] = ("Weather",)


## Classes
class Weather:
    """
    JJx: Weather
    """

    # -Constructor
    def __init__(self, _type: Weather.Type) -> None:
        self.type: Weather.Type = _type

    # -Sub-Classes
    class Type(IntFlag):
        """JJx Weather Type Flags"""
        Clear = 0x0,
        Rain = 0x1,
        Snow = 0x2,
        AcidRain = 0x3,
