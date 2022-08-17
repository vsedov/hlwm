from herbstluftwm.log import get_logger
from herbstluftwm.utils.extension import EXTENSION
from herbstluftwm.utils.utils import set_delimit_function
from herbstluftwm.utils.utils_misc import contains

log = get_logger(__name__)


def inital_setup():
    for ext in EXTENSION:

        if contains(str(ext), "magic"):
            log.info("Inside Magic")
            set_delimit_function(ext)
            log.info(f"Running {ext}")
