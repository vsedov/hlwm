from herbstluftwm.log import get_logger
from herbstluftwm.utils.utils import create_dict

log = get_logger(__name__)


def setup_dict():
    return create_dict(*{("set_class", "class", "="), ("set_instance", "windowtype", "=")})
