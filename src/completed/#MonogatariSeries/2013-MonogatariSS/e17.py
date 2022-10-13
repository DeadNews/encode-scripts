import dnfunc as dn

# -----in----- #
epname = dn.fname(__file__)
desc_h = 720

ED = 32347 + 153
EDend = 34504

epis = dn.source(f"./in/{epname}.mkv")
# ------------ #

# ----mrgc---- #
ed = dn.oped(epis, name="ed5", offset=165, start=ED, end=EDend, desc_h=desc_h)

aaep = dn.aa(epis, desc_h=desc_h)

mrgc = aaep.std.Trim(0, ED - 1) + ed + aaep.std.Trim(EDend, epis.num_frames - 1)
# ------------ #

# ----mask---- #
hard = dn.hard(epis, desc_h=desc_h, mthr=2)

mrgc = dn.rfs_image(
    mrgc,
    hard,
    "e17 7702",
    [
        (7702, 8040),
        (8501, 8681),
        (9942, 10079),
        (10623, 10790),
        (12420, 12569),
        (12777, 12831),
        (18217, 18315),
        (19023, 19168),
        (20821, 21019),
        (22191, 22334),
    ],
)
mrgc = dn.rfs_image(mrgc, hard, "e17 1864", [(1864, 1983)])
mrgc = dn.rfs_image(mrgc, hard, "e17 11471", [(11471, 11524)])
mrgc = dn.rfs_image(mrgc, hard, "e17 12604", [(12604, 12703)])
mrgc = dn.rfs_image(
    mrgc, hard, "e17 15599", [(15599, 15727), (15986, 16006), (16257, 16397), (21358, 21474)]
)
mrgc = dn.rfs_image(mrgc, hard, "e17 16027", [(16027, 16071)])
mrgc = dn.rfs_image(mrgc, hard, "e17 16084", [(16084, 16256)])
mrgc = dn.rfs_image(mrgc, hard, "e17 16572", [(16572, 16688)])
mrgc = dn.rfs_image(mrgc, hard, "e17 17202", [(17202, 17414)])
mrgc = dn.rfs_image(mrgc, hard, "e17 21927", [(21927, 22028)])
mrgc = dn.rfs_image(mrgc, hard, "e17 22119", [(22119, 22143)])
mrgc = dn.rfs_image(mrgc, hard, "e17 22533", [(22533, 22877)])
mrgc = dn.rfs_image(mrgc, hard, "e17 27427", [(27427, 27645)])
mrgc = dn.rfs_image(mrgc, hard, "e17 27959", [(27959, 28149), (26772, 26900)])
mrgc = dn.rfs_image(mrgc, hard, "e17 5007", [(5007, 5036)])
mrgc = dn.rfs_image(mrgc, hard, "e17 4698", [(4698, 4729)])
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
F2 = dn.filt(mrgc, sm_thr=45, db_thr=1, rt_sigma=0.8)
F3 = dn.filt(mrgc, sm_thr=44, db_thr=1, rt_sigma=0.7)
F4 = dn.filt(mrgc, sm_thr=38, db_thr=1, rt_sigma=0.6, db_grain=40)
F5 = dn.filt(mrgc, sm_thr=34, db_thr=1, rt_sigma=0.6, db_grain=36)
F6 = dn.filt(mrgc, sm_thr=300, db_thr=6, db_mode=1, rt_sigma=4, db_det=128)
F7 = dn.filt(mrgc, sm_thr=60, db_thr=4, db_mode=1)

F1 = dn.rfs(F1, F2, [(7297, 7477), (20562, 20721), (27902, 27958), (30810, 30935), (37038, 37121)])
F1 = dn.rfs(
    F1,
    F3,
    [
        (1840, 1858),
        (4987, 5006),
        (11369, 11470),
        (11950, 12022),
        (22469, 22532),
        (31718, 31731),
        (35888, 35950),
        (38328, 38357),
        (34779, 34826),
        (30780, 30809),
        (31036, 31059),
    ],
)
F1 = dn.rfs(F1, F4, [(23069, 23134), (31432, 31461), (31767, 31846), (38823, 38852)])
F1 = dn.rfs(F1, F5, [(5876, 5896), (30480, 30557), (38823, 38852), (36026, 36067)])

F1 = dn.rfs_image(F1, F6, "e17 34598", [(34598, 34625)])
F1 = dn.rfs_image(F1, F7, "e17 36026", [(36026, 36067)])
# ------------ #

# ----out----- #
clip = dn.out(F1, epname)
clip.set_output()
# ------------ #

# ----save---- #
# dn.pw4(mrgc, 2, 1, epis, clip).set_output()
# epis.set_output()
# clip.std.Trim(0, 3000).set_output()

# dn.rfs_resc(mrgc, epis, desc_h=desc_h, mthr=50, out_mask=True).set_output()
# ------------ #

# ----err----- #
dn.check_num_frames(epis, clip)
# ------------ #
