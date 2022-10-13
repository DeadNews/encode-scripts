import dnfunc as dn

# -----in----- #
epname = dn.fname(__file__)
desc_h = 720

ED = 32608
EDend = 34765

epis = dn.source(f"./in/{epname}.mkv")
# ------------ #

# ----mrgc---- #
ed = dn.oped(epis, name="ed3", offset=0, start=ED, end=EDend, desc_h=desc_h)

aaep = dn.aa(epis, desc_h=desc_h)

mrgc = aaep.std.Trim(0, ED - 1) + ed + aaep.std.Trim(EDend, epis.num_frames - 1)
# ------------ #

# ----mask---- #
stabilize = dn.qtgmc(aaep)
mrgc = dn.rfs_image(mrgc, stabilize, "e8 21502", [(21502, 21650)])
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
F3 = dn.filt(mrgc, sm_thr=44, db_thr=1, rt_sigma=0.7, db_saveblack=0)
F4 = dn.filt(mrgc, db_thr=1, rt_sigma=0.8)
F5 = dn.filt(mrgc, db_thr=1, rt_sigma=0.8, db_saveblack=0)
F6 = dn.filt(mrgc, sm_thr=300, db_thr=6, db_mode=1, rt_sigma=4, db_det=128)
F7 = dn.filt(mrgc, db_mode=2)

F1 = dn.rfs(F1, F2, [(5405, 5428), (31375, 31419)])
F1 = dn.rfs(F1, F3, [(28199, 28270)])
F1 = dn.rfs(F1, F4, [(12866, 17135)])
F1 = dn.rfs(F1, F5, [(12878, 12894)])
F1 = dn.rfs(F1, F7, [(12364, 12387), (18965, 19054), (32508, 32519)])

F1 = dn.rfs_image(F1, F6, "e8 13386", [(13386, 13445), (14282, 14353)])
# ------------ #

# ----out----- #
clip = dn.out(F1, epname)
clip.set_output()
# ------------ #

# ----save---- #
# dn.pw4(mrgc, 2, 1, epis, clip).set_output()
# epis.set_output()
# clip.std.Trim(31463,32006).set_output()

# dn.rfs_resc(mrgc, epis, desc_h=desc_h, mthr=50, out_mask=True).set_output()
# ------------ #

# ----err----- #
dn.check_num_frames(epis, clip)
# ------------ #
