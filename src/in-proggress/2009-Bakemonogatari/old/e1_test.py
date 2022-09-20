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
mrgc = dn.rfs(mrgc, fixed_black, f"[0 2205] [{OP} {OPend-1}]")

sw_mask = dn.gradfun_mask(aaep, thr_det=1, db_mode=3).fmtc.bitdepth(bits=8)
save_wite = core.std.MaskedMerge(mrgc, aaep, db_mode=sw_mask, planes=0)
mrgc = dn.rfs_image(mrgc, save_wite, "SWfilter", "[0 591]")
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

F1 = dn.filt(mrgc)

# black_clip = core.std.BlankClip(filtered)
# F1 = rfs_sb_mask(F1, black_clip, mask_src=mrgc, maps=f"[0 {EDend}]")
# F1 = rfs_sb_mask(F1, black_clip, mask_src=mrgc, maps="[13805 14023] [14055 14077]")
# 4818 28322   38882 44162   49922 55486   106830 125542
# tolerance=4 — для усиления
# tolerance=2 — для замены на черное
# хотя в некоторых сценах можно и 4 поставить для замены
# разность можно между ними посмотреть и вернуть по этой маске дебанд с 4

# sb_mask = core.tcm.TColorMask(mrgc, '$000000', tolerance=2)
# from vapoursynth import GRAY16
# sb_mask = core.resize.Point(sb_mask, format=GRAY16)
# sb_mask.set_output()

# AD = dn.adaptive_grain(filtered, strength=0.25, static=True, luma_ag_scaling=12, show_db_mode=True)
# AD.set_output()

F1 = dn.filt(mrgc)
F2 = dn.filt(mrgc, db_saveblack=0, sm_thr=100, db_mode=1, rt_sigma=4, db_grain=58)
# F2 = dn.filt(mrgc, db_saveblack=0, sm_thr=100, db_thr=2.5, db_mode=3, rt_sigma=3, db_grain=28, db_range=10)


def filtr_func(src):
    return dn.filt(mrgc, mrgc=src, db_saveblack=0, sm_thr=100, db_mode=1, rt_sigma=4, db_grain=58)
    #  return dn.filt(mrgc, mrgc=src, db_saveblack=0, sm_thr=100, db_thr=2.5, db_mode=3, rt_sigma=3, db_grain=16, db_range=10)


test = dn.sb_test(F1, F2, mask_src=mrgc, filtr=filtr_func)
# test.set_output(
filtered = test
# ------------ #

# ----out----- #
clip = dn.out(F1, epname)
clip.set_output()
# ------------ #

# ----save---- #
# dn.pw(dn.filt(mrgc, out_mode=2), filt(mrgc, out_mode=1), epis, clip).set_output()
# epis.set_output()
# clip.std.Trim(13705, 14177).set_output()
# ------------ #

# ----err----- #
dn.check_num_frames(epis, clip)
# ------------ #
