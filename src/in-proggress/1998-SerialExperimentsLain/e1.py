import dnfunc as dn

# ----in---- #
epname = dn.fname(__file__)

OP = dn.chapt(epname, "OP")
OPend = dn.chapt(epname, "Part_A")
ED = dn.chapt(epname, "ED")
EDend = dn.chapt(epname, "EDend")

epis = dn.source(f"./in/{epname}.mp4")

# ----ef---- #
epis, _crop = dn.crop(epis)
epis_back, epis, edgefixer = dn.edgefix(epis)

dehalo = dn.rfs_dehalo(epis)
mrgc = dn.rfs(dehalo, epis, [(OP, OPend - 1), (ED, EDend - 1)])
# ---------- #

# ---filt--- #
F1 = dn.filt(mrgc)
F2 = dn.filt(mrgc, zone="op")
F3 = dn.filt(mrgc, zone="ed")

F1 = dn.rfs(F1, F2, [(OP, OPend - 1)])
F1 = dn.rfs(F1, F3, [(ED, EDend - 1)])
# ---------- #

# ---out---- #
clip = dn.out(F1, epname)
clip.set_output()
# ---------- #

# ---save--- #
# dn.pw(mrgc, None, None, epis_back, clip).set_output()
# dn.pw(mrgc, [2, 3, 4, 6], 'main', epis_back, clip).set_output()
"""
ef 48678 55658
db 59982 15218 63322 71482 83002  44518 22918 89718 74222 78544 73410
ha 21410 14690 55218 59538 31618 38338 87622 24466 33246
"""
# epis.set_output()
# clip.std.Trim(3589, 6589).set_output()
# dn.rfs_dehalo(epis, zone='main', out_mask=True).set_output() # 3674
# ---------- #

# ---err---- #
dn.check_num_frames(epis, clip)
# ---------- #
