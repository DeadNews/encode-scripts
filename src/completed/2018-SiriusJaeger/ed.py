import dnfunc as dn

# -----in----- #
epname = dn.fname(__file__)

epis = dn.source(f"./in/{epname}.mp4")
# epis, epis_back, edgefixer = dn.edgefix(epis)
# ------------ #

# -----aa----- #
aaep = dn.aa(epis, epname)
# aaep = dn.rfs_dehalo(aaep)
mrgc = aaep
# ------------ #

# ----filt---- #
F1 = dn.filt(mrgc, zone="ed")
# ------------ #

# ----out----- #
clip = dn.out(F1, epname)
clip.set_output()
# ------------ #

# ----save---- #
# dn.pw4(mrgc, 2, 1, epis_back, clip).set_output()
# dn.pw8(mrgc, 4, 7, 2, 5, 6, epis_back, clip, 0, zone='main').set_output()
# 5094
# epis.set_output()
# dn.planes(clip)[2].set_output()
# ------------ #

# ----err----- #
dn.check_num_frames(epis, clip)
# ------------ #
