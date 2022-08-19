from functools import reduce

from herbstluftwm.log import get_logger

log = get_logger(__name__)


class HC:

    def __init__(self):
        pass


hc = HC()


def hc_register(f):
    hc.__dict__[f.__name__] = f
    return f


def hc_deco(f):

    def wrapped(*args, **kwargs):
        hc.__dict__[f.__name__] = f
        return f(*args, **kwargs)

    return wrapped


def delimit_str(name, start, delim=" "):

    def out(*args):
        return reduce(lambda x, y: f"{x}{delim}{y}", args, start)

    out.__name__ = name
    return out

