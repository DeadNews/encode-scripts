import dnfunc as dn

# -----in----- #
epname = dn.fname(__file__)
desc_h = 720

OP = 528
OPend = 2688
ED = 41721
EDend = 43879

epis = dn.source(f"./in/{epname}.mkv")
# ------------ #

# ----mrgc---- #
op = dn.oped(epis, name="op1", offset=12, start=OP, end=OPend, desc_h=desc_h)
ed = dn.oped(epis, name="ed2", offset=12, start=ED, end=EDend, desc_h=desc_h)

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
mrgc = dn.rfs(mrgc, aaep, [(OP + 713, OP + 873)])

stabilize = dn.qtgmc(aaep)
mrgc = dn.rfs(mrgc, stabilize, [(18235, 18498)])
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
F2 = dn.filt(mrgc, sm_thr=45, db_thr=1, rt_sigma=0.8)
F3 = dn.filt(mrgc, sm_thr=300, db_thr=6, db_mode=1, rt_sigma=4, db_det=128)
F4 = dn.filt(mrgc, db_mode=1, db_thr=2, rt_sigma=1.1, sm_thr=100, db_grain=58)
F5 = dn.filt(mrgc, db_mode=2)
F6 = dn.filt(mrgc, db_saveblack=0, sm_thr=45, db_thr=1, rt_sigma=0.8)
F7 = dn.filt(mrgc, db_saveblack=0)
F8 = dn.filt(mrgc, db_saveblack=0, sm_thr=100, db_mode=1, rt_sigma=4, db_grain=58)
F9 = dn.filt(mrgc, db_saveblack=0, db_mode=2)

F1 = dn.rfs(F1, F2, [(0, 527), (3507, 32511)])
F1 = dn.rfs(
    F1,
    F0,
    [
        (8199, 8217),
        (12924, 12947),
        (14199, 14216),
        (30746, 30781),
        (31859, 31924),
        (9687, 10177),
        (10190, 10271),
        (10734, 10931),
        (10950, 11066),
        (11331, 11645),
    ],
)
F1 = dn.rfs(F1, F4, [(3006, 3024), (3186, 3221), (3222, 3326)])
F1 = dn.rfs(
    F1,
    F5,
    [
        (2724, 2747),
        (3043, 3096),
        (3126, 3185),
        (3351, 3374),
        (6319, 6495),
        (8421, 8438),
        (8601, 8636),
    ],
)
F1 = dn.rfs(
    F1,
    F6,
    [
        (4558, 4593),
        (4867, 4908),
        (5287, 5310),
        (8025, 8075),
        (8091, 8177),
        (8218, 8239),
        (8637, 8879),
        (12663, 12703),
        (31361, 31456),
    ],
)
F1 = dn.rfs(F1, F4, [(8439, 8462), (8565, 8579), (39060, 39173)])

F1 = dn.rfs_image(F1, F3, "e4 41052", [(41052, 41099)])
F1 = dn.rfs_image(F1, F3, "e4 12738", [(12738, 12779)])
F1 = dn.rfs_image(F1, F8, "e4 9618", [(9618, 9668), (10488, 10625)])
F1 = dn.rfs_image(F1, F9, "e4 12593", [(12593, 12628)])

F1 = dn.rfs_color(
    F1,
    F8,
    mask_src=mrgc,
    maps=[(9687, 10177), (10190, 10271), (10734, 10931), (10950, 11066), (11331, 11645)],
)
# ------------ #

# ----out----- #
clip = dn.out(F1, epname)
clip.set_output()
# ------------ #

# ----save---- #
# dn.pw4(mrgc, 2, 1, epis, clip).set_output()
# epis.set_output()
# clip.std.Trim(2724, 3374).set_output()
# clip.std.Trim(9687, 10177).set_output()
# ------------ #

# ----err----- #
dn.check_num_frames(epis, clip)
# ------------ #
