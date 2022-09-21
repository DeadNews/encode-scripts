import dnfunc as dn
from vapoursynth import core

# -----in----- #
epname = "e1"
jpn = dn.source(f"./in/{epname}.mp4")
ita = dn.source(f"./in/2nd/{epname}.mp4")
epis = dn.average([jpn, ita])

epis, epis_back, edgefixer = dn.edgefix(epis)
# ------------ #

rt0 = dn.retinex_edgemask(epis, 1)
rt1 = rt0.std.Expr("x 1000 +")

core.std.Interleave([rt0, rt1]).set_output()
