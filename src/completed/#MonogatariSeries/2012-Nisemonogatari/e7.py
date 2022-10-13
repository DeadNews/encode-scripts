import dnfunc as dn

# -----in----- #
epname = dn.fname(__file__)
desc_h = 720

Next = 36924

epis = dn.source(f"./in/{epname}.mkv")
# ------------ #

# ----mrgc---- #
aaep = dn.aa(epis, desc_h=desc_h)

mrgc = dn.rfs(aaep, epis, [(36058, 36887)])
# ------------ #

# ----mask---- #
mrgc = dn.rfs_qtgmc(mrgc, aaep, maps=[(15701, 16513)])
mrgc = dn.rfs_hard(mrgc, mrgc, mthr=99, maps=[(15701, 16513)])
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
F2 = dn.filt(mrgc, db_mode=1)
F3 = dn.filt(mrgc, db_mode=2, db_range=20)
F4 = dn.filt(mrgc, db_mode=1, db_range=20)

F1 = dn.rfs(F1, F2, [(9604, 9675), (12853, 13170)])
F1 = dn.rfs(F1, F3, [(29219, 29242), (29285, 29335), (30080, 30205)])
F1 = dn.rfs(F1, F4, [(28865, 29047)])
# ------------ #

# ----out----- #
clip = dn.out(F1, epname)
clip.set_output()
# ------------ #

# ----save---- #
# dn.pw4(mrgc, 2, 1, epis, clip).set_output()
# epis.set_output()
# clip.std.Trim(15701, 16513).set_output()

# dn.rfs_resc(mrgc, epis, desc_h=desc_h, mthr=50, out_mask=True).set_output()
# ------------ #

# ----err----- #
dn.check_num_frames(epis, clip)
# ------------ #
