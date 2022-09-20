import dnfunc as dn

# -----in----- #
epname = dn.fname(__file__, mode="aa")
desc_h = 846

epis = dn.source(f"./in/{epname}.mkv")

# -----aa----- #
aaep = dn.aa(epis, desc_h=desc_h)
# ------------ #

# ----out----- #
aaep.set_output()
# ------------ #
