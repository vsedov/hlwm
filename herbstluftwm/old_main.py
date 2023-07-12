import herbstluftwm.constants as const
from herbstluftwm.helper.utils import bind_cycle_layout, chain, do_config, hc_run, rotate, startup_run, system_run
from herbstluftwm.log import get_logger

log = get_logger(__name__)

tag_names = list(range(1, 10))
tag_keys = list(range(1, 10)) + [0]

hc_run("emit_hook reload")
system_run("echo 35 > /tmp/herbstluftwm-gap")
hc_run("lock")
# standard
# remove all existing keybindings
hc_run('keyunbind --all')
hc_run("mouseunbind --all")
hc_run("unrule -F")
bind_cycle_layout()

layout = "(split horizontal:0.5:0 " \
         "(clients vertical:0) (clients vertical:0))"
hc_run(f"load {str(tag_names[0])} '{layout}'")

# tag number 5
hc_run("floating 5 on")

# hc("set tree_style '╾│ ├└╼─┐'")
hc_run("set tree_style '⊙│ ├╰»─╮'")

# unlock, just to be sure
hc_run("unlock")

# load on startup
startup_run(const.STARTUP)
