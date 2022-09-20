import dnfunc as dn

# -----in----- #
epname = dn.fname(__file__, mode="aa")

epis = dn.source(f"./in/{epname}.mp4")
# ------------ #

# -----aa----- #
aaep = dn.aa(epis)
# ------------ #

# ----out----- #
aaep.set_output()
# ------------ #
