import dnfunc as dn
from vapoursynth import GRAY, YUV, core

# -----in----- #
epname = dn.fname(__file__)

OP = 0
OPend = 3174
ED = 133499

epis = dn.source(f"./in/{epname}.mkv")
epis = epis.std.CropRel(top=20, bottom=22)

# -----ef----- #
epis_py = (
    core.std.ShufflePlanes(epis, 0, GRAY)
    .std.Crop(top=1)
    .edgefixer.Continuity(top=1, bottom=1)
    .std.AddBorders(top=1)
)
epis_p1 = core.std.ShufflePlanes(epis, 1, GRAY).edgefixer.Continuity(top=2, bottom=1)
epis_p2 = core.std.ShufflePlanes(epis, 2, GRAY).edgefixer.Continuity(top=2, bottom=1)
epis_ef = core.std.ShufflePlanes([epis_py, epis_p1, epis_p2], [0, 0, 0], YUV)

mrgc = epis_ef
# ------------ #

# ----mask---- #
# mrgc = dn.rfs_hard(mrgc, epis, mthr=99, maps=[(26123, 26181)])
# ------------ #

# -----in----- #
"""
def filt_old(
    mrgc=mrgc,
    sm_thr=100,
    tr=48,
    pref=1,
    cs_mode=2,
    cs_val=0.50,
    db_det=60,
    db_grain=48,
    db_thr=2.6,
    db_mode=1,
    db_range=15,
    rt_sigma=1,
    out_mode=0,
):
"""

F0 = dn.filt(epis, sm_thr=70, tr=5, db_thr=0, rt_sigma=1)  # epis_ef

F1 = dn.filt(mrgc)
F2 = dn.filt(mrgc, cs_val=0.75, sm_thr=70)
F3 = dn.filt(mrgc, cs_val=0.75, db_thr=2.7, db_mode=2)
F4 = dn.filt(mrgc, cs_val=0.55, db_thr=2.4, db_mode=2, sm_thr=70)
F5 = dn.filt(mrgc, cs_val=0.75, db_thr=1.6, db_mode=2, sm_thr=90, rt_sigma=0.9)

F1 = dn.rfs(F1, F0, [(0, OPend - 1), (75561, 75633), (ED, epis.num_frames - 1)])
F1 = dn.rfs(F1, F2, [(74446, 75562)])
F1 = dn.rfs(F1, F3, [(84372, 86005), (87558, 87607), (87960, 88087)])
F1 = dn.rfs(F1, F4, [(107945, 113687)])
F1 = dn.rfs(F1, F5, [(113688, 119373)])
# ------------ #

# ----out----- #
clip = dn.out(F1, epname)
clip.set_output()
# ------------ #

# ----save---- #
# dn.pw4(mrgc, 2, 1, epis, clip).set_output()
# epis.set_output()
# clip.std.Trim(33922, 36922).set_output()
# clip.std.Trim(113877, 116877).set_output()
# clip.std.Trim(108877, 111877).set_output()
# ------------ #

# ----err----- #
dn.check_num_frames(epis, clip)
# ------------ #
