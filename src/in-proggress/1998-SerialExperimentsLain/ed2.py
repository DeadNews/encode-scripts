import dnfunc as dn
from vapoursynth import core

# ----in---- #
epname = dn.fname(__file__)
epis = dn.source(f"./in/{epname}.mp4")
# ------------ #


def _crop_rel(epis):
    return epis.std.CropRel(top=10, bottom=10, left=246, right=246)


# ------------ #
# epis_back = epis
epis_back = _crop_rel(epis)

mrgc = core.yadifmod.Yadifmod(epis, edeint=core.nnedi3.nnedi3(epis, 1), order=1, mode=0)
mrgc = _crop_rel(mrgc)
# ---------- #

# ----in---- #
"""
def filt_old(
    mrgc=mrgc,
    dn_thr=100,
    dn_pref=3,
    cs_mode=1,
    cs_val=0.07,
    db_thr=1.0,
    db_mode=3,
    db_det=64,
    db_grain=48,
    db_range=15,
    db_saveblack=2,
    db_cs=2,
    rt_sigma=1.0,
    ag=True,
    ag_str=0.30,
    ag_scaling=12,
    ag_saveblack=2,
    out_mode=0,
):
"""

F1 = dn.filt(mrgc)
# ---------- #

# ---out---- #
clip = dn.out(F1, epname)
clip.set_output()
# ---------- #

# ---save--- #
# dn.pw4(mrgc, 2, 1, epis_back, clip).set_output()
# epis.set_output()
# ------------ #

# ---err---- #
dn.check_num_frames(epis, clip)
# ---------- ## ------------ #
