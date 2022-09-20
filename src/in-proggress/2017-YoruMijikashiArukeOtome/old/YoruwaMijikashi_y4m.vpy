import fvsfunc as fvf
import gradfun_amod as gfa
import kagefunc
import vapoursynth as vs
from vapoursynth import core

core.set_max_cache_size(10000)
core.avs.LoadPlugin(r"c:/#prog/CLI/dgdecnv/x64 Binaries/DGDecodeNV.dll")

y4m = core.raws.Source(r"y:\Yoru wa Mijikashi_y4m.y4m")
epis = core.avs.DGSource(r"..\dgi\Yoru wa Mijikashi.dgi")

# ---f1_main--- #
clip16 = core.fmtc.bitdepth(epis, bits=16)
denoised = core.knlm.KNLMeansCL(
    clip16,
    h=0.15,
    d=2,
    a=3,
    wmode=0,
    wref=1,
    s=1,
    channels="Y",
    device_type="GPU",
    device_id=1,
)
denoised = core.knlm.KNLMeansCL(
    denoised,
    h=0.25,
    d=2,
    a=3,
    wmode=0,
    wref=1,
    s=1,
    channels="UV",
    device_type="GPU",
    device_id=1,
)
debanded = gfa.GradFun3(denoised, smode=6, thr_det=4, db_grain=14, grainc=14, db_mode=0)

ret_mask = kagefunc.retinex_edgemask(clip16, rt_sigma=0.2)
ret_mask = core.resize.Point(ret_mask, format=vs.YUV420P16, matrix_s="709")
filtered = core.std.MaskedMerge(debanded, clip16, ret_mask)
# ------- #

# ---f2_denois(low)_thr_det=1--- #
denoised_2 = core.knlm.KNLMeansCL(
    clip16,
    h=0.1,
    d=2,
    a=3,
    wmode=0,
    wref=1,
    s=1,
    channels="Y",
    device_type="GPU",
    device_id=1,
)
denoised_2 = core.knlm.KNLMeansCL(
    denoised_2,
    h=0.20,
    d=2,
    a=3,
    wmode=0,
    wref=1,
    s=1,
    channels="UV",
    device_type="GPU",
    device_id=1,
)
debanded_2 = gfa.GradFun3(denoised_2, smode=6, thr_det=1, db_grain=14, grainc=14, db_mode=0)

ret_mask_2 = kagefunc.retinex_edgemask(clip16, rt_sigma=0.0)
ret_mask_2 = core.resize.Point(ret_mask_2, format=vs.YUV420P16, matrix_s="709")
filtered_2 = core.std.MaskedMerge(debanded_2, clip16, ret_mask_2)
# ------- #

# ---f3_thr_det=1--- #
debanded_3 = gfa.GradFun3(clip16, smode=6, thr_det=1, db_grain=14, grainc=14, db_mode=0)

ret_mask_3 = kagefunc.retinex_edgemask(clip16, rt_sigma=0.0)
ret_mask_3 = core.resize.Point(ret_mask_3, format=vs.YUV420P16, matrix_s="709")
filtered_3 = core.std.MaskedMerge(debanded_3, clip16, ret_mask_3)
# ------- #

# ---f4_thr_det=2--- #
debanded_4 = gfa.GradFun3(clip16, smode=6, thr_det=2, db_grain=14, grainc=14, db_mode=0)

ret_mask_4 = kagefunc.retinex_edgemask(clip16, rt_sigma=0.0)
ret_mask_4 = core.resize.Point(ret_mask_4, format=vs.YUV420P16, matrix_s="709")
filtered_4 = core.std.MaskedMerge(debanded_4, clip16, ret_mask_4)
# ------- #

# ---f5_denois(low)--- #
denoised_5 = core.knlm.KNLMeansCL(
    clip16,
    h=0.1,
    d=2,
    a=3,
    wmode=0,
    wref=1,
    s=1,
    channels="Y",
    device_type="GPU",
    device_id=1,
)
denoised_5 = core.knlm.KNLMeansCL(
    denoised_2,
    h=0.20,
    d=2,
    a=3,
    wmode=0,
    wref=1,
    s=1,
    channels="UV",
    device_type="GPU",
    device_id=1,
)

ret_mask_5 = kagefunc.retinex_edgemask(clip16, rt_sigma=0.0)
ret_mask_5 = core.resize.Point(ret_mask_2, format=vs.YUV420P16, matrix_s="709")
filtered_5 = core.std.MaskedMerge(denoised_5, clip16, ret_mask_5)
# ------- #

