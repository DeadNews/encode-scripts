import dnfunc as dn

# -----in----- #
epname = dn.fname(__file__)

jpn = dn.source(f"./in/{epname}.mp4")
gbr = dn.source(f"./in/gbr/{epname}.mp4")
ita = dn.source(f"./in/ita/{epname}.mp4")[24:]
hkg = dn.source(f"./in/hkg/{epname}.mp4")[48:]

epis = dn.average([jpn, ita, hkg, gbr, jpn, ita, hkg])
# ------------ #

# ----mrgc---- #
epis = dn.crop(epis)[0]

mrgc = epis
# ------------ #

# ----filt---- #
F1 = dn.filt(mrgc, zone="sp")
# ------------ #

# ----out----- #
clip = dn.out(F1, epname)
clip.set_output()
# ------------ #

# ----save---- #
# dn.pw(mrgc, None, None, epis, clip).set_output()
# dn.pw(mrgc, [2, 3, 4, 6], "main", epis, clip).set_output()
"""
1:
2:
6:
"""
# from vapoursynth import core
# core.std.Interleave([epis, jpn]).set_output()

# epis.set_output()
# ------------ #

# ----err----- #
dn.check_num_frames(epis, clip)
# ------------ #
