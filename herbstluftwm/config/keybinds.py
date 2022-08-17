# type: ignore
from dataclasses import dataclass

from herbstluftwm.helper.magic import hc
from herbstluftwm.log import get_logger

log = get_logger(__name__)
resize_step = "0.05"


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

    def create(self):
        """ Create the keybinds that get parsed through """
        main_keybind_dict = {}
        for keybind in self.__dict__:
            if keybind.startswith("keybind_"):
                main_keybind_dict = {
                    **main_keybind_dict,
                    **self.__dict__[keybind],
                }
        return main_keybind_dict


def setup_binds():

    keybind_sesion = {
        # Session keys
        hc.mod_shift("q"): "quit",
        hc.mod_shift("r"): "reload",
        hc.mod_shift("c"): "close"
    }
    #
    keybind_misc_spawn = {
        # misc keys
        hc.mod("d"): hc.spawn("rofi -show run"),
        hc.mod("Enter"): hc.spawn("kitty"),
        hc.mod_shift("Enter"): hc.spawn("waterfox-g4 --sync")
    }

    keybind_focus_client = {
        # focus client keys
        hc.mod("Left"): "focus left",
        hc.mod("Down"): "focus down",
        hc.mod("Up"): "focus up",
        hc.mod("Right"): "focus right",
        hc.mod("h"): "focus left",
        hc.mod("j"): "focus down",
        hc.mod("k"): "focus up",
        hc.mod("l"): "focus right",
    }

    keybind_focus_monitor = {
        # Monitor focus
        hc.mod("BackSpace"): 'cycle_moinitor',
        hc.mod("Tab"): "cycle_all +1",
        hc.mod_shift("Tab"): "cycle_all -1",
        hc.mod("c"): "cycle",
        hc.mod("i"): "jumpto urgent"
    }

    keybind_move_client = {
        # move client
        hc.mod_shift("Left"): "shift left",
        hc.mod_shift("Down"): "shift down",
        hc.mod_shift("Up"): "shift up",
        hc.mod_shift("Right"): "shift right",
        hc.mod_shift("h"): "shift left",
        hc.mod_shift("j"): "shift down",
        hc.mod_shift("k"): "shift up",
        hc.mod_shift("l"): "shift right",
    }
    keybind_split_frames = {
        # Fram Splitting
        hc.mod("u"): "split bottom 0.5",
        hc.mod("o"): "split right 0.5",
        hc.mod_ctrl("space"): "split explod"
    }

    keybind_resize_frames = {
        # resize frames
        hc.mod_ctrl("h"): 'resize left  +' + resize_step,
        hc.mod_ctrl("j"): 'resize down' + resize_step,
        hc.mod_ctrl("k"): 'resize up' + resize_step,
        hc.mod_ctrl("l"): 'resize right' + resize_step,
        hc.mod_ctrl("Left"): 'resize left' + resize_step,
        hc.mod_ctrl("Down"): 'resize down' + resize_step,
        hc.mod_ctrl("Up"): 'resize up' + resize_step,
        hc.mod_ctrl("Right"): 'resize right' + resize_step,
    }

    keybind_tag = {
        hc.mod("period"): "use_index +1 --skip-visible",
        hc.mod("comma"): "use_index -1 --skip-visible"
    }

    keybind_layout = {
        hc.mod("r"): "remove",
        hc.mod("s"): "floating toggle",
        hc.mod("f"): "fullscreen toggle",
        hc.mod("p"): "pseudotile toggle",
    }
    return CreateBinds(
        keybind_sesion, keybind_misc_spawn, keybind_focus_client, keybind_focus_monitor, keybind_move_client,
        keybind_split_frames, keybind_resize_frames, keybind_tag, keybind_layout).create()
