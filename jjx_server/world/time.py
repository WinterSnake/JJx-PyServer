#!/usr/bin/python
##-------------------------------##
## Junk Jack X: World            ##
## Written By: Ryan Smith        ##
##-------------------------------##
## Time                          ##
##-------------------------------##

## Imports
from enum import IntFlag

## Constants
__all__: tuple[str] = ("Time",)


## Classes
class Time:
    """
    JJx: Time
    """

    # -Constructor
    def __init__(self, tick: int, phase: Time.Phase) -> None:
        self.tick: int = tick
        self.phase: Time.Phase = phase

    # -Sub-Classes
    class Phase(IntFlag):
        """JJx Time Phase Flags"""
        Day = 0x1,
        Dusk = 0x2,
        Night = 0x4,
        Dawn = 0x8,
