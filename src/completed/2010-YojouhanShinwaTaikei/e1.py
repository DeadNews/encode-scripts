import dnfunc as dn

# -----in----- #
epname = dn.fname(__file__)
kernel, desc_h = "bilinear", 720

OP = dn.chapt(epname, "OP")
OPend = dn.chapt(epname, "OPend")
ED = dn.chapt(epname, "ED")

epis = dn.source(f"./in/{epname}.mp4")
EDend = epis.num_frames - 1
# ------------ #

# ----mrgc---- #
aaep = dn.aa(epis, desc_h=desc_h, kernel=kernel)
mrgc = aaep
# ------------ #

# ----mask---- #
mrgc = dn.rfs(mrgc, epis, [(ED, EDend)])

hard = dn.hard(mrgc, mthr=50)
mrgc = dn.rfs_image(mrgc, hard, "ed1", [(ED + 1656, ED + 1725)])
# ------------ #

# ----filt---- #
# Removed `db_cs=True`, increase `cs_va` to 0.7 instead
"""
def filt_old(
    mrgc=mrgc,
    sm_thr=100,
    dn_pref=3,
    cs_mode=1,
    cs_val=0.6,
    db_thr=2.3,
    db_mode=3,
    db_det=64,
    db_grain=58,
    db_range=15,
    db_saveblack=0,
    db_cs=True,
    rt_sigma=0.9,
    ag=True,
    ag_str=0.33,
    ag_scaling=12,
    out_mode=0,
):
"""

F1 = dn.filt(mrgc)
F2 = dn.filt(mrgc, sm_thr=150, db_thr=3, ag_str=0.50, cs_val=0.4)
F3 = dn.filt(mrgc, sm_thr=150, db_thr=4, ag_str=0.40)
F4 = dn.filt(
    mrgc,
    sm_thr=300,
    db_thr=5,
    rt_sigma=1,
    ag_str=2.00,
    ag_scaling=0,
    cs_val=0.4,
)
F5 = dn.filt(mrgc, sm_thr=30, db_thr=1.5, rt_sigma=0.7, ag_str=0.05)
F6 = dn.filt(mrgc, sm_thr=200, db_thr=2.6)
F7 = dn.filt(mrgc, db_thr=2.6)

F1 = dn.rfs(F1, F2, [(OP, OPend - 744)])
F1 = dn.rfs(F1, F3, [(OPend - 743, OPend - 1)])
F1 = dn.rfs(F1, F4, [(ED, EDend)])
F1 = dn.rfs(F1, F5, [(ED + 1353, ED + 1451), (ED + 1761, ED + 1864), (30630, 30680)])
F1 = dn.rfs(F1, F6, [(OPend, 10861), (12110, 13111)])
F1 = dn.rfs(F1, F7, [(0, 359), (455, OP - 1)])
# ------------ #

# ----out----- #
clip = dn.out(F1, epname)
clip.set_output()
# ------------ #

# ----save---- #
# dn.pw4(mrgc, 2, 1, epis, clip).set_output()
# 107186 111986 54770 137706 122546
# dn.pw(dn.filt(mrgc, out_mode=6), filt(mrgc, out_mode=1), epis, clip).set_output()
# epis.set_output()
# clip.std.Trim(OPend, ED-1).set_output()
# clip.std.Trim(0, OP-1).set_output()
# clip.std.Trim(8319, 10861).set_output()
# ------------ #

# ----err----- #
dn.check_num_frames(epis, clip)
# ------------ #
