from pathlib import Path

import dnfunc as dn

# -----in----- #
epname = dn.fname(__file__)
kernel, desc_h = "bilinear", 720

epis = dn.source(f"./in/{epname}.mp4")
# ------------ #

# -----aa----- #
aaep = (
    dn.source(f"./temp/{epname}_aa_lossless.mp4")
    if Path(f"./temp/{epname}_aa_lossless.mp4").is_file()
    else dn.aa(epis, desc_h=desc_h, kernel=kernel)
)

mrgc = aaep
# ------------ #

# ----filt---- #
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

F1 = dn.filt(mrgc, sm_thr=150, db_thr=4, ag_str=0.40)
F2 = dn.filt(mrgc, sm_thr=150, db_thr=3, ag_str=0.50, cs_val=0.4)

F1 = dn.rfs(F1, F2, (0, 1437))
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
