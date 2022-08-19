from herbstluftwm.helper.test import hc, hc_deco
from herbstluftwm.log import get_logger

log = get_logger(__name__)


@hc_deco
def demo(a, b, c):
    return a + b + c


demo(1, 2, 3)
