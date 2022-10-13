import dnfunc as dn

# -----in----- #
epname = dn.fname(__file__)
kernel, desc_h = "bicubic", 720

OP = 11456
OPend = 12985
ED = 158375
EDend = 165757

epis = dn.source(f"./in/{epname}.mp4")
# ------------ #

# ----mrgc---- #
aaep = dn.aa(epis, desc_h=desc_h, kernel=kernel)
op = dn.oped(epis, name="op3", offset=566, start=OP, end=OPend, desc_h=desc_h)
ed = epis.std.Trim(ED, EDend - 1)

mrgc = (
    aaep.std.Trim(0, OP - 1)
    + op
    + aaep.std.Trim(OPend, ED - 1)
    + ed
    + aaep.std.Trim(EDend, epis.num_frames - 1)
)
# ------------ #

# ----mask---- #
mrgc = dn.rfs(mrgc, epis, [(167194, 167635)])
mrgc = dn.rfs_image(mrgc, epis, "3", [(11032, 11157)])
mrgc = dn.rfs_resc(
    mrgc,
    epis,
    desc_h=desc_h,
    mthr=100,
    maps=[
        (24379, 24419),
        (24498, 24521),
        (24675, 24737),
        (24780, 24863),
        (26521, 26568),
        (40662, 40706),
        (40798, 40851),
        (59963, 59978),
        (60156, 60230),
        (61206, 61262),
        (62859, 62959),
        (65091, 65109),
        (65582, 65603),
        (67318, 67385),
        (67560, 67591),
        (67610, 67646),
    ],
)

mrgc = dn.rfs_hard(mrgc, mrgc, mthr=99, maps=[(21444, 21476)])
# ------------ #

# -----in----- #
"""
def filt_old(
    mrgc=mrgc,
    sm_thr=48,
    tr=48,
    pref=1,
    cs_mode=99,
    cs_val=0.55,
    db_thr=1.0,
    db_mode=3,
    db_det=64,
    db_grain=48,
    db_range=10,
    db_saveblack=2,
    rt_sigma=0.9,
    out_mode=0,
):
"""

F1 = dn.filt(mrgc)
F2 = dn.filt(mrgc, db_thr=0, cs_mode=0, sm_thr=2000)
F6 = dn.adaptive_grain(F2, strength=1.5, luma_ag_scaling=60)
F3 = dn.filt(mrgc, sm_thr=35, rt_sigma=0.7, db_grain=8, db_range=5)
F4 = dn.filt(mrgc, db_saveblack=0)
F5 = dn.filt(mrgc, db_thr=1.1, sm_thr=50)

F1 = dn.rfs(F1, F6, [(ED, EDend - 1)])
F1 = dn.rfs(
    F1,
    F3,
    [
        (21047, 21146),
        (21182, 21443),
        (21477, 21565),
        (21882, 22505),
        (22593, 22885),
        (23213, 23366),
        (23486, 23568),
        (23821, 23945),
        (37776, 37875),
    ],
)
F1 = dn.rfs(F1, F4, [(59092, 59133)])
F1 = dn.rfs(
    F1,
    F5,
    [
        (0, 353),
        (26796, 26885),
        (56630, 56653),
        (60130, 60237),
        (68293, 68340),
        (81952, 82017),
        (89659, 89690),
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
# clip.std.Trim(0, 1593).set_output()
# dn.rfs_resc(mrgc, epis, desc_h=desc_h, mthr=100, out_mask=True).set_output()
# ------------ #

# ----err----- #
dn.check_num_frames(epis, clip)
# ------------ #
