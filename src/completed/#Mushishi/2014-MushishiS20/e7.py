import dnfunc as dn

# -----in----- #
epname = dn.fname(__file__)
str, kernel, desc_h = 0.5, "bilinear", 720

OP = dn.chapt(epname, "OP")
OPend = dn.chapt(epname, "OPend")
ED = dn.chapt(epname, "ED")
EDend = dn.chapt(epname, "Next")

epis = dn.source(f"./in/{epname}.mp4")
# ------------ #

# ----mrgc---- #
aaep = dn.aa(epis, str=str, kernel=kernel, desc_h=desc_h)
mrgc = aaep
# ------------ #

# ----mask---- #
mrgc = dn.rfs(mrgc, epis, [(OP, OPend - 1)])  # op
mrgc = dn.rfs(mrgc, epis, [(ED, EDend - 1)])  # ed
# ------------ #

# -----in----- #
"""
def filt_old(
    mrgc=mrgc,
    sm_thr=61,
    dn_pref=1,
    cs_mode=1,
    cs_val=0.4,
    db_thr=1.0,
    db_mode=3,
    db_det=64,
    db_grain=48,
    db_range=15,
    db_saveblack=0,
    db_cs=2,
    rt_sigma=0.9,
    ag=True,
    ag_str=0.131,
    ag_scaling=5,
    out_mode=0,
):
"""

F1 = dn.filt(mrgc)
F2 = dn.filt(mrgc, sm_thr=40, db_thr=1.9, cs_mode=0, ag_str=0)

F1 = dn.rfs(F1, F2, [(OP, OPend - 1), (ED, EDend - 1)])
# ------------ #

# ----out----- #
clip = dn.out(F1, epname)
clip.set_output()
# ------------ #

# ----save---- #
# dn.pw4(mrgc, 2, 1, epis, clip).set_output()
# epis.set_output()
# ------------ #

# ----err----- #
dn.check_num_frames(epis, clip)
# ------------ #
