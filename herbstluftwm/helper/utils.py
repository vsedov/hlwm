import os

from herbstluftwm.log import get_logger

log = get_logger(__name__)


def system_run(run: str):
    """
    Run System commands

    Parameters
    ----------
    run : str
        executalbe system command
    """
    os.system(run)


def hc(args: str):
    """HC runs herbstclient commands

    Parameters
    ----------
    args : str
        Executes herbclient commands
    """
    system_run(f"herbstclient {args}")


def do_config(command: str, dictionary: dict):
    """
    Create config / do_config
    Parses herbstclient command based on command

    Parameters
    ----------
    command : str
        Command based on herb
    dictionary : dict
        data being parsed down
    """
    for k, v in dictionary.items():
        hc(f"{command} {k} {v}")
        log.info(f"{command} {k} {v}")


def startup_run(command_dict: dict[str]):
    """Commands to run on startup"""
    command = 'silent new_attr bool my_not_first_autostart'
    exit_code = hc(command)
    if exit_code == 0:
        for command in command_dict:
            system_run(command)


def bind_cycle_layout():
    # The following cycles through the available layouts
    # within a frame, but skips layouts, if the layout change
    # wouldn't affect the actual window positions.
    # I.e. if there are two windows within a frame,
    # the grid layout is skipped.

    hc(
        "keybind Mod4-space "
        "or , and . compare tags.focus.curframe_wcount = 2 "
        ". cycle_layout +1 vertical horizontal max vertical grid "
        ", cycle_layout +1 ")

