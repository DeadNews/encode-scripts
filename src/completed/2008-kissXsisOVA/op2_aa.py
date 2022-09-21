import dnfunc as dn

# -----in----- #
epname = dn.fname(__file__, mode="aa")

epis = dn.source(f"./in/{epname}.mp4")
epis, epis_back, edgefixer = dn.edgefix(epis)
# ------------ #

# -----aa----- #
aaep = dn.aa(epis, zone="low")
# ------------ #

# ----out----- #
aaep.set_output()
# ------------ #
