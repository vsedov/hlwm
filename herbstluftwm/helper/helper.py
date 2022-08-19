from inspect import getmembers, isfunction

from attr import define

from herbstluftwm.helper.test import hc_deco
from herbstluftwm.log import get_logger
from herbstluftwm.utils.utils import cls_func_name_to_var

log = get_logger(__name__)


#  PERF(vsedov) (23:26:48 - 19/08/22): This is bad python code :
#  Modifying global = Bad, do not do that.
def set_global(class_name, glob):
    helper = class_name()
    them_var = cls_func_name_to_var(class_name)
    for f in them_var:
        # log.info(f)
        glob[f] = getattr(helper, f)
    return glob
