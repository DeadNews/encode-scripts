import dnfunc as dn

# -----in----- #
epname = dn.fname(__file__)
desc_h = 720

OP = 1702
OPend = 3860
ED = 34766

epis = dn.source(f"./in/{epname}.mkv")
EDend = epis.num_frames - 39
# ------------ #

# ----mrgc---- #
op = dn.oped(epis, name="op3", offset=12, start=OP, end=OPend, desc_h=desc_h)
ed = dn.oped(epis, name="ed1", offset=12, start=ED, end=EDend, desc_h=desc_h)

aaep = dn.aa(epis, desc_h=desc_h)

mrgc = (
    aaep.std.Trim(0, OP - 1)
    + op
    + aaep.std.Trim(OPend, ED - 1)
    + ed
    + aaep.std.Trim(EDend, epis.num_frames - 1)
)
# ------------ #

# ----mask---- #
mrgc = dn.rfs_qtgmc(mrgc, aaep, maps=[(891, 1160), (25791, 25814), (26563, 26607)])

stabilize = dn.qtgmc(mrgc)
mrgc = dn.rfs_image(mrgc, stabilize, "e5 20556", [(20556, 20579)])
mrgc = dn.rfs_image(mrgc, stabilize, "e5 23535", [(23535, 23555)])
mrgc = dn.rfs_image(mrgc, stabilize, "e5 24256-2", [(26608, 26973), (27040, 27258)])
mrgc = dn.rfs_image(mrgc, stabilize, "e5 7735", [(7735, 8001)])
mrgc = dn.rfs_image(mrgc, stabilize, "e5 8414", [(8414, 8437)])

mrgc = dn.rfs_hard(
    mrgc,
    mrgc,
    mthr=20,
    maps=[
        (21224, 21237),
        (21795, 21811),
        (23706, 23745),
        (24532, 24561),
        (25791, 25814),
        (26563, 26607),
        (10325, 10461),
        (10510, 10684),
    ],
)
mrgc = dn.rfs_hard(mrgc, mrgc, mthr=80, maps=[(30766, 30903)])

hard_1 = dn.hard(mrgc, mthr=10)
mrgc = dn.rfs_image(
    mrgc,
    hard_1,
    "e5 24256",
    [
        (24256, 24495),
        (24562, 25013),
        (25068, 25235),
        (25383, 25562),
        (25961, 26260),
        (26608, 26973),
        (27040, 27258),
    ],
)
mrgc = dn.rfs_image(mrgc, hard_1, "e5 27996", [(27668, 27997)])

hard_2 = dn.hard(mrgc, mthr=20)
mrgc = dn.rfs_image(mrgc, hard_2, "e5 7735", [(7735, 8001)])
mrgc = dn.rfs_image(mrgc, hard_2, "e5 8414", [(8414, 8437)])
mrgc = dn.rfs_image(mrgc, hard_2, "e5 14977", [(14972, 15066)])
mrgc = dn.rfs_image(mrgc, hard_2, "e5 17343", [(17343, 17583)])
mrgc = dn.rfs_image(mrgc, hard_2, "e5 19019", [(18985, 19019)])
mrgc = dn.rfs_image(mrgc, hard_2, "e5 20427", [(20427, 20447)])
mrgc = dn.rfs_image(mrgc, hard_2, "e5 22365", [(22355, 22576)])
mrgc = dn.rfs_image(mrgc, hard_2, "e5 22838", [(22838, 22900)])
mrgc = dn.rfs_image(mrgc, hard_2, "e5 31368", [(31368, 31406)])
mrgc = dn.rfs_image(mrgc, hard_2, "e5 32161", [(32161, 32208)])
mrgc = dn.rfs_image(mrgc, hard_2, "e5 21658", [(21658, 21748)])

hard_3 = dn.hard(mrgc, mthr=70)
mrgc = dn.rfs_image(mrgc, hard_3, "e5 24010", [(24010, 24144)])
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
F2 = dn.filt(mrgc, rt_sigma=0.8, db_saveblack=0)
F3 = dn.filt(mrgc, db_mode=1, db_saveblack=0)
F4 = dn.filt(mrgc, db_mode=2, db_saveblack=0)
F5 = dn.filt(mrgc, sm_thr=45, db_thr=1, rt_sigma=0.8)
F6 = dn.filt(mrgc, sm_thr=44, db_thr=1, rt_sigma=0.7)
F7 = dn.filt(mrgc, sm_thr=4, db_thr=0, rt_sigma=0.6)
F8 = dn.filt(mrgc, sm_thr=300, db_thr=6, db_mode=1, rt_sigma=4, db_det=128)
F9 = dn.filt(mrgc, db_mode=1)
F10 = dn.filt(mrgc, db_mode=2)
F11 = dn.filt(mrgc, db_thr=1, rt_sigma=0.8)

F1 = dn.rfs(F1, F2, [(ED, EDend - 1 - 24)])
F1 = dn.rfs(F1, F3, [(OP + 33, OP + 95)])
F1 = dn.rfs(F1, F4, [(OP + 96, OP + 157)])
F1 = dn.rfs(
    F1,
    F5,
    [
        (10325, 10461),
        (10510, 10684),
        (10913, 11007),
        (22814, 22837),
        (22950, 23012),
        (27378, 27542),
        (28319, 28337),
        (31237, 31292),
        (31573, 31734),
        (31951, 32028),
        (34319, 34765),
    ],
)
F1 = dn.rfs(
    F1,
    F6,
    [
        (25749, 25790),
        (26348, 26362),
        (26416, 26428),
        (26486, 26530),
        (26974, 27039),
        (27998, 28318),
    ],
)
F1 = dn.rfs(F1, F7, [(21005, 21106)])
F1 = dn.rfs(F1, F9, [(13079, 13182), (19621, 19640), (22783, 22813), (23640, 23675)])
F1 = dn.rfs(
    F1,
    F10,
    [(3944, 4951), (11245, 11302), (11460, 11682), (18914, 18967), (20123, 20158), (21432, 21455)],
)
F1 = dn.rfs(F1, F11, [(23068, 23138)])

F1 = dn.rfs_image(F1, F8, "e5 20447", [(20427, 20447)])
F1 = dn.rfs_image(F1, F8, "e5 27997", [(27668, 27997)])
# ------------ #

# ----out----- #
clip = dn.out(F1, epname)
clip.set_output()
# ------------ #

# ----save---- #
# dn.pw4(mrgc, 2, 1, epis, clip).set_output()
# epis.set_output()
# clip.std.Trim(8414, 8437).set_output()

# dn.rfs_resc(mrgc, epis, desc_h=desc_h, mthr=50, out_mask=True).set_output()
# ------------ #

# ----err----- #
dn.check_num_frames(epis, clip)
# ------------ #
