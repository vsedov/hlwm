#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# File Name: constants.py
import os
from typing import Optional

TRACE_LOGGERS: list[str] = [f"!{__name__}"]
# paths
DIR: Optional[str] = os.path.dirname(__file__)

STARTUP = {
    "applet &", "nm-applet", "dunst &", "flameshot &", "feh --bg-scale ~/Downloads/upscalebuterfly.png",
    "~/.config/polybar/launch.sh", "pasystray", "/user/bin/subl", "/user/bin/franz", "/user/bin/lampe-gtk",
    "sleep 15 ^^ pulseeffects"
}
EXCLUDE = ["get_logger"]
