import dnfunc as dn

# -----in----- #
epname = dn.fname(__file__)
desc_h = 720

OP = 0
Chapter_30 = 1440
Chapter_31 = 8349
Chapter_32 = 18607
Chapter_33 = 32494
ED = 44119

epis = dn.source(f"./in/{epname}.mkv")
# ------------ #

# ----mrgc---- #
aaep = dn.aa(epis, desc_h=desc_h)
mrgc = aaep
# ------------ #

# ----mask---- #
mrgc = dn.rfs_hard(mrgc, mrgc, mthr=2, maps=[(3671, 3925)])
mrgc = dn.rfs_hard(
    mrgc,
    mrgc,
    mthr=12,
    maps=[(3112, 3188), (3995, 4042), (6144, 6269), (11482, 11814), (11863, 12209)],
)
mrgc = dn.rfs_hard(
    mrgc,
    mrgc,
    mthr=32,
    maps=[(1476, 1577), (1578, 1625), (1953, 2000), (2295, 2354), (2124, 2240)],
)

stabilize_2 = dn.qtgmc(aaep, ThSAD1=492, ThSAD2=197, ThSCD1=139, ThSCD2=75)
mrgc = dn.rfs(mrgc, stabilize_2, [(2550, 2765), (2766, 3036)])

hard = dn.hard(mrgc, mthr=9)
stabilize_1 = dn.qtgmc(hard)
mrgc = dn.rfs_image(mrgc, stabilize_1, "e6 1864", [(1864, 1928)])
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
F0 = F1
F2 = dn.filt(mrgc, db_saveblack=0)
F3 = dn.filt(mrgc, db_saveblack=0, sm_thr=70)
F4 = dn.filt(mrgc, sm_thr=70)
F5 = dn.filt(mrgc, db_mode=2)
F6 = dn.filt(mrgc, db_mode=1)
F7 = dn.filt(mrgc, sm_thr=30, db_thr=1)
F8 = dn.filt(mrgc, sm_thr=120)
F9 = dn.filt(mrgc, sm_thr=160, db_thr=0)
F10 = dn.filt(mrgc, db_thr=0)
F11 = dn.filt(mrgc, db_saveblack=0, sm_thr=30, db_thr=1)
F12 = dn.filt(mrgc, db_saveblack=0, sm_thr=500, db_mode=1, db_thr=3, db_grain=58)

F1 = dn.rfs(F1, F2, [(3112, 7268), (12656, 12967), (12968, 13087), (16074, 16193), (16714, 16822)])
F1 = dn.rfs(F1, F0, [(3671, 3925), (4827, 5157), (5901, 5918), (6270, 6353), (6423, 6500)])
F1 = dn.rfs(F1, F3, [(4085, 4144), (5655, 5900), (6036, 6144)])
F1 = dn.rfs(F1, F4, [(8227, 8325), (5901, 5918), (10748, 10804), (14563, 14912)])
F1 = dn.rfs(
    F1,
    F5,
    [
        (7920, 8111),
        (10022, 10147),
        (10805, 10888),
        (16950, 16976),
        (17640, 17883),
        (17945, 17961),
        (19686, 19887),
        (29528, 29563),
    ],
)
F1 = dn.rfs(F1, F6, [(4307, 4376), (25375, 25481)])
F1 = dn.rfs(
    F1,
    F7,
    [
        (9878, 10021),
        (10667, 10747),
        (11134, 11163),
        (23964, 24109),
        (18976, 19219),
        (28053, 28088),
    ],
)
F1 = dn.rfs(F1, F8, [(11242, 11274)])
F1 = dn.rfs(F1, F9, [(13088, 13159), (13685, 13822)])
F1 = dn.rfs(F1, F10, [(14464, 14562)])
F1 = dn.rfs(F1, F11, [(15951, 16073), (27750, 27794), (4630, 4691), (6501, 6644), (7152, 7244)])
F1 = dn.rfs_image(F1, F3, "e6 63998", [(15951, 16073)])
F1 = dn.rfs_image(F1, F12, "e6 14107v2", [(3432, 3630)])
# ------------ #

# ----out----- #
clip = dn.out(F1, epname)
clip.set_output()
# ------------ #

# ----save---- #
# dn.pw4(mrgc, 2, 1, epis, clip).set_output()
# epis.set_output()
# clip.std.Trim(3432, 3648).set_output()
# clip.std.Trim(2550, 3036).set_output()
# clip.std.Trim(1864, 1928).set_output()

# dn.rfs_resc(mrgc, epis, desc_h=desc_h, mthr=50, out_mask=True).set_output()
# ------------ #

# ----err----- #
dn.check_num_frames(epis, clip)
# ------------ #
