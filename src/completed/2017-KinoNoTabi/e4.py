import dnfunc as dn
from vapoursynth import core

# -----in----- #
epname = dn.fname(__file__)
desc_h = 720

Avant = 0
OP = 792
# OP = 768 (-24)
OPend = 2949
Part_B = 13452
ED = 30211
EDend = 32369
Next = 33927

epis = dn.source(f"./in/{epname}.mkv")
epis = core.std.DuplicateFrames(epis.std.Trim(0, 23), list(range(24))) + epis.std.Trim(
    24, epis.num_frames - 1
)
# make from the first 24 frames 48
# ------------ #

# ----mrgc---- #
aaep = dn.aa(epis, desc_h=desc_h)
# mrgc =  aaep

op = dn.oped(epis, name="op2", offset=24, start=OP, end=OPend, desc_h=desc_h)
ed = epis.std.Trim(ED, EDend - 1)

mrgc = (
    aaep.std.Trim(0, OP - 1)
    + op
    + aaep.std.Trim(OPend, ED - 1)
    + ed
    + aaep.std.Trim(EDend, epis.num_frames - 1)
)
# ------------ #

# ----mask---- #
hard = dn.hard(epis, desc_h=desc_h, mthr=2)
mrgc = dn.rfs_image(mrgc, hard, "e4 03", "[20973 21158]")

mrgc = dn.rfs_image(mrgc, epis, "e4 01", "[146 235]")
mrgc = dn.rfs_image(mrgc, epis, "e4 02", "[32383 32438]")
# ------------ #

# ----filt---- #
"""
def filt_old(
    mrgc=mrgc,
    sm_thr=100,
    tr=48,
    pref=1,
    cs_mode=99,
    cs_val=0.5,
    db_thr=2.1,
    db_mode=2,
    db_det=64,
    db_grain=52,
    db_range=15,
    db_saveblack=0,
    rt_sigma=1,
    out_mode=0,
):
"""

F1 = dn.filt(mrgc)
F2 = dn.filt(mrgc, sm_thr=80, db_mode=3)

F1 = dn.rfs(F1, F2, f"[{OP} {OPend-1}]")
# ------------ #

# ----out----- #
clip = dn.out(F1, epname)
clip.set_output()
# ------------ #

# ----save---- #
# dn.pw4(mrgc, 2, 1, epis, clip).set_output()
# epis.set_output()
# fix.set_output()
# clip.std.Trim(0, 400).set_output()

# dn.rfs_resc(mrgc, epis, desc_h=desc_h, mthr=50, out_mask=True).set_output()
# ------------ #

# ----err----- #
# dn.check_num_frames(epis, clip)
# ------------ #
