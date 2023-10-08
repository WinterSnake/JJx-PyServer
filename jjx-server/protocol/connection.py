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
from collections.abc import Callable
from typing import Any, Type

from enet import Host, Packet, Peer  # type: ignore

from .messages import Message, _bytes_to_hex_string, parse as message_parse
from ..version import Version

## Constants
EventHandler = Callable[[Any], None]
LOGGER = logging.getLogger(__name__)
CHANNELS: int = 0


## Classes
class Connection(ABC):
    """
    JJx: Base Connection
    """

    # -Constructor
    def __init__(self, host: Host | None) -> None:
        self._host: Host | None = host
        self._events: dict[Type[Message], list[EventHandler]] = {}

    # -Instance Methods
    @abstractmethod
    def close(self) -> None: ...

    @abstractmethod
    def run(self, ip: str, port: int) -> None:
        '''Run enet event loop and pass events to handlers'''
        while True:
            event = self.host.service(0)
            # -Connected
            if event.type == 1:
                self._on_connected(event.peer)
            # -Disconnected
            elif event.type == 2:
                self._on_disconnected(event.peer)
            # -Receive
            if event.type == 3:
                data = _bytes_to_hex_string(event.packet.data)
                LOGGER.debug(f"Received message '{data}' via channel[{event.channelID}]")
                message = message_parse(event.packet.data)
                self._on_message(event.peer, message)

    def send(
        self, message: Message, peer: Peer,
        channel_id: int = 0, immediate: bool = False
    ) -> None:
        '''Covert message to enet packet and send to peer channel'''
        msg = message.to_bytes()
        LOGGER.debug(
            f"Sending '{_bytes_to_hex_string(msg)}' to peer "
            f"@{peer.address} via channel[{channel_id}]"
        )
        peer.send(channel_id, Packet(msg))
        if immediate:
            self.host.flush()

    def subscribe_message(self, message: Type[Message], handle: EventHandler) -> None:
        '''Add a function callback for message handling'''
        LOGGER.debug(f"Adding {handle.__name__} for '{message}' event")
        if message in self._events:
            self._events[message].append(handle)
        else:
            self._events[message] = [handle]

    def _on_message(self, peer: Peer, message: Message) -> None:
        '''Call appropriate event handlers for message and pass message parameters'''
        msg_type = type(message)
        if msg_type not in self._events:
            LOGGER.debug(f"No event handlers for '{msg_type}'")
            return
        for handle in self._events[msg_type]:
            args = message.to_args()
            LOGGER.debug(
                f"Calling {handle.__name__}("
                f"{','.join(str(arg) for arg in args)})"
            )
            if args:
                handle(*args, peer)  # type: ignore
            else:
                handle(peer)  # type: ignore

    @abstractmethod
    def _on_connected(self, peer: Peer) -> None: ...

    @abstractmethod
    def _on_disconnected(self, peer: Peer) -> None: ...

    # -Properties
    @property
    def host(self) -> Host:
        assert self._host is not None
        return self._host
