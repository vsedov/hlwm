import builtins

from herbstluftwm.config.keybinds import setup_binds
from herbstluftwm.helper.magic import hc
from herbstluftwm.log import get_logger
from herbstluftwm.setup.module_load import inital_setup

log = get_logger(__name__)
inital_setup()

#  TODO(vsedov) (01:16:12 - 17/08/22): Should i be using builtins, or should i
#  import the modules ?
#
# builtins.hc = hc

#  TODO(vsedov) (01:18:57 - 17/08/22): This is temp, i have to setup the call as well properly
# remove this function once you have time .
# x = setup_binds()
# __import__('pprint').pprint(x)
