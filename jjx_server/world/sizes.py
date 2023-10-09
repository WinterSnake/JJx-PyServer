#!/usr/bin/python
##-------------------------------##
## Junk Jack X: World            ##
## Written By: Ryan Smith        ##
##-------------------------------##
## Sizes                         ##
##-------------------------------##

## Imports
from enum import IntEnum

## Constants
__all__: tuple[str] = ("InitSize",)


## Classes
class InitSize(IntEnum):
    """JJx Init Sizes"""
    Tiny = 0x0  # -Size:  512 * 128
    Small = 0x1  # -Size:  768 * 256
    Normal = 0x2  # -Size: 1024 * 256
    Large = 0x3  # -Size: 2048 * 384
    Huge = 0x4  # -Size: 4096 * 512
    Custom = 0x5
