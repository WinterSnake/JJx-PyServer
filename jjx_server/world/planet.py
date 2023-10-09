#!/usr/bin/python
##-------------------------------##
## Junk Jack X: World            ##
## Written By: Ryan Smith        ##
##-------------------------------##
## Planet                        ##
##-------------------------------##

## Imports
from enum import IntFlag

## Constants
__all__: tuple[str] = ("Planet",)


## Classes
class Planet(IntFlag):
    """JJx Planet Flags"""
    Terra = 0x00000001
    Seth = 0x00000002
    Alba = 0x00000004
    Xeno = 0x00000008
    Magmar = 0x00000010
    Cryo = 0x00000020
    Yuca = 0x00000040
    Lilith = 0x00000080
    Thetis = 0x00000100
    Mykon = 0x00000200
    Umbra = 0x00000400
    Tor = 0x00000800
    All = Terra | Seth | Alba | Xeno | Magmar | Cryo | Yuca | Lilith | Thetis | Mykon | Umbra | Tor
