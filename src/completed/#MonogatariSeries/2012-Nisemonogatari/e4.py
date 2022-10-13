import dnfunc as dn

# -----in----- #
epname = dn.fname(__file__)
desc_h = 720

ED = 34766
EDend = 36923

epis = dn.source(f"./in/{epname}.mkv")
# ------------ #

# ----mrgc---- #
ed = dn.oped(epis, name="ed3", offset=12, start=ED, end=EDend, desc_h=desc_h)

aaep = dn.aa(epis, desc_h=desc_h)

mrgc = aaep.std.Trim(0, ED - 1) + ed + aaep.std.Trim(EDend, epis.num_frames - 1)
# ------------ #

# ----mask---- #
hard = dn.hard(mrgc, mthr=40)
stabilize = dn.qtgmc(hard, k=0.77)
mrgc = dn.rfs_image(mrgc, stabilize, "e4 30890", [(30890, 31045)])
# ------------ #

# ----filt---- #
"""
def filt_old(
    mrgc=mrgc,
    sm_thr=50,
    tr=48,
    pref=1,
    cs_mode=99,
    cs_val=0.55,
    db_thr=1.1,
    db_mode=3,
    db_det=64,
    db_grain=48,
    db_range=15,
    db_saveblack=2,
    rt_sigma=0.9,
    out_mode=0,
):
"""

F1 = dn.filt(mrgc)
F2 = dn.filt(mrgc, db_mode=1)
F3 = dn.filt(mrgc, db_mode=2)

F1 = dn.rfs(
    F1, F2, [(255, 344), (1975, 1993), (2657, 2789), (2808, 2867), (5107, 5204), (11318, 11331)]
)
F1 = dn.rfs(
    F1,
    F3,
    [
        (0, 64),
        (520, 593),
        (610, 630),
        (875, 1240),
        (1439, 1700),
        (1768, 1908),
        (1936, 1974),
        (2127, 2140),
        (2157, 2250),
        (2456, 2656),
        (2868, 3029),
        (3376, 3562),
        (3599, 3634),
        (3873, 3929),
        (4034, 4048),
        (4078, 4251),
        (4294, 4535),
        (4602, 4790),
        (4845, 5009),
        (33130, 33153),
    ],
)
# ------------ #

# ----out----- #
clip = dn.out(F1, epname)
clip.set_output()
# ------------ #

# ----save---- #
# dn.pw4(mrgc, 2, 1, epis, clip).set_output()
# epis.set_output()
# clip.std.Trim(30890, 31045).set_output()

# dn.rfs_resc(mrgc, epis, desc_h=desc_h, mthr=50, out_mask=True).set_output()
# ------------ #

# ----err----- #
dn.check_num_frames(epis, clip)
# ------------ #
