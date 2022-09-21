import dnfunc as dn

# -----in----- #
epname = "e1"

epis = dn.source(f"./in/{epname}.mp4")
# ------------ #

# -----ag----- #
scaling = 40
# scaling = 4
# scaling = 1

adaptive_mask = dn.adaptive_grain(epis, luma_scaling=scaling, show_mask=True)

adaptive_mask.std.Invert().set_output()
# adaptive_mask.set_output()
# ------------ #

# ----split---- #
# dn.split(epis)[1].set_output()
# ------------ #

"""

"""
