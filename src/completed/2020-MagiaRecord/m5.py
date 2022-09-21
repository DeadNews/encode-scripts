import dnfunc as dn

# -----in----- #
epname = dn.fname(__file__)

epis = dn.source(f"./in/{epname}.mp4")
# ------------ #

# ----out----- #
clip = dn.depth(epis, 10)
clip.set_output()
# ------------ #
