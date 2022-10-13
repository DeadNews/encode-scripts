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
F4 = dn.filt(mrgc, ag_saveblack=2)  # black

F1 = dn.rfs(F1, F2, [(OP, OPend - 1)])
F1 = dn.rfs(F1, F3, [(ED, EDend - 1)])
# F1 = dn.rfs(F1, F4, [(, )])
# ---------- #

# ---out---- #
clip = dn.out(F1, epname)
clip.set_output()
# ---------- #

# ---save--- #
# dn.pw4(mrgc, 2, 1, epis_back, clip).set_output()
# dn.pw8(mrgc, 4, 7, 2, 5, 6, epis_back, clip, 0, zone='main').set_output()
# epis.set_output()
# ---------- #

# ---err---- #
dn.check_num_frames(epis, clip)
# ---------- #
