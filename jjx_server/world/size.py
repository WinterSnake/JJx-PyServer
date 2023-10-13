#!/usr/bin/python
##-------------------------------##
## Junk Jack X: World            ##
## Written By: Ryan Smith        ##
##-------------------------------##
## Sizes                         ##
##-------------------------------##

## Imports
from enum import IntEnum, IntFlag

## Constants
__all__: tuple[str] = ("Size",)


## Classes
class Size(IntEnum):
    """JJx Init Sizes"""

    # -Instance Methods
    def get_world_size(self) -> list[int] | None:
        '''Returns world size in blocks'''
        match self:
            case Size.Tiny:
                return [512, 128]
            case Size.Small:
                return [768, 256]
            case Size.Normal:
                return [1024, 256]
            case Size.Large:
                return [2048, 384]
            case Size.Huge:
                return [4096, 512]
        return None

    # -Class Properties
    Tiny = 0x0
    Small = 0x1
    Normal = 0x2
    Large = 0x3
    Huge = 0x4
    Custom = 0x5
