import dnfunc as dn
from vapoursynth import core

# -----in----- #
# epname = 's2'
epname = "e1"

epis = dn.source(f"./in/{epname}.mp4")
# epis = dn.source(f'./in/{epname}.m2ts')
# ------------ #

ag_scaling = 40
# ag_scaling = 4
# ag_scaling = 4

# adaptive_mask = dn.kg.adaptive_grain(epis, luma_ag_scaling=ag_scaling, show_db_mode=True)
# adaptive_mask.std.Invert().set_output()
# adaptive_mask.set_output()

# dn.split(epis)[1].set_output()

# 30057

m1 = dn.edge_detect(epis, mode="sobel")
m2 = dn.edge_detect(epis, mode="kirsch2")
m3 = dn.edge_detect(epis, mode="fine2")
m4 = core.std.Expr([m2, m3], "x y -")

m5 = dn.outerline_mask(epis, ext_db_mode=m2, max_c=1)
m6 = core.std.Expr([m2, m5], "x y -")

m4.set_output()
# s2 3818
# e1 19450
