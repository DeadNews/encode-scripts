from pathlib import Path

import dnfunc as dn

# -----in----- #
epname = dn.fname(__file__)
desc_h = 720

epis = dn.source(f"./in/{epname}.mp4")
# ------------ #

# -----aa----- #
aaep = (
    dn.source(f"./temp/{epname}_aa_lossless.mp4")
    if Path(f"./temp/{epname}_aa_lossless.mp4").is_file()
    else dn.aa(epis, desc_h=desc_h)
)

mrgc = aaep
# ------------ #

# ----mask---- #
if Path(f"./temp/{epname}_filt_lossless.mp4").is_file():
    mrgc = dn.source(f"./temp/{epname}_filt_lossless.mp4")
else:
    mrgc = dn.rfs_qtgmc(
        mrgc, aaep, k=0.77, maps=[(12, 233), (1179, 1420), (1742, 1772), (1795, 1913)]
    )
# ------------ #

# -----in----- #
"""
def filt_old(
    mrgc=mrgc,
    sm_thr=50,
    tr=48,
    pref=1,
    cs_mode=99,
    cs_val=0.55,
    db_thr=1.1,
    db_mode=3,
    db_det=64,
    db_grain=48,
    db_range=15,
    db_saveblack=2,
    rt_sigma=0.9,
    out_mode=0,
):
"""

F1 = dn.filt(mrgc, db_thr=1)
# ------------ #

# ----out----- #
clip = dn.out(F1, epname, fpsnum=24000, fpsden=1001)
clip.set_output()
# ------------ #

# ----save---- #
# dn.pw4(mrgc, 2, 1, epis, clip).set_output()
# epis.set_output()
# clip.std.Trim(0, 3000).set_output()
# ------------ #

# ----err----- #
dn.check_num_frames(epis, clip)
# ------------ #
