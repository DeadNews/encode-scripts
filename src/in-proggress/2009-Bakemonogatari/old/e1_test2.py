import dnfunc as dn
from vapoursynth import core

# -----in----- #
epname = dn.fname(__file__)
desc_h = 720

OP = 3909
OPend = 6066
ED = 34405
EDend = 36562

epis = dn.source(f"./in/{epname}.mp4")
# ------------ #

# ----mrgc---- #
aaep = dn.aa(epis, desc_h=desc_h)
mrgc = aaep
# ------------ #

# ----mask---- #
fixed_black = mrgc.std.CropRel(top=142, bottom=144).std.AddBorders(top=142, bottom=144)
mrgc = dn.rfs(mrgc, fixed_black, [(0, 2205), (OP, OPend - 1)])

sw_mask = dn.gradfun_mask(aaep, thr_det=1, db_mode=3).fmtc.bitdepth(bits=8)
save_wite = core.std.MaskedMerge(mrgc, aaep, db_mode=sw_mask, planes=0)
mrgc = dn.rfs_image(mrgc, save_wite, "SWfilter", [(0, 591)])
# ------------ #

# ----filt---- #
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
    db_saveblack=0,
    rt_sigma=0.9,
    out_mode=0,
):
"""

F1 = dn.filt(mrgc)
# 54222
F2 = dn.filt(mrgc, db_saveblack=0, sm_thr=100, db_mode=1, rt_sigma=4)
# F2 = dn.filt(mrgc, db_saveblack=0, sm_thr=100, db_mode=1, rt_sigma=4, db_grain=58)
# F2 = dn.filt(mrgc, db_saveblack=0, sm_thr=100, db_thr=2.4, db_mode=3, rt_sigma=2, db_grain=28, db_range=10)
# F2 = dn.filt(mrgc, db_saveblack=0, sm_thr=100, db_thr=2.4, db_mode=3, rt_sigma=1, db_range=10)
# can make the mask weaker ..

filtered = dn.rfs_color(mrgc, F1, F2, tolerance=4)
# 4818 28322   38882 44162   49922 55486   106830 125542
# ------------ #

# ----out----- #
clip = dn.out(F1, epname)
clip.set_output()
# ------------ #

# ----save---- #
# dn.pw4(mrgc, 2, 1, epis, clip).set_output()
# epis.set_output()
# clip.std.Trim(13705, 14177).set_output()
# ------------ #

# ----err----- #
dn.check_num_frames(epis, clip)
# ------------ #
