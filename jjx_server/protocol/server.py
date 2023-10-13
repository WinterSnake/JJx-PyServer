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

from .connection import Connection
from .message import (
    ClientInfoData, ClientInfoResponseCode, ClientInfoResponseData, Message
)
from .user import User
from ..version import Version
from ..world import World

## Constants
__all__: tuple[str] = ("Server",)
LOGGER = logging.getLogger(__name__)


## Classes
class Server(Connection):
    """
    JJx: Base Server
    """

    # -Constructor
    def __init__(self, max_players: int = 4) -> None:
        super().__init__(None)
        self.max_players: int = max_players

    # -Instance Methods
    def close(self) -> None:
        pass

    def run(self, ip: str, port: int) -> None:
        '''Bind server and run enet loop for handling client messages'''
        self._host = Host(
            Address(ip.encode('utf-8'), port),
            self.max_players, 0, 0
        )
        while True:
            self.process_messages()
            self.on_process()

    # -Instance Methods: Internal Events
    def _on_connected(self, peer: Peer) -> None:
        '''Event for when server has a client connect'''
        LOGGER.info(f"Peer @{peer.address} connected to server")
        self.on_connected(peer)

    def _on_disconnected(self, peer: Peer) -> None:
        '''Event for when server has a client disconnect'''
        LOGGER.info(f"Peer @{peer.address} disconnected from server")
        self.on_disconnected(peer)

    def _on_message(self, message: Message, peer: Peer) -> None:
        '''JJx Server Message event handler'''
        LOGGER.info(f"Received message ({message}) from @{peer.address}")
        match message.subtype:
            case Message.SubType.ClientInfo:
                assert message.data is not None
                assert isinstance(message.data, ClientInfoData)
                self._on_client_info(
                    message.data.player_id, message.data.player_name,
                    message.data.game_version, peer
                )

    def _on_client_info(
        self, _id: int, name: str, version: Version, peer: Peer
    ) -> None:
        '''Event for when client sends client info to server'''
        self.accept_client(peer)

    # -Instance Methods: API
    def accept_client(self, peer: Peer) -> None:
        '''Accept a jjx client peer'''
        msg = Message.client_response(ClientInfoResponseCode.Success)
        self.send(msg, peer)

    # -Instance Methods: API Events
    def on_process(self) -> None: ...
    def on_connected(self, peer: Peer) -> None: ...
    def on_client_info(self, user: User) -> None: ...
    def on_disconnected(self, peer: Peer) -> None: ...
