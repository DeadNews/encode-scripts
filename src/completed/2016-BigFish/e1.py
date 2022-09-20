import dnfunc as dn
from lvsfunc import misc

# -----in----- #
epname = dn.fname(__file__)

epis = dn.source(f"./in/{epname}.mp4")
epis = epis.std.Crop(top=138, bottom=138)
# ------------ #

# -----ef----- #
epis_back = epis
planes = dn.split(epis)

y = (
    planes[0]
    .edgefixer.Continuity(top=1, left=1, radius=1)
    .edgefixer.Continuity(top=2, bottom=1, left=2)
)
u = planes[1].edgefixer.Continuity(top=1, left=1, radius=1)
v = planes[2].edgefixer.Continuity(top=1, left=1, radius=1)

yuv = dn.join([y, u, v])
ref = yuv.std.BoxBlur(hradius=1, hpasses=2, vpasses=2)

eef = misc.wipe_row(yuv, ref, pos=(0, 0), size=(1920, 1))
eef = misc.wipe_row(eef, ref, pos=(0, 0), size=(1, 804))

epis = dn.rfs(eef, epis_back, (141996, 151712))
# ------------ #

# ----mrgc---- #
mrgc = dn.rfs_dehalo(epis)
mrgc = dn.rfs_dehalo(mrgc, zone="2nd")
# ------------ #

# ----filt---- #
F1 = dn.filt(mrgc)
F2 = dn.filt(mrgc, zone="hard")
F3 = dn.filt(mrgc, zone="lite")

F1 = dn.rfs(F1, F2, (1860, 4071))
F1 = dn.rfs(F1, F3, (88849, 112094))
# ------------ #

# ----out----- #
clip = dn.out(F1, epname)
clip.set_output()
# ------------ #

# ----save---- #
# dn.pw(mrgc, None, None, epis_back, clip).set_output()
# dn.pw(mrgc, [2, 3, 4, 6], 'main', epis_back, clip).set_output()
"""
2: 108636 110652 110942 112382 113534 114394 114412 115834 117852
2: 35386
6: db 331960
6: 77644 106156 574960 600016
"""
# epis.set_output()
# clip.std.Trim(57206, 57500).set_output()
# ------------ #

# ----err----- #
dn.check_num_frames(epis, clip)
# ------------ #
