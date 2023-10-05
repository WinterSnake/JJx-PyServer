#!/usr/bin/python
##-------------------------------##
## Junk Jack X: Protocol         ##
## Written By: Ryan Smith        ##
##-------------------------------##
## Message                       ##
##-------------------------------##

## Imports
from __future__ import annotations


## Classes
class Message:
    """"""

    # -Constructor
    def __init__(self) -> None:
        pass

    # -Class Methods
    @classmethod
    def from_bytes(cls, data: bytes) -> Message:
        ''''''
        return cls()
