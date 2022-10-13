import dnfunc as dn

# -----in----- #
epname = dn.fname(__file__)
desc_h = 720

ED = 32609
EDend = 34766

epis = dn.source(f"./in/{epname}.mkv")
# ------------ #

# ----mrgc---- #
ed = dn.oped(epis, name="ed2", offset=12, start=ED, end=EDend, desc_h=desc_h)

aaep = dn.aa(epis, desc_h=desc_h)

mrgc = aaep.std.Trim(0, ED - 1) + ed + aaep.std.Trim(EDend, epis.num_frames - 1)
# ------------ #

# ----mask---- #
mrgc = dn.rfs_qtgmc(mrgc, aaep, k=0.77, maps=[(5900, 6100)])
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
F2 = dn.filt(mrgc, db_saveblack=0)
F3 = dn.filt(mrgc, db_mode=2)
F4 = dn.filt(mrgc, db_saveblack=0, sm_thr=80, db_grain=58, rt_sigma=0.7)
F5 = dn.filt(mrgc, db_saveblack=0, rt_sigma=0.8, db_thr=1)
F6 = dn.filt(mrgc, rt_sigma=0.8, db_thr=1)
F7 = dn.filt(mrgc, sm_thr=25, db_thr=1, rt_sigma=0.4)
F8 = dn.filt(mrgc, db_mode=1)
F9 = dn.filt(mrgc, db_saveblack=0, sm_thr=100, db_mode=1, rt_sigma=4, db_grain=58)
F10 = dn.filt(mrgc, rt_sigma=0.7, db_thr=1)
F11 = dn.filt(mrgc, db_mode=2, rt_sigma=0.7)

F1 = dn.rfs(F1, F2, [(12858, 12926)])
F1 = dn.rfs(
    F1,
    F3,
    [
        (4727, 4855),
        (4934, 4980),
        (5010, 5302),
        (30894, 30931),
        (30894, 30931),
        (20560, 20643),
        (20903, 21058),
    ],
)
F1 = dn.rfs_image(F1, F4, "e3 10417", [(10417, 10464), (10498, 10578)])
F1 = dn.rfs_image(F1, F2, "e3 10705", [(10705, 10740), (10870, 10901), (11094, 11058)])
F1 = dn.rfs_image(F1, F4, "e3 11663", [(11663, 11806)])
F1 = dn.rfs_image(F1, F4, "e3 12633", [(12633, 12857)])
F1 = dn.rfs(F1, F4, [(12088, 12122)])
F1 = dn.rfs(F1, F10, [(21548, 21710)])
F1 = dn.rfs(F1, F11, [(22078, 22110)])

F1 = dn.rfs_image(F1, F5, "crop2", [(22445, 25109)])  # 1nd half of the last chapter
F1 = dn.rfs(F1, F6, [(25110, ED - 1)])  # 2nd half of the last chapter
F1 = dn.rfs_image(
    F1,
    F5,
    "crop2",
    [
        (25637, 25667),
        (25977, 26066),
        (26458, 26535),
        (26578, 26625),
        (26932, 26989),
        (27550, 27614),
        (27918, 28102),
        (28103, 28169),
        (28776, 28823),
        (28911, 28982),
        (31736, 31867),
        (32186, 32217),
        (32299, 32333),
        (32494, 32553),
    ],
)  # fix for 2 half
F1 = dn.rfs(
    F1, F6, [(23107, 23277), (23651, 23687), (24257, 24430), (24675, 24748)]
)  # fix for 1 half
F1 = dn.rfs(F1, F7, [(23687, 23734), (24551, 24634)])
F1 = dn.rfs(F1, F8, [(27248, 27267), (26932, 26989)])
F1 = dn.rfs_image(F1, F5, "e3 31962", [(31909, 31962), (32035, 32185)])
F1 = dn.rfs_image(F1, F2, "crop2", [(22484, 22694), (24143, 24220), (27918, 27968)])

sb_filt = dn.rfs_color(F1, F9, mask_src=mrgc)
F1 = dn.rfs_image(
    F1,
    sb_filt,
    "crop2",
    [
        (22484, 22694),
        (23834, 24112),
        (24143, 24220),
        (24658, 24674),
        (24846, 24908),
        (26932, 26989),
        (27969, 28102),
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
# clip.std.Trim(27918, 28102).set_output()
# output = clip[22484:22694] + clip[23834:24112] + clip[24143:24220] + clip[24658:24674] + clip[24846:24908] + clip[26932:26989] + clip[27918:28102]; output.set_output()

# dn.rfs_resc(mrgc, epis, desc_h=desc_h, mthr=50, out_mask=True).set_output()
# ------------ #

# ----err----- #
dn.check_num_frames(epis, clip)
# ------------ #
