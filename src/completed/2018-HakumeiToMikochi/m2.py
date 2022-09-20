import dnfunc as dn

# -----in----- #
epname = dn.fname(__file__)

epis = dn.source(f"./in/{epname}.mp4")
# ------------ #

# -----aa----- #
mrgc = epis
# ------------ #

# ----filt---- #
"""
def filt_old(
    mrgc=mrgc,
    sm_thr=50,
    dn_pref=1,
    cs_mode=1,
    cs_val=0.1,
    db_thr=2.4,
    db_mode=3,
    db_det=64,
    db_grain=48,
    db_range=15,
    db_saveblack=0,
    rt_sigma=1.1,
    ag_str=0,
    ag_scaling=12,
    out_mode=0,
):
"""

F1 = dn.filt(mrgc, sm_thr=70, db_thr=4, db_saveblack=2)
# ------------ #

# ----out----- #
clip = dn.out(F1, epname)
clip.set_output()
# ------------ #

# ----save---- #
# dn.pw4(mrgc, 2, 1, epis, clip).set_output()
# epis.set_output()
# clip.std.Trim(0, 436).set_output()
# ------------ #

# ----err----- #
dn.check_num_frames(epis, clip)
# ------------ #
