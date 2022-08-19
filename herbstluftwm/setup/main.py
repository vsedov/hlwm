# flake8: noqa
# type: ignore
from herbstluftwm.config.attributes import setup_attributes
from herbstluftwm.config.keybinds import setup_binds
from herbstluftwm.helper.magic import delimit_str, hc, hc_register
from herbstluftwm.log import get_logger, setup
from herbstluftwm.setup.module_load import inital_setup

log = get_logger(__name__)

inital_setup()
