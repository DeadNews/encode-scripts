import dnfunc as dn

# -----in----- #
epname = dn.fname(__file__)

epis = dn.source(f"./in/{epname}.mp4", fpsnum=24000, fpsden=1001)
# ------------ #

# ----mrgc---- #
epis = dn.crop(epis)[0]
epis, epis_back, _ = dn.edgefix(epis)

mrgc = dn.rescale_(epis, width=1920)
# ------------ #

# ----filt---- #
F1 = dn.filt(mrgc, zone="e5")
# ------------ #

# ----out----- #
clip = dn.out(F1, epname)
clip.set_output()
# ------------ #

# ----save---- #
# epis_back = dn.rescale_(epis_back, width=1920, mode="lanczos")
# dn.pw(mrgc, None, None, epis_back, clip).set_output()
# dn.pw(mrgc, [2, 3, 4, 6], 'main', epis_back, clip).set_output()
"""
1:
2: 10212 11076
6:
"""
# epis.set_output()
# ------------ #

# ----err----- #
dn.check_num_frames(epis, clip)
# ------------ #
