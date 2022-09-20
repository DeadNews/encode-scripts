from pathlib import Path

import dnfunc as dn

# -----in----- #
epname = dn.fname(__file__)

epis = dn.source(f"./in/{epname}.mp4")
# ------------ #

# -----aa----- #
if Path(f"./temp/{epname}_aa_lossless.mp4").is_file():
    aaep = dn.source(f"./temp/{epname}_aa_lossless.mp4")
else:
    aaep = dn.aa(epis)

mrgc = dn.rfs_dehalo(aaep, epis, mode="kirsch", max_c=4, min_c=1)
mrgc = dn.rfs_resc(mrgc, epis, desc_h=938, mthr=17)
# ------------ #

# ----filt---- #
"""
def filt_old(
    mrgc=mrgc,
    sm_thr=50,
    dn_pref=1,
    cs_mode=1,
    cs_val=0.20,
    db_thr=2.3,
    db_mode=3,
    db_det=64,
    db_grain=48,
    db_range=15,
    db_saveblack=2,
    db_cs=2,
    rt_sigma=1.0,
    ag_str=0,
    ag_scaling=12,
    out_mode=0,
):
"""

F1 = dn.filt(mrgc, db_saveblack=2)
# ------------ #

# ----out----- #
clip = dn.out(F1, epname, fpsnum=24000, fpsden=1001)
clip.set_output()
# ------------ #

# ----save---- #
# dn.pw4(mrgc, 2, 1, epis, clip).set_output()
# epis.set_output()
# ------------ #

# ----err----- #
dn.check_num_frames(epis, clip)
# ------------ #
