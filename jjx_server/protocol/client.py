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
    WorldDataMessage, WorldInfoMessage, WorldInfoRequestMessage,
    Unknown1Message,
)
from ..version import Version
from ..world import Planet, TileMap, World

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
        self._world: World | None = None
        # -Event Subscriptions
        self.subscribe_message(AcceptMessage, self._on_accepted)
        self.subscribe_message(WorldInfoMessage, self._on_world_info)
        self.subscribe_message(WorldDataMessage, self._on_world_data)

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

    def _on_world_data(self, data: bytes, peer: Peer) -> None:
        ''''''
        self.world.blocks = TileMap.from_bytes(data, self.world.size, compressed=True)
        self.on_world_data(self.world.blocks)

    def _on_world_info(self, world: World, planet: Planet, peer: Peer) -> None:
        ''''''
        self._world = world
        self.on_world_info(world, planet)

    def _on_unknown1(self, data: bytes, peer: Peer) -> None:
        ''''''
        LOGGER.warn(f"Unknown compressed data: {data!r}")

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
    def on_world_info(self, world: World, planet: Planet) -> None: ...
    def on_world_data(self, tilemap: TileMap) -> None: ...

    # -Properties
    @property
    def connected(self) -> bool:
        return self.connection.state == 5

    @property
    def connection(self) -> Peer:
        '''Returns server peer'''
        return self.host.peers[0]

    @property
    def world(self) -> World:
        assert self._world is not None
        return self._world
