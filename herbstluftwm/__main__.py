from herbstluftwm.helper.magic import hc
from herbstluftwm.log import get_logger
from herbstluftwm.setup.main import inital_setup

log = get_logger(__name__)
inital_setup()

#  TODO(vsedov) (00:31:34 - 17/08/22): test this shit
log.info(hc.mod_shift("x"))
