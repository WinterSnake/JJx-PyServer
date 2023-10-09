#!/usr/bin/python
##-------------------------------##
## Junk Jack X: Protocol         ##
## Written By: Ryan Smith        ##
##-------------------------------##
## Message: World Info           ##
##-------------------------------##

## Imports
from __future__ import annotations
import struct
from typing import cast

from .base import Message
from ...world import (
    Gamemode, InitSize, Planet, Season, TileMap, Time, World
)


## Classes
class WorldInfoMessage(Message):
    """
    JJx Message: World Info
    """

    # -Constructor
    def __init__(
            self,
            world_init_size: InitSize, sky_init_size: InitSize,
            world_size: tuple[int, int], spawn_position: tuple[int, int],
            player_position: tuple[int, int], gamemode: Gamemode,
            season: Season, world_planet_1: Planet, world_planet_2: Planet,
            world_time: Time, language: str | None, world_size_in_bytes: int
    ) -> None:
        self.world_init_size: InitSize = world_init_size
        self.sky_init_size: InitSize = sky_init_size
        self.world_size: tuple[int, int] = world_size
        self.spawn_position: tuple[int, int] = spawn_position
        self.player_position: tuple[int, int] = player_position
        self.gamemode: Gamemode = gamemode
        self.season: Season = season
        self.planet_1: Planet = world_planet_1
        self.planet_2: Planet = world_planet_2
        self.world_time: Time = world_time
        self.language: str | None = language
        self.world_size_in_bytes: int = world_size_in_bytes

    def __len__(self) -> int:
        return len(self.to_bytes())

    def __str__(self) -> str:
        return "WorldInfo"

    # -Instance Methods
    def to_args(self) -> tuple[World, Planet]:
        return (
            World(
                self.world_init_size, self.sky_init_size,
                self.world_size, self.spawn_position, self.player_position,
                self.gamemode, self.world_time, self.planet_1, self.season,
                TileMap(self.world_size), self.language
            ),
            self.planet_2
        )


    def to_bytes(self) -> bytes:
        message = bytearray(struct.pack(">H", self.opcode))
        message.extend(struct.pack("<HH", *self.world_size))
        message.extend(struct.pack("<HH", *self.spawn_position))
        message.extend(struct.pack("<HH", *self.player_position))
        message.extend(self.time.ticks.to_bytes(4, byteorder='little'))
        message.append(self.time.phase.value)
        message.extend([0x01, 0x00])  # ---UNKNOWN
        message.extend(self.planet_1.value.to_bytes(4, byteorder='little'))
        message.append(0x02)  # ---UNKNONW
        message.extend(self.planet_2.value.to_bytes(4, byteorder='little'))
        message.extend([
            self.season, self.gamemode, self.world_init_size, self.sky_init_size
        ])
        message.extend(
            self.language.encode('ascii') if self.language else [0xFF, 0xFF]
        )
        message.extend([0x00, 0x00])  # ---UNKNOWN
        message.extend(self.world_size_in_bytes)
        return bytes(message)

    # -Class Methods
    @classmethod
    def from_bytes(cls, data: bytes) -> WorldInfoMessage:
        world_size = struct.unpack("<HH", data[0:4])
        spawn_position = struct.unpack("<HH", data[4:8])
        player_position = struct.unpack("<HH", data[8:12])
        language: str | None = None
        try:
            language = data[32:34].decode('ascii')
        except UnicodeDecodeError:
            pass
        return cls(
            # -World Init Size / Sky Init Size
            InitSize(data[30]), InitSize(data[31]),
            cast(tuple[int, int], world_size),  # -World Size
            cast(tuple[int, int], spawn_position),  # -Spawn Position
            cast(tuple[int, int], player_position),  # -Player Position
            # -Gamemode / Season
            Gamemode(data[29]), Season(data[28]),
            # -Planets
            Planet(int.from_bytes(data[19:23], byteorder='little')),
            Planet(int.from_bytes(data[24:28], byteorder='little')),
            Time(
                int.from_bytes(data[12:16], byteorder='little'),
                Time.Phase(data[16])
            ),
            language, int.from_bytes(data[34:], byteorder='little')
        )

    @classmethod
    def from_world(cls, world: World) -> WorldInfoMessage:
        '''Create a world info message from a given world'''
        return cls(
            world.init_size, world.sky_size, world.size, world.spawn,
            world.player, world.gamemode, world.season, world.planet,
            world.planet, world.time, world.language, len(world.blocks)
        )

    # -Class Properties
    opcode = 0x0343
