from pathlib import Path

import dnfunc as dn

# -----in----- #
epname = dn.fname(__file__)
kernel, desc_h = "bilinear", 720

epis = dn.source(f"./in/{epname}.mp4")
# ------------ #

# -----aa----- #
if Path(f"./temp/{epname}_aa_lossless.mp4").is_file():
    aaep = dn.source(f"./temp/{epname}_aa_lossless.mp4")
else:
    aaep = dn.aa(epis, desc_h=desc_h, kernel=kernel)

mrgc = aaep
# ------------ #

# ----mask---- #
OP = 24
mrgc = dn.rfs_resc(mrgc, epis, desc_h=desc_h, mthr=30, maps=[(OP + 82, OP + 197)])  # op2
# ------------ #

# ----filt---- #
"""
def filt_old(
    mrgc=mrgc,
    sm_thr=50,
    dn_pref=1,
    cs_mode=1,
    cs_val=0.5,
    db_thr=2.3,
    db_mode=3,
    db_det=64,
    db_grain=48,
    db_range=10,
    db_saveblack=2,
    db_cs=False,
    rt_sigma=0.85,
    ag_str=0,
    ag_scaling=12,
    out_mode=0,
):
"""

F1 = dn.filt(mrgc, db_thr=2.3)
# ------------ #

# ----out----- #
clip = dn.out(F1, epname)
clip.set_output()
# ------------ #

# ----save---- #
# dn.pw4(mrgc, 2, 1, epis, clip).set_output()
# epis.set_output()

# dn.rfs_resc(mrgc, epis, desc_h=desc_h, mthr=30, out_mask=True).set_output()
# ------------ #

# ----err----- #
dn.check_num_frames(epis, clip)
# ------------ #
