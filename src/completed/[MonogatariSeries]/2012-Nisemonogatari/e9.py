import dnfunc as dn

# -----in----- #
epname = dn.fname(__file__)
desc_h = 720

OP = 1534
OPend = 3693
ED = 32609
EDend = 34766

epis = dn.source(f"./in/{epname}.mkv")
# ------------ #

# ----mrgc---- #
ed = dn.oped(epis, name="ed1", offset=12, start=ED, end=EDend, desc_h=desc_h)

aaep = dn.aa(epis, desc_h=desc_h)

mrgc = aaep.std.Trim(0, ED - 1) + ed + aaep.std.Trim(EDend, epis.num_frames - 1)
# ------------ #

# ----mask---- #
mrgc = dn.rfs_qtgmc(mrgc, aaep, k=0.77, maps="[410 516] [11291 11362]")
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
F3 = dn.filt(mrgc, sm_thr=40, db_saveblack=0, db_range=10)
F4 = dn.filt(mrgc, db_mode=2)
F5 = dn.filt(mrgc, sm_thr=35, db_thr=1, rt_sigma=0.7)

F1 = dn.rfs(F1, F2, f"[{OP} {OPend-1}]")
F1 = dn.rfs(F1, F3, "[11219 11251] [13130 13162] [25175 25205]")
F1 = dn.rfs(F1, F4, "[410 516]")
F1 = dn.rfs(F1, F5, "[8337 8378] [18610 18654]")
# ------------ #

# ----out----- #
clip = dn.out(F1, epname)
clip.set_output()
# ------------ #

# ----save---- #
# dn.pw4(mrgc, 2, 1, epis, clip).set_output()
# epis.set_output()
# clip.std.Trim(11219, 11251).set_output()
# clip.std.Trim(11219, 11229).set_output()

# dn.rfs_resc(mrgc, epis, desc_h=desc_h, mthr=50, out_mask=True).set_output()
# ------------ #

# ----err----- #
dn.check_num_frames(epis, clip)
# ------------ #
