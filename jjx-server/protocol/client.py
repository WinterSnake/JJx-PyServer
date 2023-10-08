#!/usr/bin/python
##-------------------------------##
## Junk Jack X: Protocol         ##
## Written By: Ryan Smith        ##
##-------------------------------##
## Client                        ##
##-------------------------------##

## Imports
from enet import Address, Host, Peer  # type: ignore

from .connection import Connection


## Classes
class Client(Connection):
    """
    JJx: Client Connection
    """

    # -Constructor
    def __init__(self) -> None:
        super().__init__(Host(None, 1, 0, 0))

    # -Instance Methods
    def close(self) -> None:
        pass

    def run(self, ip: str, port: int) -> None:
        ''''''
        pass

    # -Instance Methods: API
    def on_connected(self, peer: Peer) -> None:
        pass

    def on_disconnected(self, peer: Peer) -> None:
        pass
