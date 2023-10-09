#!/usr/bin/python
##-------------------------------##
## Junk Jack X: Protocol         ##
## Written By: Ryan Smith        ##
##-------------------------------##
## Message: Client Info          ##
##-------------------------------##

## Imports
from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any, ClassVar, Type


## Classes
class Message:
    """
    JJx: Base Message Interop
    """

    # -Constructor
    def __init__(self) -> None:
        pass

    # -Instance Methods
    @abstractmethod
    def to_args(self) -> tuple[Any, ...] | None: ...

    @abstractmethod
    def to_bytes(self) -> bytes: ...

    # -Class Methods
    @classmethod
    @abstractmethod
    def from_bytes(cls: Type[Message], data: bytes) -> Message: ...

    # -Class Properties
    opcode: ClassVar[int]
