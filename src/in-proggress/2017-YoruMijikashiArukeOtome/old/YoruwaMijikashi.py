import fvsfunc as fvf
import gradfun_amod as gfa
import kagefunc
import vapoursynth as vs
from vapoursynth import core

core.set_max_cache_size(10000)
core.avs.LoadPlugin(r"c:/#prog/CLI/dgdecnv/x64 Binaries/DGDecodeNV.dll")

epis = core.avs.DGSource(r"..\dgi\Yoru wa Mijikashi.dgi")

# ---f--- #
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

# ---f2--- #
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

# ---f3--- #
debanded_3 = gfa.GradFun3(clip16, smode=6, thr_det=1, db_grain=14, grainc=14, db_mode=0)

ret_mask_3 = kagefunc.retinex_edgemask(clip16, rt_sigma=0.0)
ret_mask_3 = core.resize.Point(ret_mask_3, format=vs.YUV420P16, matrix_s="709")
filtered_3 = core.std.MaskedMerge(debanded_3, clip16, ret_mask_3)
# ------- #

# ---m--- #
filtered = dn.rfs(filtered, filtered_3, [(5000, 5442)])
filtered = dn.rfs(filtered, filtered_2, [(31564, 31994)])
filtered = dn.rfs(filtered, filtered_2, [(51395, 53671)])
filtered = dn.rfs(filtered, filtered_2, [(56383, 58964)])
# ------- #

clip = filtered
clip.set_output()

# atf.MakeTestEncode(clip).set_output()
# core.tcm.TColorMask(epis, ['$e9e9e7'], 10, gray=False.set_output()
# atf.DiffRescaleMask(epis, descale_h=720, kernel='bicubic', mthr=50).set_output()
# core.std.ShufflePlanes(clip, 0, GRAY).set_output()
# core.hist.Luma(clip).set_output()
# ret_mask.set_output()
# core.std.Interleave([epis,core.fmtc.bitdepth(clip, bits=8)]).set_output()
