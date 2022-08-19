import builtins

from herbstluftwm.config.keybinds import setup_binds
from herbstluftwm.helper.magic import hc
from herbstluftwm.log import get_logger
from herbstluftwm.setup.main import setup

log = get_logger(__name__)
setup()
# Load in all the modules
log.info("All Modules Loaded")
