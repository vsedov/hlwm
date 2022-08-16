import importlib
import inspect
import pkgutil
from typing import Iterator, NoReturn

from herbstluftwm import setup
from herbstluftwm.log import get_logger

log = get_logger(__name__)


def unqualify(name: str) -> str:
    """Return an unqualified name given a qualified module/package `name`."""
    return name.rsplit(".", maxsplit=1)[-1]


def walk_extensions() -> Iterator[str]:
    """Yield extension names from the bot.exts subpackage."""

    def on_error(name: str) -> NoReturn:
        """An error handler for `pkgutil.walk_packages`."""
        raise ImportError(name=name)  # pragma: no cover

    for module in pkgutil.walk_packages(setup.__path__, f"{setup.__name__}.", onerror=on_error):
        if unqualify(module.name).startswith("_"):
            # Ignore module/package names starting with an underscore.
            continue  # pragma: no cover
        if "main" in module.name:
            continue

        if module.ispkg:
            imported = importlib.import_module(module.name)
            if not inspect.isfunction(getattr(imported, "setup", None)):  # pragma: no cover
                # If it lacks a setup function, it's not an extension + hard to test.
                continue
            log.info("i got here")

        yield module.name


def find_extension(name: str) -> str:
    """Return the qualified name of an extension given its name."""
    for module in walk_extensions():
        if unqualify(module) == name:
            return module
    log.error(f"Extension {name} not found.")
    raise ValueError(f"Extension {name} not found.")


EXTENSION = frozenset(walk_extensions())
