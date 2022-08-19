from functools import reduce

from herbstluftwm.log import get_logger
from herbstluftwm.utils.utils import create_dict

log = get_logger(__name__)


def setup_dict():
    # yapf: disable
    main_dir = {
        ("mod", "Mod4", "-"),
        ("shift", "ctrl", "-"),
        ("ctrl", "Shift", "-"),
        ("alt", "alt", "-"),
        ("space", "space", "-"),
        ("spawn", "spawn", " ")

    }
    # yapf: enable
    return create_dict(*main_dir)


def setup_extra():
    # yapf: disable
    extra_dir = {
        ("mod_shift", hc.mod(hc.shift()), "-"),
        ("mod_ctrl", hc.mod(hc.ctrl()), "-"),
        ("mod_alt", hc.mod(hc.alt()), "-"),
        ("mod_shift_ctrl", hc.mod(hc.shift(hc.ctrl())), "-")
    }
    # yapf: enable
    return create_dict(*extra_dir)
