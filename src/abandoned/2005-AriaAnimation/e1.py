import dnfunc as dn

# -----in----- #
epname = dn.fname(__file__)

epis = dn.source(
    "/run/media/deadnews/data1/temp/ARIA SEASON ONE BD/ARIAS1BD1/BDMV/STREAM/00002.m2ts"
)
# ------------ #

# ----mrgc---- #
epis = epis.std.CropRel(top=6, bottom=6, left=246, right=246)
epis_back = epis
epis = epis.edgefixer.Continuity(top=4, bottom=1, left=4, right=2)
# black bar top
# ------------ #

# ----mrgc---- #
aaep = dn.aa(epis)
mrgc = aaep

mrgc = dn.rfs_dehalo(mrgc)
mrgc = dn.rfs_dehalo(mrgc, zone="2nd")
# mrgc = rfs_dehalo(mrgc, zone='3nd')

mrgc = dn.qtgmc(mrgc, k=1.0, sharp=0.0)  # <<<
# ------------ #

# ----filt---- #
F1 = dn.filt(mrgc)
# ------------ #

# ----out----- #
clip = dn.out(F1, epname)
clip.set_output()
clip.resize.Spline36(964, 720).set_output()
# ------------ #

# ----save---- #
# pw(mrgc, None, None, epis_back, clip).set_output()
"""
1834 37527
---1
124 37527 18763
"""
# epis.set_output()
# clip.std.Trim(18668, 19141).set_output()
# ------------ #

# ----err----- #
dn.check_num_frames(epis, clip)
# ------------ #
