#!/usr/bin/python
##-------------------------------##
## Junk Jack X: Message          ##
## Written By: Ryan Smith        ##
##-------------------------------##
## Data                          ##
##-------------------------------##

## Imports
from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Type

## Constants
__all__: tuple[str] = ("MessageData",)


## Classes
class MessageData(ABC):
    """
    JJx Message: Data
    """

    # -Constructor
    def __init__(self) -> None: ...

    # -Instance Methods
    @abstractmethod
    def to_bytes(self) -> bytes: ...

    # -Class Methods
    @classmethod
    @abstractmethod
    def from_bytes(cls, data: bytes) -> MessageData: ...
