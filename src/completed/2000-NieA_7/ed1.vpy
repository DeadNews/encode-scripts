import dnfunc as dn

# -----in----- #
epname = dn.fname(__file__)
epis = dn.source(f"./in/{epname}.mp4")
# ------------ #

# ----fix----- #
epis, _crop = dn.crop(epis)
epis, epis_back, edgefixer = dn.edgefix(epis)
# ------------ #

# ----mrgc---- #
aaep = dn.aa(epis, epname)
mrgc = aaep

mrgc = dn.rfs_dehalo(mrgc)
mrgc = dn.rfs_dehalo(mrgc, zone="2nd")
mrgc = dn.rfs_dehalo(mrgc, zone="3nd")

mrgc = dn.qtgmc(mrgc, k=1.0, sharp=0.0)
# ------------ #

# ----filt---- #
F1 = dn.filt(mrgc, zone="ed")
# ------------ #

# ----out----- #
clip = dn.out(F1, epname)

# clip.set_output()
clip.resize.Spline36(960, 720).set_output()
# ------------ #

# ----save---- #
# dn.pw4(mrgc, 2, 1, epis, clip).set_output()
# epis.set_output()
"""
"""
# ------------ #

# ----err----- #
dn.check_num_frames(epis, clip)
# ------------ #
