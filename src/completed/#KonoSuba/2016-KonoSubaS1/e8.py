import dnfunc as dn

# -----in----- #
epname = dn.fname(__file__)

OP = dn.chapt(epname, "OP")
OPend = dn.chapt(epname, "Part_A")
ED = dn.chapt(epname, "ED")
EDend = dn.chapt(epname, "Next")

epis = dn.source(f"./in/{epname}.mp4")
# ------------ #

# ----mrgc---- #
aaep = dn.aa(epis)
op = dn.oped(epis, name="op", offset=24, start=OP, end=OPend)
ed = dn.oped(epis, name="ed", offset=24, start=ED, end=EDend)

mrgc = (
    aaep.std.Trim(0, OP - 1)
    + op
    + aaep.std.Trim(OPend, ED - 1)
    + ed
    + epis.std.Trim(EDend, epis.num_frames - 1)
)
# ------------ #

# ----mask---- #
mrgc = dn.rfs_dehalo(mrgc)
mrgc = dn.rfs_qtgmc(mrgc, mrgc, k=2, maps=f"[{ED} {ED+173}]")  # <<<<<<<<<<<<<<<<<<
# ------------ #

# ----filt---- #
F1 = dn.filt(mrgc)
F2 = dn.filt(mrgc, zone="oped")
F3 = dn.filt(mrgc, zone="limb")
F4 = dn.filt(mrgc, sm_thr=50)
F5 = dn.filt(mrgc, sm_thr=120)

F1 = dn.rfs(F1, F2, f"[{OP} {OPend-1}] [{ED} {EDend-1}]")
F1 = dn.rfs(F1, F3, f"[{OP+1092} {OP+1280}]")
F1 = dn.rfs(F1, F4, "[21711 21842] [26198 26347] [26552 26587]")
F1 = dn.rfs(F1, F5, "[20691 20960] [20997 21113] [21597 21638]")
# ------------ #

# ----out----- #
clip = dn.out(F1, epname)
clip.set_output()
# ------------ #

# ----save---- #
# dn.pw(mrgc, [1, 2, 3, 4, 6], 'main', epis, clip, 'old').set_output()
# dn.pw(mrgc, [1, 2, 3, 4, 5, 6, 7], 'main', epis, clip, 'old').set_output()
"""
aa 177061 91349 98221 100141 39925
db 212621 216461 217421 95341 195271 44734 218381 224141 885 168813
--10
142290 210440 212840 238090 24000 241690 258490 263290 26390 272890  218386 211447 217737
265567 310777
ha 51077
"""
# epis.set_output()
# clip.std.Trim(20613, 21638).set_output()
# clip.std.Trim(14054, 15713).set_output()
# ------------ #

# ----err----- #
dn.check_num_frames(epis, clip)
# ------------ #
