#!/usr/bin/python
##-------------------------------##
## Junk Jack X: Protocol         ##
## Written By: Ryan Smith        ##
##-------------------------------##
## Client                        ##
##-------------------------------##

## Imports
import logging

from enet import Address, Host, Peer  # type: ignore

from .connection import CHANNELS, Connection
from .messages import (
    AcceptMessage, ClientInfoMessage,
    WorldInfoMessage, WorldInfoRequestMessage,
    UnknownMessage,
)
from ..version import Version
from ..world import World

## Constants
LOGGER = logging.getLogger(__name__)


## Classes
class Client(Connection):
    """
    JJx: Client Connection
    """

    # -Constructor
    def __init__(
        self, name: str, version: Version = Version.Latest
    ) -> None:
        super().__init__(Host(None, 1, CHANNELS))
        self.name: str = name
        self.version: Version = version
        # -Event Subscriptions
        self.subscribe_message(AcceptMessage, self._on_accepted)
        self.subscribe_message(WorldInfoMessage, self._on_world_info)

    # -Instance Methods
    def close(self) -> None:
        if self.connected:
            self.disconnect(immediate=True)

    def run(self, ip: str, port: int) -> None:
        '''Connect to server and run enet loop for handling server messages'''
        self._peer = self.host.connect(Address(ip.encode('utf-8'), port), CHANNELS)
        super().run(ip, port)

    def _on_accepted(self, code: int, peer) -> None:
        '''Client accepted into server event'''
        self.request_world_info()

    def _on_connected(self, peer: Peer) -> None:
        '''Log server peer info'''
        LOGGER.info(f"Client connected to {peer.address}")
        self.send_client_info()
        self.on_connected()

    def _on_disconnected(self, peer: Peer) -> None:
        '''Log server peer info'''
        LOGGER.info(f"Client disconnected from {peer.address}")
        self.on_disconnected()
        self.close()

    def _on_world_info(self, world: World) -> None:
        ''''''
        pass

    # -Instance Methods: API
    def disconnect(self, immediate: bool = False) -> None:
        '''Disconnect peer from server'''
        self.connection.disconnect()
        if immediate:
            self.host.flush()

    def request_world_info(self) -> None:
        '''Request world info from server connection'''
        msg = WorldInfoRequestMessage()
        self.send(msg, self.connection)

    def send_client_info(self) -> None:
        '''Send client information to the server'''
        msg = ClientInfoMessage(self.name, self.version)
        self.send(msg, self.connection)

    def on_connected(self) -> None: ...
    def on_disconnected(self) -> None: ...

    # -Properties
    @property
    def connected(self) -> bool:
        return self.connection.state == 5

    @property
    def connection(self) -> Peer:
        '''Returns server peer'''
        return self.host.peers[0]
