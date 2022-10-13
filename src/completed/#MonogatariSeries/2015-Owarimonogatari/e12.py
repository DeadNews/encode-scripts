import dnfunc as dn

# -----in----- #
epname = dn.fname(__file__)
desc_h = 720

OP = 1702
OPend = 3141
ED = 32609

epis = dn.source(f"./in/{epname}.mkv")
EDend = epis.num_frames - 36
# ------------ #

# ----mrgc---- #
ed = dn.oped(epis, name="ed2", offset=12, start=ED, end=EDend, desc_h=desc_h)

aaep = dn.aa(epis, desc_h=desc_h)

mrgc = aaep.std.Trim(0, ED - 1) + ed + aaep.std.Trim(EDend, epis.num_frames - 1)
# ------------ #

# ----mask---- #
hard = dn.hard(mrgc, mthr=20)
mrgc = dn.rfs_image(mrgc, hard, "e12 29047", [(29047, 29262), (29374, 29550)])
mrgc = dn.rfs_image(mrgc, hard, "e12 29323", [(29323, 29373)])

mrgc = dn.rfs_hard(mrgc, mrgc, mthr=99, maps=[(6825, 6849)])
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
F3 = dn.filt(mrgc, rt_sigma=0.8, db_saveblack=0)
F4 = dn.filt(mrgc, sm_thr=44, db_thr=1, rt_sigma=0.7)
F5 = dn.filt(mrgc, sm_thr=38, db_thr=1, rt_sigma=0.6, db_grain=40)
F6 = dn.filt(mrgc, sm_thr=300, db_thr=6, db_mode=1, rt_sigma=4, db_det=128)
F7 = dn.filt(mrgc, db_mode=1)

F1 = dn.rfs(F1, F2, [(OP, OPend - 1), (13811, 28209)])
F1 = dn.rfs(F1, F3, [(ED, EDend - 1 - 24), (5184, 5243)])
F1 = dn.rfs(F1, F4, [(877, 906), (22272, 22303), (23752, 23847), (26326, 26367)])
F1 = dn.rfs(F1, F5, [(13847, 13896), (25434, 25467)])
F1 = dn.rfs(F1, F7, [(5244, 5426), (5475, 5558)])

F1 = dn.rfs_image(
    F1, F6, "e12 10977", [(10977, 11264), (11783, 11913), (12047, 12274), (12490, 12837)]
)
# ------------ #

# ----out----- #
clip = dn.out(F1, epname)
clip.set_output()
# ------------ #

# ----save---- #
# dn.pw4(mrgc, 2, 1, epis, clip).set_output()
# epis.set_output()
# clip.std.Trim(30000, 32800).set_output()
# ------------ #

# ----err----- #
dn.check_num_frames(epis, clip)
# ------------ #