# ---f6_denois_thr_det=8--- #
denoised_6 = core.knlm.KNLMeansCL(
    clip16,
    h=0.15,
    d=2,
    a=3,
    wmode=0,
    wref=1,
    s=1,
    channels="Y",
    device_type="GPU",
    device_id=1,
)
denoised_6 = core.knlm.KNLMeansCL(
    denoised_6,
    h=0.25,
    d=2,
    a=3,
    wmode=0,
    wref=1,
    s=1,
    channels="UV",
    device_type="GPU",
    device_id=1,
)
debanded_6 = gfa.GradFun3(denoised_6, smode=6, thr_det=8, db_grain=14, grainc=14, db_mode=0)

ret_mask_6 = kagefunc.retinex_edgemask(clip16, rt_sigma=0.2)
ret_mask_6 = core.resize.Point(ret_mask_6, format=vs.YUV420P16, matrix_s="709")
filtered_6 = core.std.MaskedMerge(debanded_6, clip16, ret_mask_6)
# ------- #

# ---f7_denois(max)_thr_det=10--- #
denoised_7 = core.knlm.KNLMeansCL(
    clip16,
    h=3.45,
    d=2,
    a=3,
    wmode=0,
    wref=0.8,
    s=4,
    channels="Y",
    device_type="GPU",
    device_id=1,
)
denoised_7 = core.knlm.KNLMeansCL(
    denoised_7,
    h=3.55,
    d=2,
    a=3,
    wmode=0,
    wref=1,
    s=4,
    channels="UV",
    device_type="GPU",
    device_id=1,
)
debanded_7 = gfa.GradFun3(denoised_7, smode=6, thr_det=10, db_grain=64, grainc=64, db_mode=0)

ret_mask_7 = kagefunc.retinex_edgemask(clip16, rt_sigma=0)
ret_mask_7 = ret_mask_7.std.Maximum().std.Maximum().std.Inflate().std.Inflate()
ret_mask_7 = core.resize.Point(ret_mask_7, format=vs.YUV420P16, matrix_s="709")
filtered_7 = core.std.MaskedMerge(debanded_7, clip16, ret_mask_7)
# ------- #

# ---f8_denois(maxmin)_thr_det=10--- #
denoised_8 = core.knlm.KNLMeansCL(
    clip16,
    h=1.85,
    d=2,
    a=3,
    wmode=0,
    wref=0.8,
    s=4,
    channels="Y",
    device_type="GPU",
    device_id=1,
)
denoised_8 = core.knlm.KNLMeansCL(
    denoised_8,
    h=1.95,
    d=2,
    a=3,
    wmode=0,
    wref=1,
    s=4,
    channels="UV",
    device_type="GPU",
    device_id=1,
)
debanded_8 = gfa.GradFun3(denoised_8, smode=6, thr_det=10, db_grain=64, grainc=64, db_mode=0)

ret_mask_8 = kagefunc.retinex_edgemask(clip16, rt_sigma=0)
ret_mask_8 = ret_mask_8.std.Maximum().std.Maximum().std.Inflate().std.Inflate()
ret_mask_8 = core.resize.Point(ret_mask_8, format=vs.YUV420P16, matrix_s="709")
filtered_8 = core.std.MaskedMerge(debanded_8, clip16, ret_mask_8)
# ------- #

# ---f9_denois(maxminmin)_thr_det=6--- #
denoised_9 = core.knlm.KNLMeansCL(
    clip16,
    h=0.65,
    d=2,
    a=3,
    wmode=0,
    wref=0.8,
    s=4,
    channels="Y",
    device_type="GPU",
    device_id=1,
)
denoised_9 = core.knlm.KNLMeansCL(
    denoised_9,
    h=0.75,
    d=2,
    a=3,
    wmode=0,
    wref=1,
    s=4,
    channels="UV",
    device_type="GPU",
    device_id=1,
)
debanded_9 = gfa.GradFun3(denoised_9, smode=6, thr_det=6, db_grain=64, grainc=64, db_mode=0)

ret_mask_9 = kagefunc.retinex_edgemask(clip16, rt_sigma=0)
ret_mask_9 = ret_mask_9.std.Maximum().std.Maximum().std.Inflate().std.Inflate()
ret_mask_9 = core.resize.Point(ret_mask_9, format=vs.YUV420P16, matrix_s="709")
filtered_9 = core.std.MaskedMerge(debanded_9, clip16, ret_mask_9)
# ------- #

