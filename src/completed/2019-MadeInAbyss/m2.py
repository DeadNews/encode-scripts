import dnfunc as dn
from vapoursynth import core

# -----in----- #
epname = dn.fname(__file__)

epis = dn.source(f"./in/{epname}.mp4")
# ------------ #

# ----out----- #
clip = core.fmtc.bitdepth(epis, bits=10)
clip.set_output()
# ------------ #
