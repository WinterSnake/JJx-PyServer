#!/usr/bin/python
##-------------------------------##
## Junk Jack X: World            ##
## Written By: Ryan Smith        ##
##-------------------------------##
## Season                        ##
##-------------------------------##

## Imports
from enum import IntFlag

## Constants
__all__: tuple[str] = ("Season",)


## Classes
class Season(IntFlag):
    """JJx Season Flags"""
    Spring = 0x1
    Summer = 0x2
    Autumn = 0x4
    Winter = 0x8
    Null = 0xF
