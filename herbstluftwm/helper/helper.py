from inspect import getmembers, isfunction

from attr import define

from herbstluftwm.log import get_logger

log = get_logger(__name__)


def set_global(class_name, glob):
    """
    Create global variables:
    This little function will index, global to create variables based on the function names
    For example :
        ```
            def mod(self, args: str) -> str:
                return f"Mod4-{args}"

            def shift(self, args: str) -> str:
                return f"shift-{args}"
        ```
    Will create a list of ["mod", "shift"]
    Then the loop will index into global vars

    return None
    """

    helper = class_name()
    them_var = [f[0] for f in getmembers(class_name, isfunction) if not f[0].startswith("_")]
    for f in them_var:
        # log.info(f)
        glob[f] = getattr(helper, f)
    return glob


@define
class SetKeybinds:

    def spawn(self, args):
        return f"spawn {args}"

    def mod(self, args: str) -> str:
        return f"mod4-{args}"

    def shift(self, args: str) -> str:
        return f"shift-{args}"

    def control(self, args: str) -> str:
        return f"control-{args}"

    def alt(self, args: str) -> str:
        return f"mod1-{args}"

    def space(self, args: str) -> None:
        return f"space-{args}"

    def mod_shift(self, command: str) -> str:
        return self.mod(self.shift(command))

    def mod_ctrl(self, command: str) -> str:
        return self.mod(self.control(command))


@define
class SetRules:

    def set_class(self, args: str) -> None:
        return f"class={args}"

    def window_type(self, args: str) -> None:
        return f"windowtype={args}"


@define
class SetTheme:

    def set_theme(self, args):
        return f"theme.{args}"

    def set_floating_theme(self, args):
        return self.set_theme(f"floating.{args}")

    def set_active_theme(self, args):
        return self.set_theme(f"active.{args}")
