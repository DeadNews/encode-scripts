import dnfunc as dn
from vapoursynth import core

# -----in----- #
epname = dn.fname(__file__)
epis = dn.source(f"./in/{epname}.mp4")
# ------------ #

# -----aa----- #
mrgc = epis
mrgc = core.yadifmod.Yadifmod(epis, edeint=core.nnedi3.nnedi3(epis, 1), order=1, mode=0)
# mrgc = core.bwdif.Bwdif(mrgc, field=1)
# ------------ #

# ----filt---- #
F1 = dn.filt(mrgc, sm_thr=320, dn_pref=True, db_mode=2, db_gf_mode=3)
# ------------ #

# ----out----- #
clip = dn.out(F1, epname)
# clip = clip.std.AssumeFPS(fpsnum=30000, fpsden=1001)
clip.set_output()
# ------------ #

# ----save---- #
# dn.pw(mrgc, [3, 4], 'main', epis, clip).set_output()
# epis.set_output()
# ------------ #

# ----err----- #
dn.check_num_frames(epis, clip)
# ------------ #
# ------------ #
