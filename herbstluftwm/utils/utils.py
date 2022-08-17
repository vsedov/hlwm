import builtins
import importlib
from inspect import getmembers, isfunction

from herbstluftwm.constants import EXCLUDE
from herbstluftwm.helper.magic import delimit_str, hc, hc_set
from herbstluftwm.log import get_logger

log = get_logger(__name__)


def get_function_info(f, function_name, exclude_list=[]) -> bool:
    in_exclude = function_name in exclude_list
    in_main_dict = function_name in hc.__dict__.keys()
    if in_main_dict:
        log.warn(f"Skipping : => {function_name} already exists, change the name\naddress => {f[1]}")
        return False
    elif in_exclude:
        log.warn("Skipping")
        return False
    return True


def run_all_function(module_name):
    imported = importlib.import_module(module_name)
    for f in getmembers(imported, isfunction):
        function_name = f[1].__name__
        if get_function_info(f, function_name, ["get_logger"]):
            log.info(f"Running {function_name}")
            hc_set(f[1])
        else:
            continue


def dictionary_item_looper(f):
    func = f[1]
    dictionary = func()
    for key, value in dictionary.items():
        hc_set(delimit_str(key, *value))

    return dictionary, func


def set_delimit_function(module_name):
    imported = importlib.import_module(module_name)
    log.info(hc.__dict__.keys())
    for f in getmembers(imported, isfunction):
        function_name = f[1].__name__
        if get_function_info(f, function_name, ["get_logger"]):
            match function_name:
                case "setup_dict":
                    dictionary_item_looper(f)
                case "setup_extra":
                    builtins.hc = hc
                    dictionary_item_looper(f)


def chain(*args, char="."):
    """Chain data"""
    to_chain = f" {char} ".join(args)
    return f"chain {char} {to_chain}"


def rotate(n):
    """Temp_doc"""

    assert n > 0
    return chain("lock", *["rotate" for _ in range(n)], "unlock")


def cls_func_name_to_var(class_name):
    return [f[0] for f in getmembers(class_name, isfunction) if not f[0].startswith("_")]
