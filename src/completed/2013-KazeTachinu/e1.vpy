import dnfunc as dn
from vapoursynth import core

# -----in----- #
epname = dn.fname(__file__)

jpn = dn.source(f"./in/{epname}.mp4")
usa = dn.source(f"./in/2nd/{epname}.mp4")
# ------------ #

# ----mrgc---- #
jpn_trim = jpn.std.Trim(817, 181678)
usa_trim = usa.std.Trim(1057, 181918)
mean = core.average.Mean([jpn_trim, usa_trim])
epis = jpn.std.Trim(0, 816) + mean + jpn.std.Trim(181679, jpn.num_frames - 1)
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
# clip = dn.out(F1, epname)
clip = dn.out(F1, epname, fpsnum=24000, fpsden=1001)
clip.set_output()
# ------------ #

# ----save---- #
# dn.pw(mrgc, None, None, epis, clip).set_output()
# dn.pw(mrgc, [2, 3, 4, 6], 'main', epis, clip).set_output()
"""
1: 73471
2: 203180 118210 146942
6:
"""
# mrgc.set_output()
# clip.std.Trim(36212, 46846).set_output()
# dn.split(epis)[1].set_output()
# ------------ #

# ----err----- #
dn.check_num_frames(epis, clip)
# ------------ #
