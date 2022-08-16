# flake8: noqa
from dataclasses import dataclass
from inspect import getmembers, isfunction
from typing import Tuple

from herbstluftwm.helper.helper import SetTheme
from herbstluftwm.log import get_logger

log = get_logger(__name__)


#  TODO(vsedov) (01:31:05 - 16/08/22): This cannt be refactore , as the global scope would change.
def create_global_var() -> SetTheme:

    helper = SetTheme()
    them_var = [
        f[0] for f in getmembers(SetTheme, isfunction)
        if not f[0].startswith("_")
    ]
    for f in them_var:
        # log.info(f)
        globals()[f] = getattr(helper, f)
    return helper


helper = create_global_var()


@dataclass
class CreateAttributes:
    attributes: dict

    def create(self) -> Tuple[str, dict]:
        """ Create the  attributes that get parsed through """
        for attr in self.__dict__:
            if attr.startswith("attr_"):
                yield (attr, self.__dict__[attr])


attr = {
    set_theme("tiling.reset"): "1",
    set_floating_theme("reset"): "1",
    set_active_theme("active.color"): ...,
    set_theme("normal.color"): ...,
    set_theme("urgent.color"): ...,
    set_theme("inner_width"): "0",
    set_theme("inner_height"): "0",
    set_theme("border_width"): "2",
    set_floating_theme("border_width"): "4",
    set_floating_theme("outer_width"): "1",
    set_floating_theme("outer_color"): "'black'",
    set_active_theme("inner_color"): "'#3E4A00'",
    set_active_theme("outer_color"): "'#3E4A00'",
    set_active_theme("background_color"): "'#141414'",
}
ATTR = CreateAttributes(attr).create()
