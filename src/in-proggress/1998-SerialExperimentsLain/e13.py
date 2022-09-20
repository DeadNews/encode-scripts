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
mrgc = dn.rfs(dehalo, epis, f"[{OP} {OPend-1}] [{ED} {EDend-1}]")
# ---------- #

# ---filt--- #
F1 = dn.filt(mrgc)
F2 = dn.filt(mrgc, zone="op")
F3 = dn.filt(mrgc, zone="ed")
F4 = dn.filt(mrgc, ag_saveblack=2)  # black

F1 = dn.rfs(F1, F2, f"[{OP} {OPend-1}]")
F1 = dn.rfs(F1, F3, f"[{ED} {EDend-1}]")
# F1 = dn.rfs(F1, F4, "[]")
# ---------- #

# ---out---- #
clip = dn.out(F1, epname)
clip.set_output()
# ---------- #

# ---save--- #
# dn.pw(mrgc, [3, 4], 'main', epis, clip).set_output()
# dn.pw(mrgc, [1, 2, 3, 4, 5, 6], 'main', epis, clip).set_output()
# epis.set_output()
# ---------- #

# ---err---- #
dn.check_num_frames(epis, clip)
