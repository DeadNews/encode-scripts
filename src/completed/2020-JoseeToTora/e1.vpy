import dnfunc as dn
from lvsfunc import misc

# -----in----- #
epname = dn.fname(__file__)

Avant = dn.chapt(epname, "Avant")
Part_A = dn.chapt(epname, "Part_A")
ED = dn.chapt(epname, "ED")
EDend = dn.chapt(epname, "Epilog")
EOF = dn.chapt(epname, "EOF")

epis_back = dn.source(f"./in/{epname}.mp4")
epis = epis_back.std.Crop(top=138, bottom=138)
# ------------ #

# ----mrgc---- #
planes = dn.split(epis)

y = planes[0].std.Crop(bottom=1).edgefixer.Continuity(left=1, right=1)

y_aa = dn.aa(y)  # aa
y_aa = dn.rfs_resc(y_aa, y)  # all
maps_aa = [(Avant, Part_A - 1), (ED, EDend - 1), (141080, EOF - 1)]  # titles
y = dn.rfs_resc(y_aa, y, zone="titles", maps=maps_aa)

y = y.std.AddBorders(bottom=1).edgefixer.Continuity(bottom=1, radius=1)  # fix bot

u = planes[1].edgefixer.Continuity(bottom=1)
v = planes[2].edgefixer.Continuity(bottom=1)

yuv = dn.join([y, u, v])

ref = yuv.std.BoxBlur(hradius=1, hpasses=0, vpasses=2)
yuv = misc.wipe_row(yuv, ref, pos=(0, 803), size=(1920, 1))
mrgc = yuv.edgefixer.Continuity(bottom=1, radius=1)
# ------------ #

# ----mrgc---- #
mrgc = dn.rfs_dehalo(mrgc)
mrgc = dn.rfs_dehalo(mrgc, zone="2nd")

mrgc = dn.rfs(mrgc, epis, (0, 940))  # promo
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
1: 134362
2: resc 268724
2: aa 111300 112740 52578 117056 54018 55458 55454 56322
2: ha 52002
2: db 278174 239234 169020
6: 834526 717706 507064
"""
# epis.set_output()
# dn.rfs_resc(epis=epis, out_mask=True).set_output()
# dn.rfs_resc(epis=y, zone="titles", out_mask=True).set_output()
# ------------ #

# ----err----- #
dn.check_num_frames(epis, clip)
# ------------ #
