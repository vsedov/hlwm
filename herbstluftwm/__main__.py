import herbstluftwm.constants as const
from herbstluftwm.log import get_logger
from herbstluftwm.helper.utils import (
    bind_cycle_layout,
    chain,
    do_config,
    hc,
    rotate,
    startup_run,
    system_run,
)

log = get_logger(__name__)

tag_names = list(range(1, 10))
tag_keys = list(range(1, 10)) + [0]

hc("emit_hook reload")
system_run("echo 35 > /tmp/herbstluftwm-gap")
hc("lock")
# standard
# remove all existing keybindings
hc('keyunbind --all')
hc("mouseunbind --all")
hc("unrule -F")
bind_cycle_layout()

layout = "(split horizontal:0.5:0 " \
         "(clients vertical:0) (clients vertical:0))"
hc("load " + str(tag_names[0]) + " '" + layout + "'")

# tag number 5
hc("floating 5 on")

# hc("set tree_style '╾│ ├└╼─┐'")
hc("set tree_style '⊙│ ├╰»─╮'")

# unlock, just to be sure
hc("unlock")

# load on startup
startup_run(const.STARTUP)
