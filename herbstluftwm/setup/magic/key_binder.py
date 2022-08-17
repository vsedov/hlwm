from herbstluftwm.log import get_logger

log = get_logger(__name__)


def setup_dict():

    return {
        "mod": ["Mod4", "-"],
        "shift": ["Shift", "-"],
        "ctrl": ["control", "-"],
        "alt": ["alt", "-"],
        "space": ["space", "-"],
        "spawn": ["spawn", " "],
    }


def setup_extra():
    return {
        "mod_shift": [hc.mod(hc.shift()), "-"],
        "mod_ctrl": [hc.mod(hc.ctrl()), "-"],
        "mod_alt": [hc.mod(hc.alt()), "-"],
        "mod_shift_ctrl": [hc.mod(hc.shift(hc.ctrl())), "-"],
    }