# ---f10_denois(maxminminmin)_thr_det=4--- #
denoised_10 = core.knlm.KNLMeansCL(
    clip16,
    h=0.45,
    d=2,
    a=3,
    wmode=0,
    wref=0.8,
    s=4,
    channels="Y",
    device_type="GPU",
    device_id=1,
)
denoised_10 = core.knlm.KNLMeansCL(
    denoised_10,
    h=0.55,
    d=2,
    a=3,
    wmode=0,
    wref=1,
    s=4,
    channels="UV",
    device_type="GPU",
    device_id=1,
)
debanded_10 = gfa.GradFun3(denoised_10, smode=6, thr_det=4, db_grain=64, grainc=64, db_mode=0)

ret_mask_10 = kagefunc.retinex_edgemask(clip16, rt_sigma=0)
ret_mask_10 = ret_mask_10.std.Maximum().std.Maximum().std.Inflate().std.Inflate()
ret_mask_10 = core.resize.Point(ret_mask_10, format=vs.YUV420P16, matrix_s="709")
filtered_10 = core.std.MaskedMerge(debanded_10, clip16, ret_mask_10)
# ------- #

# ---f11_denois(maxminminmin)_thr_det=10_grain--- #
denoised_11 = core.knlm.KNLMeansCL(
    clip16,
    h=1.85,
    d=2,
    a=3,
    wmode=0,
    wref=0.8,
    s=4,
    channels="Y",
    device_type="GPU",
    device_id=1,
)
denoised_11 = core.knlm.KNLMeansCL(
    denoised_11,
    h=1.95,
    d=2,
    a=3,
    wmode=0,
    wref=1,
    s=4,
    channels="UV",
    device_type="GPU",
    device_id=1,
)
debanded_11 = gfa.GradFun3(denoised_11, smode=6, thr_det=10, db_grain=16, grainc=16, db_mode=0)

ret_mask_11 = kagefunc.retinex_edgemask(clip16, rt_sigma=0.1)
ret_mask_11 = core.resize.Point(ret_mask_11, format=vs.YUV420P16, matrix_s="709")
filtered_11 = core.std.MaskedMerge(debanded_11, clip16, ret_mask_11)
# ------- #

# ---f12_denois(maxminminmin)_thr_det=10_grain--- #
denoised_12 = core.knlm.KNLMeansCL(
    clip16,
    h=0.65,
    d=2,
    a=3,
    wmode=0,
    wref=0.8,
    s=4,
    channels="Y",
    device_type="GPU",
    device_id=1,
)
denoised_12 = core.knlm.KNLMeansCL(
    denoised_12,
    h=0.55,
    d=2,
    a=3,
    wmode=0,
    wref=1,
    s=4,
    channels="UV",
    device_type="GPU",
    device_id=1,
)
debanded_12 = gfa.GradFun3(denoised_12, smode=6, thr_det=10, db_grain=16, grainc=16, db_mode=0)

ret_mask_12 = kagefunc.retinex_edgemask(clip16, rt_sigma=0.1)
ret_mask_12 = core.resize.Point(ret_mask_12, format=vs.YUV420P16, matrix_s="709")
filtered_12 = core.std.MaskedMerge(debanded_12, clip16, ret_mask_12)
# ------- #

# ---f13_denois(maxminminmin)_thr_det=4_grain=f10--- #
denoised_13 = core.knlm.KNLMeansCL(
    clip16,
    h=0.45,
    d=2,
    a=3,
    wmode=0,
    wref=0.8,
    s=4,
    channels="Y",
    device_type="GPU",
    device_id=1,
)
denoised_13 = core.knlm.KNLMeansCL(
    denoised_13,
    h=0.55,
    d=2,
    a=3,
    wmode=0,
    wref=1,
    s=4,
    channels="UV",
    device_type="GPU",
    device_id=1,
)
debanded_13 = gfa.GradFun3(denoised_13, smode=6, thr_det=4, db_grain=16, grainc=16, db_mode=0)

ret_mask_13 = kagefunc.retinex_edgemask(clip16, rt_sigma=0.1)
ret_mask_13 = core.resize.Point(ret_mask_13, format=vs.YUV420P16, matrix_s="709")
filtered_13 = core.std.MaskedMerge(debanded_13, clip16, ret_mask_13)
# ------- #

# ---f14_denois(maxminminmin)_thr_det=4_grain--- #
denoised_14 = core.knlm.KNLMeansCL(
    clip16,
    h=0.20,
    d=2,
    a=3,
    wmode=0,
    wref=0.8,
    s=4,
    channels="Y",
    device_type="GPU",
    device_id=1,
)
denoised_14 = core.knlm.KNLMeansCL(
    denoised_14,
    h=0.30,
    d=2,
    a=3,
    wmode=0,
    wref=1,
    s=4,
    channels="UV",
    device_type="GPU",
    device_id=1,
)
debanded_14 = gfa.GradFun3(denoised_14, smode=6, thr_det=4, db_grain=16, grainc=16, db_mode=0)

