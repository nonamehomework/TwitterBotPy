# -*- coding: utf-8 -*-
import os

__version__ = '1.0'

home = os.getenv("HOME")
default_config_path = [
    home + "/.botkun.toml",
    home + "/.config/botkun.toml",
    home + "/.config/botkun/config.toml"
]

