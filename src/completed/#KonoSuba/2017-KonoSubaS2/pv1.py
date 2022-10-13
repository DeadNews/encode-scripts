import dnfunc as dn

# -----in----- #
epname = dn.fname(__file__)

epis = dn.source(f"./in/{epname}.mp4")
# ------------ #

# ----mrgc---- #
aaep = dn.aa(epis)
mrgc = aaep
mrgc = dn.rfs_dehalo(mrgc)
# ------------ #

# ----filt---- #
F1 = dn.filt(mrgc, zone="oped")
F3 = dn.filt(mrgc, zone="limb")
F4 = dn.filt(mrgc, zone="noise")

F1 = dn.rfs(F1, F3, [(995, 1031)])
F1 = dn.rfs(F1, F4, [(792, 994)])
# ------------ #

# ----out----- #
clip = dn.out(F1, epname)
clip.set_output()
# ------------ #

# ----save---- #
# dn.pw(mrgc, [1, 2, 3, 4, 6], 'main', epis, clip, 'old').set_output()
"""
"""
# epis.set_output()
# clip.std.Trim(792, 994).set_output()
# ------------ #

# ----err----- #
dn.check_num_frames(epis, clip)
# ------------ #
