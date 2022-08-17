from inspect import getmembers, isfunction

from attr import define

from herbstluftwm.helper.test import hc_deco
from herbstluftwm.log import get_logger
from herbstluftwm.utils.utils import cls_func_name_to_var

log = get_logger(__name__)


def set_global(class_name, glob):
    """
    Create global variables:
    This little function will index, global to create variables based on the function names
    For example :
        ```
            def mod(self, args: str) -> str:
                return f"Mod4-{args}"

            def shift(self, args: str) -> str:
                return f"shift-{args}"
        ```
    Will create a list of ["mod", "shift"]
    Then the loop will index into global vars

    return None
    """
    helper = class_name()
    them_var = cls_func_name_to_var(class_name)
    for f in them_var:
        # log.info(f)
        glob[f] = getattr(helper, f)
    return glob
