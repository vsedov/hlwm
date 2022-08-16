from functools import reduce

from herbstluftwm.log import get_logger

log = get_logger(__name__)


class HC:

    def __init__(self):
        pass


hc = HC()


def hc_set(f):
    hc.__dict__[f.__name__] = f
    return f


def hc_deco(f):

    def wrapped(*args, **kwargs):
        hc.__dict__[f.__name__] = f
        return f(*args, **kwargs)

    return wrapped
