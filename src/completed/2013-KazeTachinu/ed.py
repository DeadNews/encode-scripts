import dnfunc as dn
from vapoursynth import core

# -----in----- #
epname = dn.fname(__file__)

jpn = dn.source(f"./in/{epname}.mp4")
usa = dn.source(f"./in/2nd/{epname}.mp4")
# ------------ #

# ----mrgc---- #
jpn_trim = jpn.std.Trim(0, usa.num_frames - 1 - 46)
usa_trim = usa.std.Trim(46, usa.num_frames - 1)
mean = core.average.Mean([jpn_trim, usa_trim])
epis = mean
# ------------ #

# ----mrgc---- #
epis = epis.std.CropRel(top=20, bottom=20)

planes = dn.split(epis)

y = planes[0]
u = planes[1].edgefixer.Continuity(top=2, bottom=2)
v = planes[2].edgefixer.Continuity(top=2, bottom=2)

mrgc = dn.join([y, u, v])
# ------------ #

# ----filt---- #
F1 = dn.filt(mrgc)
# ------------ #

# ----out----- #
clip = dn.out(F1, epname)
# clip = dn.out(F1, epname, fpsnum=24000, fpsden=1001)
clip.set_output()
# ------------ #

# ----save---- #
# dn.pw(mrgc, None, None, epis, clip).set_output()
"""
"""
# mrgc.set_output()
# ------------ #
