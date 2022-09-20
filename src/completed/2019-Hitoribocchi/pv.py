import dnfunc as dn

# -----in----- #
epname = dn.fname(__file__)

epis = dn.source(f"./in/{epname}.mp4")
# ------------ #

# -----aa----- #
aaep = dn.aa(epis)
mrgc = aaep

mrgc = dn.rfs_resc(mrgc, epis, mthr=17)
# ------------ #

# ----filt---- #
F1 = dn.filt(mrgc, zone="pv")
# ------------ #

# ----out----- #
clip = dn.out(F1, epname)
clip.set_output()
# ------------ #

# ----save---- #
# dn.pw(mrgc, None, None, epis, clip).set_output()
"""
668
"""
# epis.set_output()
# ------------ #

# ----err----- #
dn.check_num_frames(epis, clip)
# ------------ #
