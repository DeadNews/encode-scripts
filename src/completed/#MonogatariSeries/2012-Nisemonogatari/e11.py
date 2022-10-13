import dnfunc as dn

# -----in----- #
epname = dn.fname(__file__)
desc_h = 720

OP = 3045
OPend = 5204
ED = 34777

epis = dn.source(f"./in/{epname}.mkv")
# ------------ #

# ----mrgc---- #
aaep = dn.aa(epis, desc_h=desc_h)

mrgc = dn.rfs(aaep, epis, [(ED, 36360)])
# ------------ #

# ----mask---- #
mrgc = dn.rfs_qtgmc(mrgc, aaep, maps=[(19357, 19540), (19580, 19806), (20059, 20089)])
mrgc = dn.rfs_hard(mrgc, mrgc, mthr=99, maps=[(19357, 19540), (20059, 20089)])

hard = dn.hard(mrgc, mthr=20)
mrgc = dn.rfs_image(mrgc, hard, "e11 34585", [(34585, 34680)])
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
F2 = dn.filt(mrgc, sm_thr=90)
F3 = dn.filt(mrgc, db_saveblack=0)
F4 = dn.filt(mrgc, db_mode=1)
F5 = dn.filt(mrgc, db_mode=2)
F6 = dn.filt(mrgc, rt_sigma=0.8)
F7 = dn.filt(mrgc, rt_sigma=0.6, db_thr=1)
F8 = dn.filt(mrgc, sm_thr=80)

F1 = dn.rfs(F1, F2, [(OP, OPend - 1)])
F1 = dn.rfs(F1, F3, [(16532, 16553), (19333, 19356), (21644, 21685), (22768, 22973)])
F1 = dn.rfs(F1, F4, [(9253, 9273), (9411, 9432), (10842, 10898)])
F1 = dn.rfs(F1, F5, [(9433, 9795), (9877, 9963), (10356, 10460)])
F1 = dn.rfs(F1, F6, [(16627, 16659)])
F1 = dn.rfs(F1, F7, [(22026, 22079)])
F1 = dn.rfs(F1, F8, [(22080, 22185)])
F1 = dn.rfs_image(F1, F4, "e11 21011", [(21011, 21461)])
# ------------ #

# ----out----- #
clip = dn.out(F1, epname)
clip.set_output()
# ------------ #

# ----save---- #
# dn.pw4(mrgc, 2, 1, epis, clip).set_output()
# epis.set_output()
# clip.std.Trim(19357, 19540).set_output()
# output = clip.std.Trim(19357, 19540) + clip.std.Trim(19580, 19806) + clip.std.Trim(20059, 20089); output.set_output()

# dn.rfs_resc(mrgc, epis, desc_h=desc_h, mthr=50, out_mask=True).set_output()
# ------------ #

# ----err----- #
dn.check_num_frames(epis, clip)
# ------------ #
