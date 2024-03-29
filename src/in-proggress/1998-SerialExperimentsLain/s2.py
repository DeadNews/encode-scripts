import dnfunc as dn
from vapoursynth import core

# ----in---- #
epname = dn.fname(__file__)
epis = dn.source(f"./in/{epname}.mp4")


def _crop_rel(epis):
    return epis.std.CropRel(top=14, bottom=14, left=246, right=250)


# ----di---- #
# epis_back = epis
epis_back = _crop_rel(epis)

mrgc = core.yadifmod.Yadifmod(epis, edeint=core.nnedi3.nnedi3(epis, 1), order=1, mode=0)
mrgc = _crop_rel(mrgc)

# maybe deint is not needed here at all?
# something with captions — 7738
# mrgc = dn.rfs_resc(mrgc, epis_back, desc_h=320, mthr=200, maps=[(1934, 2009)]) #test
# ---------- #

# ----in---- #
F1 = dn.filt(mrgc)
# ---------- #

# ---out---- #
clip = dn.out(F1, epname)
clip = clip.std.AssumeFPS(fpsnum=30000, fpsden=1001)
clip.set_output()
# ---------- #

# ---save--- #
# dn.pw4(mrgc, 2, 1, epis_back, clip).set_output()
# epis.set_output()
# dn.rfs_resc(mrgc, epis_back, desc_h=320, mthr=200, out_mask=True).set_output()
# ---------- #

# ---err---- #
dn.check_num_frames(epis, clip)
# ---------- #
