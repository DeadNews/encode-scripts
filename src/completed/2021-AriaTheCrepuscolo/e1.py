import dnfunc as dn

# -----in----- #
epname = dn.fname(__file__)

epis = dn.source(f"./in/{epname}.mp4")
# ------------ #

# ----mrgc---- #
mrgc = dn.rfs_dehalo(epis)

dehalo = dn.rfs_dehalo(mrgc, zone="2nd")
dehalo_hard = dn.rfs_dehalo(mrgc, zone="3nd")

mrgc = dn.rfs(dehalo, dehalo_hard, (82405, 85884))

eedi = dn.aa(mrgc)
mrgc = dn.rfs(mrgc, eedi, (80720, 80802))
# ------------ #

# ----filt---- #
F1 = dn.filt(mrgc)
# ------------ #

# ----out----- #
clip = dn.out(F1, epname)
clip.set_output()
# ------------ #

# ----save---- #
# dn.pw(mrgc, None, None, epis, clip).set_output()
# dn.pw(mrgc, [2, 3, 4, 6], 'main', epis, clip).set_output()
"""
2: 32072 161504 160928 61770 167606
2: 161504
2: 89102
"""
# epis.set_output()
# ------------ #

# ----err----- #
dn.check_num_frames(epis, clip)
# ------------ #
