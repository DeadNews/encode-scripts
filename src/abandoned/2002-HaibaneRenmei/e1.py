import dnfunc as dn
from vapoursynth import core

# -----in----- #
epname = dn.fname(__file__)

# ED = dn.chapt(epname, 'ED')
# EDend = dn.chapt(epname, 'Part_C', 'Next')
# Next = dn.chapt(epname, 'Next')

# epis = dn.source(f'./in/{epname}.mp4')
epis = dn.source(
    "/run/media/deadnews/data1/temp/灰羽联盟BDMV/灰羽連盟 Blu-ray BOX DISC1/HAIBANE_RENMEI_BD_01/BDMV/STREAM/00002.m2ts"
)
# ------------ #

# ----fix----- #
epis_back = epis
epis = core.yadifmod.Yadifmod(epis, edeint=core.nnedi3.nnedi3(epis, 1), order=1, mode=0)
# ------------ #

# ----mrgc---- #
aaep = dn.aa(epis)
mrgc = aaep

# mrgc = dn.rfs_repair(mrgc)
mrgc = dn.rfs_dehalo(mrgc)
# mrgc = dn.rfs_linedark(mrgc)

# from havsfunc import LSFmod
# mrgc = LSFmod(mrgc, defaults="slow", strength=150)
# mrgc = mrgc.warp.AWarpSharp2(type=1, blur=2, depth=4)
mrgc = mrgc.warp.AWarpSharp2(depth=16, chroma=1)
# clip = core.cas.CAS(aaep, sharpness=0.1)

# mrgc = dn.qtgmc(mrgc, k=1, sharp=0.0)  # <<<
# ------------ #

# ----filt---- #
F1 = dn.filt(mrgc)

# sharp?
# ------------ #

# ----out----- #
clip = dn.out(F1, epname)
clip.set_output()
dn.downscale(clip, 720).set_output()
# ------------ #

# ----save---- #
# dn.pw(mrgc, None, None, epis, clip).set_output()
# dn.pw(mrgc, [3, 4], 'main', epis, clip).set_output()
# dn.pw(mrgc, [1, 2, 3, 4, 5, 6], 'main', epis, clip).set_output()
"""
2: 1976 9996 30397 32916 39934
1: 4195
"""
# epis.set_output()
# clip.std.Trim(7102, 7502).set_output()
# dn.rfs_dehalo(aaep, zone='main', out_mask=True).set_output()
# ------------ #

# ----err----- #
dn.check_num_frames(epis, clip)
