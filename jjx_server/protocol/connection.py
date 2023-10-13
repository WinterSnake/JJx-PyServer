#!/usr/bin/python
##-------------------------------##
## Junk Jack X: Protocol         ##
## Written By: Ryan Smith        ##
##-------------------------------##
## Connection                    ##
##-------------------------------##

## Imports
import logging
from abc import ABC, abstractmethod

from enet import Event, Host, Packet, Peer  # type: ignore

from .message import Message

## Constants
__all__: tuple[str] = ("Connection",)
LOGGER = logging.getLogger(__name__)


## Classes
class Connection(ABC):
    """
    JJx: Enet Connection
    """

    # -Constructor
    def __init__(self, host: Host | None) -> None:
        self._host: Host | None = host

    # -Instance Methods
    @abstractmethod
    def close(self) -> None: ...

    def process_messages(self) -> None:
        '''Process message events in the enet queue and push to event handlers'''
        event: Event = self.host.service(0)
        if event.type == 1:
            self._on_connected(event.peer)
        elif event.type == 2:
            self._on_disconnected(event.peer)
        elif event.type == 3:
            LOGGER.debug(
                f"{type(self).__name__} handling event from "
                f"@{event.peer.address} via channel[{event.channelID}] "
                f"with data: {event.packet.data}"
            )
            message = Message.from_bytes(event.packet.data)
            self._on_message(message, event.peer)


    @abstractmethod
    def run(self, ip: str, port: int) -> None: ...

    def send(
        self, message: Message, peer: Peer,
        channel_id: int = 0, immediate: bool = False
    ) -> None:
        '''Send a message over the enet socket'''
        packet = Packet(message.to_bytes())
        peer.send(channel_id, packet)
        if immediate:
            self.host.flush()

    # -Instance Methods: API
    @abstractmethod
    def _on_connected(self, peer: Peer) -> None: ...
    
    @abstractmethod
    def _on_disconnected(self, peer: Peer) -> None: ...

    @abstractmethod
    def _on_message(self, message: Message, peer: Peer) -> None: ...

    # -Properties
    @property
    def host(self) -> Host:
        assert self._host is not None
        return self._host
