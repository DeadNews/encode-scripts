import dnfunc as dn

# -----in----- #
epname = dn.fname(__file__)

ita = dn.source(f"./in/ita/{epname}.mp4")[24:]
jpn = dn.source(f"./in/{epname}.mp4")
# ------------ #

# -----aa----- #
jpn = dn.rfs_image(jpn, ita, "s1s2", yuv=True)
maps = [
    26,
    65,
    (1342, 1343),
    1372,
    1387,
    1392,
    (1394, 1395),
    (1401, 1408),
    1410,
    1412,
    1414,
    1416,
    1418,
    1420,
    1422,
    (1430, 1459),
    1545,
    1647,
    1655,
    4639,
    4642,
    4663,
    4667,
    4675,
    4687,
    (4694, 4695),
    4751,
    4765,
    8946,
    8949,
    8972,
    9007,
    9020,
    9107,
    9116,
    9146,
    9206,
    9208,
    (9384, 9386),
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
7030
"""
# epis.set_output()
# ------------ #

# ----err----- #
dn.check_num_frames(epis, clip)
# ------------ #
