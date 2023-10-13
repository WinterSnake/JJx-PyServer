#!/usr/bin/python
##-------------------------------##
## Junk Jack X: Protocol         ##
## Written By: Ryan Smith        ##
##-------------------------------##
## Client                        ##
##-------------------------------##

## Imports
import logging
import random

from enet import Address, Host, Peer  # type: ignore

from .connection import Connection
from .message import (
    ClientInfoResponseCode, ClientInfoResponseData, Message
)
from ..player import Player
from .user import User
from ..world import World

## Constants
__all__: tuple[str] = ("Client",)
LOGGER = logging.getLogger(__name__)


## Classes
class Client(Connection, User):
    """
    JJx: Base Client
    """

    # -Constructor
    def __init__(self, player: Player) -> None:
        Connection.__init__(self, Host(None, 1, 0, 0))
        User.__init__(self, random.randint(1, 255), player)

    # -Instance Methods
    def close(self) -> None:
        pass

    def run(self, ip: str, port: int) -> None:
        '''Connect to server and run enet loop for handling server messages'''
        self.host.connect(Address(ip.encode('utf-8'), port), 0)
        while True:
            self.process_messages()
            if self.ready:
                self.on_process()

    # -Instance Methods: Internal API Events
    def _on_connected(self, peer: Peer) -> None:
        '''Event for when client connects to server successfully'''
        LOGGER.info(f"Successfully connected to @{peer.address}")
        self.send_client_info()
        self.on_connected()

    def _on_disconnected(self, peer: Peer) -> None:
        '''Event for when client disconnect to server successfully'''
        LOGGER.info(f"Disconnected from @{peer.address}")
        self.on_disconnected()

    def _on_message(self, message: Message, peer: Peer) -> None:
        '''JJx Client Message event handler'''
        LOGGER.info(f"Received message [{message}] from @{peer.address}")
        match message.subtype:
            case Message.SubType.ClientInfoResponse:
                print(type(message.data))
                assert message.data is not None
                assert isinstance(message.data, ClientInfoResponseData)
                self._on_client_info_response(message.data.code)

    def _on_client_info_response(self, code: ClientInfoResponseCode) -> None:
        '''Event for when client receives code from server login'''
        if code == ClientInfoResponseCode.Success:
            pass
        self.on_client_info_response(code)

    # -Instance Methods: API
    def disconnect(self) -> None:
        '''Send a disconnect packet to connected server'''
        self.remote.disconnect()
        self.host.flush()

    def send_client_info(self) -> None:
        '''Send client information to connected server'''
        msg = Message.client_info(
            self.id,
            self.character.name,
            self.character.version
        )
        self.send(msg, self.remote)

    # -Instance Methods: API Events
    def on_process(self) -> None: ...
    def on_connected(self) -> None: ...
    def on_client_info_response(self, code: ClientInfoResponseCode) -> None: ...
    def on_disconnected(self) -> None: ...

    # -Properties
    @property
    def connected(self) -> bool:
        return self.remote.state == 5

    @property
    def ready(self) -> bool:
        return False

    @property
    def remote(self) -> Peer:
        return self.host.peers[0]
