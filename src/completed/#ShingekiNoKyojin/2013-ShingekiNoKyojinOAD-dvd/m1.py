import dnfunc as dn

# -----in----- #
# epname = dn.fname(__file__)
epname = "m8"

epis = dn.source(f"./in/{epname}.mp4")
# ------------ #

# ----mrgc---- #
mrgc = epis
mrgc = dn.rfs_dehalo(mrgc, zone="menu")

mrgc = dn.rescale_(mrgc, mode="insane_aa", width=1920, height=1080)
# ------------ #

# ----filt---- #
F1 = dn.filt(mrgc, zone="menu")
# ------------ #

# ----out----- #
clip = dn.out(F1, epname)
clip.set_output()
dn.downscale(clip, 576).set_output()
# ------------ #

# ----save---- #
# dn.pw(mrgc, None, None, epis_back, clip).set_output()
"""
"""
# epis.set_output()
# ------------ #

# ----err----- #
dn.check_num_frames(epis, clip)
# ------------ #
