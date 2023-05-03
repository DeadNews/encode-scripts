from pathlib import Path

import dnfunc as dn

# -----in----- #
epname = dn.fname(__file__)
aa_str, kernel, desc_h = 0.5, "bicubic", 720

epis = dn.source(f"./in/{epname}.mp4")
# ------------ #

# -----aa----- #
if Path(f"./temp/{epname}_aa_lossless.mp4").is_file():
    aaep = dn.source(f"./temp/{epname}_aa_lossless.mp4")
else:
    aaep = dn.aa(epis, str=aa_str, kernel=kernel, desc_h=desc_h)

mrgc = aaep
# ------------ #

# ----filt---- #
"""
def filt_old(
    mrgc=mrgc,
    sm_thr=91,
    dn_pref=1,
    cs_mode=1,
    cs_val=0.44,
    db_thr=2.0,
    db_mode=3,
    db_det=64,
    db_grain=48,
    db_range=15,
    db_saveblack=0,
    rt_sigma=0.91,
    ag_str=0,
    ag_scaling=12,
    out_mode=0,
):
"""

F1 = dn.filt(mrgc, sm_thr=100, rt_sigma=0.95, cs_val=0.32)
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