ret_mask_14 = kagefunc.retinex_edgemask(clip16, rt_sigma=0.1)
ret_mask_14 = core.resize.Point(ret_mask_14, format=vs.YUV420P16, matrix_s="709")
filtered_14 = core.std.MaskedMerge(debanded_14, clip16, ret_mask_14)
# ------- #

# ---f15_denois(maxminminmin)_thr_det=4_grain--- #
denoised_15 = core.knlm.KNLMeansCL(
    clip16,
    h=0.20,
    d=2,
    a=3,
    wmode=0,
    wref=0.8,
    s=4,
    channels="Y",
    device_type="GPU",
    device_id=1,
)
denoised_15 = core.knlm.KNLMeansCL(
    denoised_15,
    h=0.30,
    d=2,
    a=3,
    wmode=0,
    wref=1,
    s=4,
    channels="UV",
    device_type="GPU",
    device_id=1,
)
debanded_15 = gfa.GradFun3(denoised_15, smode=6, thr_det=4, db_grain=16, grainc=16, db_mode=0)

ret_mask_15 = kagefunc.retinex_edgemask(clip16, rt_sigma=0.1)
ret_mask_15 = ret_mask_15.std.Maximum().std.Maximum().std.Inflate().std.Inflate()
ret_mask_15 = core.resize.Point(ret_mask_15, format=vs.YUV420P16, matrix_s="709")
filtered_15 = core.std.MaskedMerge(debanded_15, clip16, ret_mask_15)
# ------- #

# --to10 #
f0 = core.fmtc.bitdepth(epis, bits=10)
f2 = core.fmtc.bitdepth(filtered_2, bits=10)
f3 = core.fmtc.bitdepth(filtered_3, bits=10)
f4 = core.fmtc.bitdepth(filtered_4, bits=10)
f5 = core.fmtc.bitdepth(filtered_5, bits=10)
f6 = core.fmtc.bitdepth(filtered_6, bits=10)
f7 = core.fmtc.bitdepth(filtered_7, bits=10)
f8 = core.fmtc.bitdepth(filtered_8, bits=10)
f9 = core.fmtc.bitdepth(filtered_9, bits=10)
f10 = core.fmtc.bitdepth(filtered_10, bits=10)
f11 = core.fmtc.bitdepth(filtered_11, bits=10)
f12 = core.fmtc.bitdepth(filtered_12, bits=10)
f13 = core.fmtc.bitdepth(filtered_13, bits=10)
f14 = core.fmtc.bitdepth(filtered_14, bits=10)
f15 = core.fmtc.bitdepth(filtered_15, bits=10)
# ------- #

