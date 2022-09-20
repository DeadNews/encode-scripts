import dnfunc as dn

# -----in----- #
epname = dn.fname(__file__)

epis = dn.source(f"./in/{epname}.mp4")
# epis, epis_back, edgefixer = dn.edgefix(epis)
# ------------ #

# -----aa----- #
# aaep = dn.aa(epis, epname)
# mrgc = aaep
mrgc = epis
# ------------ #

# ----filt---- #
F1 = dn.filt(mrgc, zone="op")
# ------------ #

# ----out----- #
clip = dn.out(F1, epname)
clip.set_output()
# ------------ #

# ----save---- #
# dn.pw4(mrgc, 2, 1, epis, clip).set_output()
# 5314
# epis.set_output()
# ------------ #

# ----err----- #
dn.check_num_frames(epis, clip)
# ------------ #
