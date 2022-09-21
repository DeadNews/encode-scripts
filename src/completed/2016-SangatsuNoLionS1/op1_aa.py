import dnfunc as dn

# -----in----- #
epname = dn.fname(__file__, mode="aa")
kernel, desc_h = "bilinear", 719

epis = dn.source(f"./in/{epname}.mp4")
# ------------ #

# -----aa----- #
aaep = dn.aa(epis, desc_h=desc_h, kernel=kernel)
# ------------ #

# ----out----- #
aaep.set_output()
# ------------ #
