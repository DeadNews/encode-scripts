from pathlib import Path

import dnfunc as dn

# -----in----- #
epname = dn.fname(__file__)
str, kernel, desc_h = 0.58, "bicubic", 720

epis = dn.source(f"./in/{epname}.mp4")
epis = epis.edgefixer.Continuity(2, 2, 2, 2)

# -----aa----- #
if Path(f"./temp/{epname}_aa_lossless.mp4").is_file():
    aaep = dn.source(f"./temp/{epname}_aa_lossless.mp4")
else:
    aaep = dn.aa(epis, str=str, kernel=kernel, desc_h=desc_h, yuv=True)

mrgc = aaep
# ------------ #

# ----mask---- #
mrgc = dn.rfs_resc(
    mrgc, epis, desc_h=desc_h, planes=[0, 1, 2], mthr=50, maps=f"[0 {epis.num_frames-1}]"
)
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
# dn.rfs_resc(mrgc, epis, desc_h=desc_h, mthr=50, out_mask=True).set_output()
# ------------ #

# ----err----- #
dn.check_num_frames(epis, clip)
# ------------ #
