from inspect import getmembers, isfunction

from attr import define

from herbstluftwm.helper.test import hc_deco
from herbstluftwm.log import get_logger
from herbstluftwm.utils.utils import cls_func_name_to_var

log = get_logger(__name__)


def set_global(class_name, glob):
    helper = class_name()
    them_var = cls_func_name_to_var(class_name)
    for f in them_var:
        # log.info(f)
        glob[f] = getattr(helper, f)
    return glob


