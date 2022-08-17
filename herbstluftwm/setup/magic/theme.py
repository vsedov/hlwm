from herbstluftwm.log import get_logger

log = get_logger(__name__)


def setup_dict():
    return {
        "set_theme": ["theme", "."],
    }


def setup_extra():
    return {
        "set_floating_theme": [hc.set_theme("floating"), "."],
        "set_active_theme": [hc.set_theme("active"), "."],
    }
