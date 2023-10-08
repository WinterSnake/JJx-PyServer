#!/usr/bin/python
##-------------------------------##
## Junk Jack X: Protocol         ##
## Written By: Ryan Smith        ##
##-------------------------------##
## Server                        ##
##-------------------------------##

## Imports
import logging

from enet import Address, Host, Peer  # type: ignore

from .connection import CHANNELS, Connection
from .messages import ClientInfoMessage
from ..version import Version

## Constants
LOGGER = logging.getLogger(__name__)


## Classes
class Server(Connection):
    """
    JJx: Server Connection
    """

    # -Constructor
    def __init__(self, name: str, max_players: int = 4) -> None:
        super().__init__(None)
        max_players = max(1, min(max_players, 0xFFF))
        self.name: str = name
        self.max_players: int = max_players
        # -Event Subscriptions
        self.subscribe_message(ClientInfoMessage, self._on_client_info)

    # -Instance Methods
    def close(self) -> None:
        pass

    def run(self, ip: str, port: int) -> None:
        '''Bind server and run enet loop for handling client messages'''
        self._host = Host(
            Address(ip.encode('utf-8'), port),
            self.max_players, CHANNELS
        )
        super().run(ip, port)

    def _on_connected(self, peer: Peer) -> None:
        '''Log client peer info'''
        LOGGER.info(f"Client connected @{peer.address}")
        self.on_connected(peer)

    def _on_disconnected(self, peer: Peer) -> None:
        '''Log client peer info'''
        LOGGER.info(f"Client disconnected @{peer.address}")
        self.on_disconnected(peer)

    def _on_client_info(self, name: str, version: Version, peer: Peer) -> None:
        ''''''
        LOGGER.info("Event: OnClientInfo")
        self.on_client_info(name, version, peer)

    # -Instance Methods: API
    def on_connected(self, peer: Peer) -> None: ...
    def on_client_info(self, name: str, version: Version, peer: Peer) -> None: ...
    def on_disconnected(self, peer: Peer) -> None: ...