# f0<f5<f3<f4&f2<f1<f6<f10<f9<f8<f7 ; f15<f14<f13<f12<f11
# ---m--- #
y4m = fvf.dn.rfs(y4m, f3, "[4600 4803]")
y4m = fvf.dn.rfs(y4m, f0, "[5000 5442]")
y4m = fvf.dn.rfs(y4m, f4, "[6121 6168]")
y4m = fvf.dn.rfs(y4m, f5, "[7332 7454]")
y4m = fvf.dn.rfs(y4m, f3, "[7779 7910]")
y4m = fvf.dn.rfs(y4m, f4, "[10617 10754]")
y4m = fvf.dn.rfs(y4m, f3, "[14550 14825]")
y4m = fvf.dn.rfs(y4m, f5, "[18484 18558]")
y4m = fvf.dn.rfs(y4m, f5, "[22476 22591]")
y4m = fvf.dn.rfs(y4m, f3, "[31564 31692]")
y4m = fvf.dn.rfs(y4m, f3, "[33782 33961]")
y4m = fvf.dn.rfs(y4m, f5, "[34196 34267]")
y4m = fvf.dn.rfs(y4m, f5, "[34519 34806]")
y4m = fvf.dn.rfs(y4m, f3, "[35833 35940]")
y4m = fvf.dn.rfs(y4m, f3, "[42664 42664]")
y4m = fvf.dn.rfs(y4m, f5, "[43134 43214]")
y4m = fvf.dn.rfs(y4m, f2, "[46916 47083]")
y4m = fvf.dn.rfs(y4m, f5, "[48866 49559]")
y4m = fvf.dn.rfs(y4m, f3, "[50549 50602]")
y4m = fvf.dn.rfs(y4m, f3, "[51395 53671]")
y4m = fvf.dn.rfs(y4m, f3, "[55911 56052]")
y4m = fvf.dn.rfs(y4m, f2, "[56239 56328]")
y4m = fvf.dn.rfs(y4m, f5, "[58160 58201]")
y4m = fvf.dn.rfs(y4m, f3, "[58268 58435]")
y4m = fvf.dn.rfs(y4m, f3, "[59163 59315]")
y4m = fvf.dn.rfs(y4m, f3, "[59608 59667]")
y4m = fvf.dn.rfs(y4m, f3, "[60403 60474]")
y4m = fvf.dn.rfs(y4m, f3, "[61492 61557]")
y4m = fvf.dn.rfs(y4m, f5, "[64166 64325]")
y4m = fvf.dn.rfs(y4m, f3, "[69170 69241]")
y4m = fvf.dn.rfs(y4m, f6, "[81708 82144]")
y4m = fvf.dn.rfs(y4m, f7, "[82684 83234]")
y4m = fvf.dn.rfs(y4m, f8, "[87643 88224]")
y4m = fvf.dn.rfs(y4m, f7, "[88453 89141]")
y4m = fvf.dn.rfs(y4m, f7, "[90200 90784]")
y4m = fvf.dn.rfs(y4m, f5, "[92229 92288]")
y4m = fvf.dn.rfs(y4m, f5, "[103219 103340]")
y4m = fvf.dn.rfs(y4m, f3, "[106952 107143]")
y4m = fvf.dn.rfs(y4m, f3, "[116278 116349]")
y4m = fvf.dn.rfs(y4m, f3, "[118504 118563]")
y4m = fvf.dn.rfs(y4m, f9, "[85287 85529]")
y4m = fvf.dn.rfs(y4m, f8, "[85554 85661]")
y4m = fvf.dn.rfs(y4m, f7, "[85662 85826]")
# y4m = fvf.dn.rfs(y4m, f10, "[85995 86088]")
y4m = fvf.dn.rfs(y4m, f10, "[86843 87295]")
y4m = fvf.dn.rfs(y4m, f9, "[87296 87438]")
y4m = fvf.dn.rfs(y4m, f5, "[108489 108584]")
y4m = fvf.dn.rfs(y4m, f10, "[89370 89501]")
y4m = fvf.dn.rfs(y4m, f13, "[89828 90043]")
y4m = fvf.dn.rfs(y4m, f6, "[90044 90055]")
y4m = fvf.dn.rfs(y4m, f10, "[90056 90145]")
y4m = fvf.dn.rfs(y4m, f13, "[90146 90199]")
y4m = fvf.dn.rfs(y4m, f9, "[90785 90976]")
y4m = fvf.dn.rfs(y4m, f10, "[90977 91491]")
y4m = fvf.dn.rfs(y4m, f6, "[83235 83354]")
y4m = fvf.dn.rfs(y4m, f10, "[83391 83510]")
y4m = fvf.dn.rfs(y4m, f10, "[83511 83546]")
y4m = fvf.dn.rfs(y4m, f12, "[83966 84094]")
y4m = fvf.dn.rfs(y4m, f14, "[84095 84369]")
y4m = fvf.dn.rfs(y4m, f11, "[84370 84519]")
y4m = fvf.dn.rfs(y4m, f15, "[89696 89827]")

# y4m = fvf.dn.rfs(y4m, f12, "[29012 29107]")
y4m = fvf.dn.rfs(y4m, f12, "[29012 29107]")
y4m = fvf.dn.rfs(y4m, f13, "[29229 29276]")
y4m = fvf.dn.rfs(y4m, f13, "[14333 14392]")

y4m = fvf.dn.rfs(y4m, f8, "[82456 82563]")
# ------- #

y4m.set_output()

# y4m.std.Trim(83287, 86259).set_output()
# ret_mask_3.std.Deflate().set_output()

# atf.MakeTestEncode(y4m).set_output()
# core.tcm.TColorMask(epis, ['$e9e9e7'], 10, gray=False.set_output()
# atf.DiffRescaleMask(epis, descale_h=720, kernel='bicubic', mthr=50).set_output()
# core.std.ShufflePlanes(clip, 0, GRAY).set_output()
# core.hist.Luma(clip).set_output()
# ret_mask.set_output()
# core.std.Interleave([epis,core.fmtc.bitdepth(clip, bits=8)]).set_output()
