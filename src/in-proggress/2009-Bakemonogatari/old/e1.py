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
# fixed_black = mrgc.std.CropRel(top=142, bottom=144).std.AddBorders(top=142, bottom=144)
# mrgc         = dn.rfs(mrgc, fixed_black, f"[0 2205] [{OP} {OPend-1}]")
#
# sw_mask      = dn.gradfun_mask(aaep, thr_det=1, db_mode=3).fmtc.bitdepth(bits=8)
# save_wite = core.std.MaskedMerge(mrgc, aaep, db_mode=sw_mask, planes=0)
# mrgc      = dn.rfs_image(mrgc, save_wite, 'timer', "[0 591]")
# ------------ #


def filtr_func(mrgc, clip16, tolerance=2):
    black_clip = core.std.BlankClip(clip16)
    clip16_black = dn.rfs_color(mrgc, clip16, black_clip, tolerance=tolerance)
    val = 0.03
    #  val = 0.05

    return core.std.Expr([clip16_black, clip16], f"x {val} * y 1 {val} - * +")


def filtr_func4(mrgc, clip16, tolerance=4):
    return filtr_func(mrgc, clip16, tolerance=tolerance)


# -----in----- #
"""
def filt_old(
    mrgc=mrgc,
    sm_thr=70,
    tr=48,
    pref=1,
    cs_mode=99,
    cs_val=0.55,
    db_thr=3.0,
    db_mode=3,
    db_det=64,
    db_grain=48,
    db_range=15,
    db_saveblack=0,
    rt_sigma=0.9,
    out_mode=0,
    prefilt_function=None,
    db_yuv=True,
):
"""

F1 = dn.filt(mrgc)
F2 = dn.filt(mrgc, prefilt_func=filtr_func4)
F3 = dn.filt(
    mrgc,
    prefilt_func=filtr_func,
    db_saveblack=0,
    cs_mode=0,
    sm_thr=3000,
    db_mode=1,
    rt_sigma=4,
    db_grain=32,
)

F1 = dn.rfs(F1, F2, "[26665 26820]")
F1 = dn.rfs_color(mrgc, F1, F3, tolerance=4)
# 54222 38882 63842
# 4818 28322   38882 44162   49922 55486   106830 125542   57122

# F1 = dn.adaptive_grain(F1, strength=0.25, static=True, luma_ag_scaling=12, show_db_mode=False)
# ------------ #

# ----mask---- #
fix_black = F1.std.CropRel(top=142, bottom=144).std.AddBorders(top=142, bottom=144)
F1 = dn.rfs(F1, fix_black, f"[0 2205] [{OP} {OPend-1}]")

w_mask = dn.gradfun_mask(aaep, thr_det=1, db_mode=3)
save_wite = core.std.MaskedMerge(F1, aaep.fmtc.bitdepth(bits=16), db_mode=w_mask, planes=0)
F1 = dn.rfs_image(F1, save_wite, "timer", "[0 591]")

# halos = core.std.Expr([mask_outer, mask_inner], 'x y -')
# ------------ #

# ----out----- #
clip = dn.out(F1, epname)
clip.set_output()
# ------------ #

# ----save---- #
# dn.pw4(mrgc, 2, 1, epis, clip).set_output()
# epis.set_output()
# clip.std.Trim(13705, 14177).set_output()
# clip.std.Trim(26665, 26820).set_output()
# clip.std.Trim(31294, 31494).set_output()
# ------------ #

# ----err----- #
dn.check_num_frames(epis, clip)
# ------------ #
