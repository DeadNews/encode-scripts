import dnfunc as dn

# -----in----- #
epname = dn.fname(__file__)

ita = dn.source(f"./in/ita/{epname}.mp4")[24:]
jpn = dn.source(f"./in/{epname}.mp4")
# ------------ #

# -----aa----- #
jpn = dn.rfs_image(jpn, ita, "s1s2", yuv=True)
maps = [
    27,
    57,
    69,
    (2264, 2325),
    (2353, 2355),
    (2365, 2367),
    (2386, 2388),
    (2398, 2400),
    (2410, 2412),
    4399,
    4437,
    4920,
    5684,
    6117,
    6119,
    (6122, 6123),
    (6126, 6129),
    (6132, 6133),
    (6136, 6138),
    (6142, 6143),
    (6146, 6147),
    8898,
    8902,
    8904,
    8912,
    8928,
    8931,
    8936,
    8938,
    9132,
    9136,
    9215,
]
epis = dn.rfs_diff(ita, jpn, maps=maps)

mrgc = dn.rfs_dehalo(epis)
mrgc = dn.rfs_repair(mrgc)
# ------------ #

# ----filt---- #
F1 = dn.filt(mrgc, zone="sp")
# ------------ #

# ----out----- #
clip = dn.out(F1, epname)
clip.set_output()
# ------------ #

# ----save---- #
# dn.pw(mrgc, None, None, epis, clip).set_output()
# dn.pw(mrgc, [2, 3, 4, 6], 'main', epis, clip).set_output()
"""
"""
# epis.set_output()
# ------------ #

# ----err----- #
dn.check_num_frames(epis, clip)
# ------------ #
