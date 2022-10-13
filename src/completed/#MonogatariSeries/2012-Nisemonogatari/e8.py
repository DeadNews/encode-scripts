import dnfunc as dn

# -----in----- #
epname = dn.fname(__file__)
desc_h = 720

OP = 1344
OPend = 3501
ED = 32609
EDend = 34766

epis = dn.source(f"./in/{epname}.mkv")
# ------------ #

# ----mrgc---- #
ed = dn.oped(epis, name="ed3", offset=12, start=ED, end=EDend, desc_h=desc_h)

aaep = dn.aa(epis, desc_h=desc_h)

mrgc = aaep.std.Trim(0, ED - 1) + ed + aaep.std.Trim(EDend, epis.num_frames - 1)
# ------------ #

# ----mask---- #
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
F3 = dn.filt(mrgc, db_mode=1)
F4 = dn.filt(mrgc, db_thr=1, rt_sigma=0.8)
F5 = dn.filt(mrgc, sm_thr=40, db_thr=1, rt_sigma=0.7)
F6 = dn.filt(mrgc, sm_thr=35, db_thr=1, rt_sigma=0.7, db_grain=16)
F7 = dn.filt(mrgc, sm_thr=35)

F1 = dn.rfs(F1, F2, [(OP, OPend - 1)])
F1 = dn.rfs(F1, F3, [(7818, 7846), (30515, 30550), (31751, 31792), (7356, 7388)])
F1 = dn.rfs(F1, F4, [(22688, 22807), (22850, 22921), (23630, 23661), (24531, 24701)])
F1 = dn.rfs(F1, F5, [(16015, 16158), (22922, 23041)])
F1 = dn.rfs(F1, F6, [(7267, 7306), (7329, 7355), (7389, 7628)])
F1 = dn.rfs(F1, F7, [(16765, 16800)])
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
