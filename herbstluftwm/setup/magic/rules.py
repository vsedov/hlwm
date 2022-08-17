from herbstluftwm.log import get_logger

log = get_logger(__name__)


def setup_dict():
    return {
        "set_class": ["class", "="],
        "set_instance": ["windowtype", "="],
    }
