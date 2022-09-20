from pathlib import Path

import dnfunc as dn

# -----in----- #
epname = dn.fname(__file__)
desc_h = 720

epis = dn.source(f"./in/{epname}.mkv")

# -----aa----- #
if Path(f"./temp/{epname}_aa_lossless.mp4").is_file():
    aaep = dn.source(f"./temp/{epname}_aa_lossless.mp4")
else:
    aaep = dn.aa(epis, desc_h=desc_h)

mrgc = aaep
# ------------ #

# ----mask---- #
# ------------ #

# ----filt---- #
"""
def filt_old(
    mrgc=mrgc,
    sm_thr=80,
    tr=48,
    pref=1,
    cs_mode=99,
    cs_val=0.5,
    db_thr=2.1,
    db_mode=3,
    db_det=64,
    db_grain=48,
    db_range=15,
    db_saveblack=0,
    rt_sigma=1,
    out_mode=0,
):
"""

F1 = dn.filt(mrgc)
# ------------ #

# ----out----- #
clip = dn.out(F1, epname)
clip.set_output()
# ------------ #

# ----save---- #
# dn.pw4(mrgc, 2, 1, epis, clip).set_output()
# epis.set_output()
# clip.std.Trim(1341, 1476).set_output()

# dn.rfs_resc(mrgc, epis, desc_h=desc_h, mthr=50, out_mask=True).set_output()
# ------------ #

# ----err----- #
dn.check_num_frames(epis, clip)
# ------------ #
