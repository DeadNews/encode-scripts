import dnfunc as dn

# -----in----- #
epname = dn.fname(__file__)
desc_h = 720

OP = 3693
OPend = 5851
ED = 34767

epis = dn.source(f"./in/{epname}.mkv")
EDend = epis.num_frames - 50
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
mrgc = dn.rfs_qtgmc(mrgc, aaep, maps=[(34148, 34424)])

mrgc = dn.rfs_hard(mrgc, epis, desc_h=desc_h, mthr=10, maps=[(32928, 33026)])
mrgc = dn.rfs_hard(mrgc, mrgc, mthr=20, maps=[(34058, 34147)])
mrgc = dn.rfs_hard(
    mrgc,
    mrgc,
    mthr=85,
    maps=[(10211, 10243), (31650, 31679), (32418, 32459), (34641, 34766), (34148, 34424)],
)
mrgc = dn.rfs_hard(mrgc, mrgc, mthr=99, maps=" [33156 33272] [34563 34640] [18075 18197]")

hard_def = dn.hard(mrgc, mthr=20)
mrgc = dn.rfs_image(mrgc, hard_def, "e7 8773", [(8773, 8901)])
mrgc = dn.rfs_image(mrgc, hard_def, "e7 10510", [(10510, 10585)])
mrgc = dn.rfs_image(mrgc, hard_def, "e7 32127", [(32127, 32150)])
mrgc = dn.rfs_image(mrgc, hard_def, "e7 34425", [(34425, 34493)])
mrgc = dn.rfs_image(mrgc, hard_def, "e7 31929", [(31929, 32024), (33834, 33917)])

hard_desc = dn.hard(epis, desc_h=desc_h, mthr=10)
mrgc = dn.rfs_image(mrgc, hard_desc, "e7 33273", [(33273, 33392)])
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
F7 = dn.filt(mrgc, sm_thr=34, db_thr=1, rt_sigma=0.6, db_grain=8, db_range=8)
F8 = dn.filt(mrgc, db_mode=1)
F9 = dn.filt(mrgc, db_mode=2)
F10 = dn.filt(mrgc, db_saveblack=0)

F1 = dn.rfs(F1, F2, [(ED, EDend - 1 - 24)])
F1 = dn.rfs(F1, F3, [(OP + 33, OP + 95)])
F1 = dn.rfs(F1, F4, [(OP + 96, OP + 157)])
F1 = dn.rfs(
    F1,
    F5,
    [
        (12555, 12593),
        (15040, 15075),
        (23563, 23637),
        (23668, 23685),
        (23746, 23783),
        (18941, 19009),
    ],
)
F1 = dn.rfs(F1, F6, [(3069, 3158), (20968, 21047), (21282, 21304), (22037, 22126), (31263, 31358)])
F1 = dn.rfs(F1, F7, [(10686, 10709), (12002, 12054)])
F1 = dn.rfs(
    F1,
    F8,
    [(1614, 1658), (1725, 1757), (5923, 6033), (14989, 15006), (15409, 15489), (29835, 29888)],
)
F1 = dn.rfs(F1, F9, [(2241, 2291), (7724, 7780), (12382, 12403)])
F1 = dn.rfs(F1, F10, [(7856, 7906), (9273, 9290)])
# ------------ #

# ----out----- #
clip = dn.out(F1, epname)
clip.set_output()
# ------------ #

# ----save---- #
# dn.pw4(mrgc, 2, 1, epis, clip).set_output()
# epis.set_output()
# clip.std.Trim(30000, 32800).set_output()

# dn.rfs_resc(mrgc, epis, desc_h=desc_h, mthr=50, out_mask=True).set_output()
# ------------ #

# ----err----- #
dn.check_num_frames(epis, clip)
# ------------ #
