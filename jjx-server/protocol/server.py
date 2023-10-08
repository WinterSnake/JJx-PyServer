#!/usr/bin/python
##-------------------------------##
## Junk Jack X: Protocol         ##
## Written By: Ryan Smith        ##
##-------------------------------##
## Server                        ##
##-------------------------------##

## Imports
from enet import Address, Host, Peer  # type: ignore

from .connection import Connection
from .messages import ClientInfoMessage
from version import Version


## Classes
class Server(Connection):
    """
    JJx: Server Connection
    """

    # -Constructor
    def __init__(self, name: str, max_players: int = 4) -> None:
        super().__init__(None)
        self.name: str = name
        self.max_players: int = max_players
        # -Event Subscriptions
        self.subscribe_message(ClientInfoMessage, self._on_client_info)
        print(self._events)

    # -Instance Methods
    def close(self) -> None:
        pass

    def run(self, ip: str, port: int) -> None:
        ''''''
        self._host = Host(Address(ip.encode('utf-8'), port), 1, 0, 0)
        super().run(ip, port)

    def _on_client_info(self, name: str, version: Version, peer: Peer) -> None:
        ''''''
        print(f"ClientInfoEvent: name: {name}, version: {version}")

    # -Instance Methods: API
    def on_connected(self, peer: Peer) -> None:
        pass

    def on_disconnected(self, peer: Peer) -> None:
        pass
