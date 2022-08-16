# flake8: noqa

from dataclasses import dataclass
from typing import Tuple

from herbstluftwm.helper.helper import SetKeybinds, set_global
from herbstluftwm.log import get_logger

log = get_logger(__name__)
resize_step = "0.05"

set_global(SetKeybinds, globals())


@dataclass
class CreateBinds:
    keybind_sesion: dict
    keybind_misc_spawn: dict
    keybind_focus_client: dict
    keybind_focus_monitor: dict
    keybind_move_client: dict
    keybind_split_frames: dict
    keybind_resize_frames: dict
    keybind_tag: dict
    keybind_layout: dict

    def create(self) -> Tuple[str, dict]:
        """ Create the keybinds that get parsed through """
        for keybind in self.__dict__:
            if keybind.startswith("keybind_"):
                yield (keybind, self.__dict__[keybind])


keybind_sesion = {
    # Session keys
    mod_shift("q"): "quit",
    mod_shift("r"): "reload",
    mod_shift("c"): "close"
}
#
keybind_misc_spawn = {
    # misc keys
    mod("d"): spawn("rofi -show run"),
    mod("Enter"): spawn("kitty"),
    mod_shift("Enter"): spawn("waterfox-g4 --sync")
}

keybind_focus_client = {
    # focus client keys
    mod("Left"): "focus left",
    mod("Down"): "focus down",
    mod("Up"): "focus up",
    mod("Right"): "focus right",
    mod("h"): "focus left",
    mod("j"): "focus down",
    mod("k"): "focus up",
    mod("l"): "focus right",
}

keybind_focus_monitor = {
    # Monitor focus
    mod("BackSpace"): 'cycle_moinitor',
    mod("Tab"): "cycle_all +1",
    mod_shift("Tab"): "cycle_all -1",
    mod("c"): "cycle",
    mod("i"): "jumpto urgent"
}

keybind_move_client = {
    # move client
    mod_shift("Left"): "shift left",
    mod_shift("Down"): "shift down",
    mod_shift("Up"): "shift up",
    mod_shift("Right"): "shift right",
    mod_shift("h"): "shift left",
    mod_shift("j"): "shift down",
    mod_shift("k"): "shift up",
    mod_shift("l"): "shift right",
}
keybind_split_frames = {
    # Fram Splitting
    mod("u"): "split bottom 0.5",
    mod("o"): "split right 0.5",
    mod_ctrl("space"): "split explod"
}

keybind_resize_frames = {
    # resize frames
    mod_ctrl("h"): 'resize left  +' + resize_step,
    mod_ctrl("j"): 'resize down' + resize_step,
    mod_ctrl("k"): 'resize up' + resize_step,
    mod_ctrl("l"): 'resize right' + resize_step,
    mod_ctrl("Left"): 'resize left' + resize_step,
    mod_ctrl("Down"): 'resize down' + resize_step,
    mod_ctrl("Up"): 'resize up' + resize_step,
    mod_ctrl("Right"): 'resize right' + resize_step,
}

keybind_tag = {
    mod("period"): "use_index +1 --skip-visible",
    mod("comma"): "use_index -1 --skip-visible"
}

keybind_layout = {
    mod("r"): "remove",
    mod("s"): "floating toggle",
    mod("f"): "fullscreen toggle",
    mod("p"): "pseudotile toggle",
}

BINDS = CreateBinds(
    keybind_sesion, keybind_misc_spawn, keybind_focus_client, keybind_focus_monitor, keybind_move_client,
    keybind_split_frames, keybind_resize_frames, keybind_tag, keybind_layout).create()
