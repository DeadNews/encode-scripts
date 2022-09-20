import dnfunc as dn

# -----in----- #
epname = dn.fname(__file__)

jpn = dn.source(f"./in/{epname}.mp4")
usa = dn.source(f"./in/usa/{epname}.mp4", fpsnum=24000, fpsden=1001)[24:]

epis = dn.average([jpn, usa, jpn, jpn])
# ------------ #

# ----mrgc---- #
mrgc = dn.rfs_dehalo(epis)
# ------------ #

# ----filt---- #
F1 = dn.filt(mrgc, zone="mensp")
# ------------ #

# ----out----- #
clip = dn.out(F1, epname)
clip.set_output()
# ------------ #

# ----save---- #
# dn.pw(mrgc, None, None, epis, clip).set_output()
# dn.pw(mrgc, [2, 3, 4, 6], 'main', epis, clip).set_output()
"""
4172
"""
# epis.set_output()
# ------------ #

# ----err----- #
dn.check_num_frames(epis, clip)
# ------------ #
