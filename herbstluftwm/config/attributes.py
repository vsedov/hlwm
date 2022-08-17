# flake8: noqa
# type: ignore
from dataclasses import dataclass
from typing import Tuple

from herbstluftwm.helper.magic import hc
from herbstluftwm.log import get_logger

log = get_logger(__name__)


@dataclass
class CreateAttributes:
    attributes: dict

    def create(self) -> Tuple[str, dict]:
        """ Create the  attributes that get parsed through """
        main_attr = {}
        for attr in self.__dict__:
            if attr.startswith("attr_"):
                main_attr = {
                    **main_attr,
                    **self.__dict__[attr],
                }
        return main_attr


def setup_attributes():
    attr = {
        hc.set_theme("tiling.reset"): "1",
        hc.set_floating_theme("reset"): "1",
        hc.set_active_theme("active.color"): ...,
        hc.set_theme("normal.color"): ...,
        hc.set_theme("urgent.color"): ...,
        hc.set_theme("inner_width"): "0",
        hc.set_theme("inner_height"): "0",
        hc.set_theme("border_width"): "2",
        hc.set_floating_theme("border_width"): "4",
        hc.set_floating_theme("outer_width"): "1",
        hc.set_floating_theme("outer_color"): "'black'",
        hc.set_active_theme("inner_color"): "'#3E4A00'",
        hc.set_active_theme("outer_color"): "'#3E4A00'",
        hc.set_active_theme("background_color"): "'#141414'",
    }
    return CreateAttributes(attr).create()
