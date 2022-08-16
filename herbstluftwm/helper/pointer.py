from herbstluftwm.helper.test import hc, hc_deco, hc_set
from herbstluftwm.log import get_logger

log = get_logger(__name__)

# log.info(hc.hc("keybind", hc.mod4("shift", "left"), "focus left"))


@hc_deco
def demo(a, b, c):
    return a + b + c


demo(1, 2, 3)
hc.demo
# print(hc.demo)
# log.info(hc.mod("shift", "left"))
log.info(hc.__dict__.keys())

