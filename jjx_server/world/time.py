#!/usr/bin/python
##-------------------------------##
## Junk Jack X: World            ##
## Written By: Ryan Smith        ##
##-------------------------------##
## Time                          ##
##-------------------------------##

## Imports
from __future__ import annotations
from enum import IntFlag, auto

## Constants
__all__: tuple[str] = ("Time",)


## Classes
class Time:
    """
    JJx: World Time
    """

    # -Constructor
    def __init__(self, ticks: int, phase: Time.Phase) -> None:
        self.ticks: int = ticks
        self.phase: Time.Phase = phase

    # -Dunder Methods
    def __str__(self) -> str:
        return f"[{self.phase.name}]{self.ticks}"

    # -Sub-Classes
    class Phase(IntFlag):
        """JJx Time Phase"""
        Null = 0x0,
        Day = 0x1,
        Dusk = 0x2,
        Night = 0x4,
        Dawn = 0x8,
