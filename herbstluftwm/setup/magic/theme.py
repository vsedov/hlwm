from herbstluftwm.log import get_logger
from herbstluftwm.utils.utils import create_dict

log = get_logger(__name__)


def setup_dict():
    return create_dict(*{("set_theme", "theme", ".")})


def setup_extra():
    return create_dict(
        *{("set_floating_theme", hc.set_theme("floating"), "."), ("set_active_theme", hc.set_theme("active"), ".")})
