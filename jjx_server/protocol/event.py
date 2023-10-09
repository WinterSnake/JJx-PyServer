#!/usr/bin/python
##-------------------------------##
## Junk Jack X: Protocol         ##
## Written By: Ryan Smith        ##
##-------------------------------##
## Event Handler                 ##
##-------------------------------##

## Imports
from collections.abc import Callable
from typing import Protocol, overload, runtime_checkable

from enet import Peer  # type: ignore

from ..version import Version
from ..world import World


## Classes
@runtime_checkable
class EventHandler(Protocol):

    # -Dunder Methods
    @overload
    def __call__(self, peer: Peer) -> None: ...
    @overload
    def __call__(self, code: int, peer: Peer) -> None: ...
    @overload
    def __call__(self, name: str, version: Version, peer: Peer) -> None: ...
    @overload
    def __call__(self, world: World, peer: Peer) -> None: ...

    # -Properties
    __name__: str
