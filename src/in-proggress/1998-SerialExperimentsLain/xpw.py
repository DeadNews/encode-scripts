import dnfunc as dn
from vapoursynth import core

# ---------- #

# ----in---- #
epname = "e1"
epis = dn.source(f"./in/{epname}.mp4")
epis16 = core.fmtc.bitdepth(epis, bits=16)

scaling = 20
# scaling = 4
# scaling = 1

adaptive_mask = dn.kg.adaptive_grain(epis16, luma_scaling=scaling, show_mask=True)

adaptive_mask.std.Invert().set_output()
# adaptive_mask.set_output()

# dn.planes(epis)[1].set_output()
