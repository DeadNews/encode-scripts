import dnfunc as dn

# -----in----- #
epname = dn.fname(__file__)

epis = dn.source(f"./in/{epname}.mp4")
epis, epis_back, edgefixer = dn.edgefix(epis)

# -----aa----- #
aaep = dn.aa(epis, epname)
mrgc = aaep
# ------------ #

# ----filt---- #
"""
def filt_old(
    mrgc=mrgc,
    sm_thr=40,
    dn_pref=1,
    cs_mode=1,
    cs_val=0.70,
    db_thr=2.1,
    db_mode=3,
    db_det=60,
    db_grain=48,
    db_range=15,
    db_saveblack=1,
    db_cs=2,
    rt_sigma=0.9,
    ag_str=0,
    ag_scaling=12,
    out_mode=0,
):
"""

F1 = dn.filt(mrgc, sm_thr=50, db_thr=2.1, cs_val=0.55, db_det=64)
# ------------ #

# ----out----- #
clip = dn.out(F1, epname)
clip.set_output()
# ------------ #

# ----save---- #
# dn.pw4(mrgc, 2, 1, epis_back, clip).set_output()
# epis.set_output()
# ------------ #

# ----err----- #
dn.check_num_frames(epis, clip)
# ------------ #
