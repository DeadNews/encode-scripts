import dnfunc as dn

# -----in----- #
epname = dn.fname(__file__)
desc_h = 720

Avant = 0
OP = 1726
OPend = 3885
Part_B = 15514
ED = 30960
# EDend = 33063
# Next = 33927
EDend = 32609
Next = 33063

epis = dn.source(f"./in/{epname}.mkv")
# ------------ #

# ----mrgc---- #
aaep = dn.aa(epis, desc_h=desc_h)
# mrgc =  aaep

op = dn.oped(epis, name="op2", offset=24, start=OP, end=OPend, desc_h=desc_h)
ed = epis.std.Trim(ED, EDend - 1)

mrgc = (
    aaep.std.Trim(0, OP - 1)
    + op
    + aaep.std.Trim(OPend, ED - 1)
    + ed
    + aaep.std.Trim(EDend, epis.num_frames - 1)
)
# ------------ #

# ----mask---- #
mrgc = dn.rfs_hard(mrgc, epis, desc_h=desc_h, mthr=50, yuv=True, maps="[19153 19320]")

hard = dn.hard(mrgc, mthr=2)
mrgc = dn.rfs_image(mrgc, hard, "e2 hard", "[31946 31999]")

mrgc = dn.rfs_resc(mrgc, epis, desc_h=desc_h, mthr=30, maps="[315 366]")
mrgc = dn.rfs_resc(mrgc, epis, desc_h=desc_h, mthr=99, maps="[31124 32608]")
mrgc = dn.rfs_image(mrgc, epis, "e2 01", "[367 469]")
mrgc = dn.rfs_image(mrgc, epis, "e2 02", "[30981 31066]")
mrgc = dn.rfs(mrgc, epis, "[33927 34046]")
# ------------ #

# ----filt---- #
"""
def filt_old(
    mrgc=mrgc,
    sm_thr=100,
    tr=48,
    pref=1,
    cs_mode=99,
    cs_val=0.5,
    db_thr=2.1,
    db_mode=2,
    db_det=64,
    db_grain=52,
    db_range=15,
    db_saveblack=0,
    rt_sigma=1,
    out_mode=0,
):
"""

F1 = dn.filt(mrgc)
F2 = dn.filt(mrgc, sm_thr=80, db_mode=3)
F3 = dn.filt(mrgc, db_thr=2.5)

F1 = dn.rfs(F1, F2, f"[{OP} {OPend-1}]")
F1 = dn.rfs(F1, F3, "[3885 7313]")
# ------------ #

# ----out----- #
clip = dn.out(F1, epname)
clip.set_output()
# ------------ #

# ----save---- #
# dn.pw4(mrgc, 2, 1, epis, clip).set_output()
# epis.set_output()
# clip.std.Trim(14918, 15266).set_output()

# dn.rfs_resc(mrgc, epis, desc_h=desc_h, mthr=50, out_mask=True).set_output()
# ------------ #

# ----err----- #
dn.check_num_frames(epis, clip)
# ------------ #
