#!/usr/bin/python
##-------------------------------##
## Junk Jack X: Protocol         ##
## Written By: Ryan Smith        ##
##-------------------------------##
## Connection                    ##
##-------------------------------##

## Imports
from abc import ABC, abstractmethod
from collections.abc import Callable
from typing import Any, Type

from enet import Host, Peer  # type: ignore

from .messages import Message, parse as message_parse
from version import Version

## Constants
EventHandler = Callable[[Any], None]


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
                print("Handling connect..")
            # -Disconnected
            elif event.type == 2:
                print("Handling disconnect..")
            # -Receive
            if event.type == 3:
                print("Handling received message..")
                message = message_parse(event.packet.data)
                self._on_message(event.peer, message)

    def subscribe_message(self, message: Type[Message], handle) -> None:
        '''Add a function callback for message handling'''
        if message in self._events:
            self._events[message].append(handle)
        else:
            self._events[message] = [handle]

    def _on_message(self, peer: Peer, message: Message) -> None:
        '''Call appropriate event handlers for message and pass message parameters'''
        if type(message) not in self._events:
            return
        print("Found event..")
        for handle in self._events[type(message)]:
            print(handle)
            args = message.to_args()
            if args:
                handle(*args, peer)  # type: ignore
            else:
                handle(peer)  # type: ignore

    # -Instance Methods: API
    @abstractmethod
    def on_connected(self, peer: Peer) -> None: ...

    @abstractmethod
    def on_disconnected(self, peer: Peer) -> None: ...

    # -Properties
    @property
    def host(self) -> Host:
        assert self._host is not None
        return self._host
