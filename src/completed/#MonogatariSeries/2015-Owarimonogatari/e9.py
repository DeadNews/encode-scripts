import dnfunc as dn

# -----in----- #
epname = dn.fname(__file__)
desc_h = 720

OP = 2134
OPend = 3573
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
mrgc = dn.rfs_hard(mrgc, epis, desc_h=desc_h, mthr=10, maps="[31637 31678]")
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
F2 = dn.filt(mrgc, sm_thr=45, db_thr=1, rt_sigma=0.8, db_grain=46)
F3 = dn.filt(mrgc, rt_sigma=0.8, db_saveblack=0)
F4 = dn.filt(mrgc, sm_thr=44, db_thr=1, rt_sigma=0.7, db_grain=44)
F5 = dn.filt(mrgc, sm_thr=34, db_thr=1, rt_sigma=0.6, db_grain=36)

F1 = dn.rfs(F1, F2, f"[{OP} {OPend-1}] [13937 17596]")
F1 = dn.rfs(F1, F3, f"[{ED} {EDend-1-24}]")
F1 = dn.rfs(F1, F4, "[17597 24580]")
F1 = dn.rfs(F1, F5, "[7533 7622]")
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
