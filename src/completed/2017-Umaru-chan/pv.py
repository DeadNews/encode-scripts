import dnfunc as dn
from vapoursynth import core

# -----in----- #
epname = dn.fname(__file__)
epis = dn.source(f"./in/{epname}.mp4")
# ------------ #

# -----aa----- #
mrgc = epis
# mrgc = core.yadifmod.Yadifmod(epis, edeint=core.nnedi3.nnedi3(epis, 2), order=1, mode=1)
mrgc = core.yadifmod.Yadifmod(epis, edeint=core.nnedi3.nnedi3(epis, 1), order=1, mode=0)
# ------------ #

# -----in----- #
"""
def filt_old(
    mrgc=mrgc,
    sm_thr=60,
    dn_pref=1,
    cs_mode=1,
    cs_val=0.5,
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

F1 = dn.filt(mrgc, sm_thr=70, db_thr=5.0, db_mode=1)
# ------------ #

# ----out----- #
clip = dn.out(F1, epname)
# clip = clip.std.AssumeFPS(fpsnum=30000, fpsden=1001)
clip.set_output()
# ------------ #

# ----save---- #
# dn.pw4(mrgc, 2, 1, epis, clip).set_output()
# epis.set_output()
# ------------ #

# ----err----- #
dn.check_num_frames(epis, clip)
# ------------ #
