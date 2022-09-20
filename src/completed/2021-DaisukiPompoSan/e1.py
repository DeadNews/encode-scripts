import dnfunc as dn
from lvsfunc import misc

# -----in----- #
epname = dn.fname(__file__)

OP = dn.chapt(epname, "OP")
OPend = dn.chapt(epname, "Part_A")
Part_B = dn.chapt(epname, "Part_B")
ED = dn.chapt(epname, "ED")
EDend = dn.chapt(epname, "EDend", "Next")
Next = dn.chapt(epname, "Next")
EOF = dn.chapt(epname, "EOF")

epis_back = dn.source(f"./in/{epname}.mp4")
epis = epis_back.std.Crop(top=20, bottom=22)
# ------------ #

# ----mrgc---- #
planes = dn.split(epis)

y = planes[0].std.Crop(top=1).edgefixer.Continuity(top=1).std.AddBorders(top=1)
u = planes[1].edgefixer.Continuity(top=1)
v = planes[2].edgefixer.Continuity(top=1)

yuv = dn.join([y, u, v])

ref = yuv.std.BoxBlur(hradius=1, hpasses=0, vpasses=2)
yuv = misc.wipe_row(yuv, ref, pos=(0, 0), size=(1920, 1))
mrgc = yuv.edgefixer.Continuity(top=1, radius=1).edgefixer.Continuity(bottom=1)
# ------------ #

# ----filt---- #
F1 = dn.filt(mrgc)
# ------------ #

# ----out----- #
clip = dn.out(F1, epname)
clip.set_output()
# ------------ #

# ----save---- #
# dn.pw(mrgc, None, None, epis, clip).set_output()
# dn.pw(mrgc, [2, 3, 4, 6], 'main', epis, clip).set_output()
"""
1:
2: 58728 55956 97520
6:
"""
# epis.set_output()
# ------------ #

# ----err----- #
dn.check_num_frames(epis, clip)
# ------------ #
