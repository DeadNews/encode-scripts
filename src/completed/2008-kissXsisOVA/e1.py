import dnfunc as dn

# -----in----- #
epname = dn.fname(__file__)

ED = dn.chapt(epname, "ED")
EDend = dn.chapt(epname, "EDend")

epis = dn.source(f"./in/{epname}.mp4")

# -----ef----- #
epis_back, epis_ef, edgefixer = dn.edgefix(epis)
#
epis_ef_left = epis.edgefixer.Continuity(top=2, bottom=3, left=3, right=7)
epis_ef_right = epis.edgefixer.Continuity(top=2, bottom=3, left=6, right=3)  # right=3

epis_ef = dn.rfs(epis_ef, epis_ef_left, "[23714 24033] [25868 25875]")  # left fix
epis_ef = dn.rfs(epis_ef, epis_ef_right, "[18255 18327] [14896 14961]")  # right fix
#
epis = epis_ef
# ------------ #

# ----mrgc---- #
aaep = dn.aa(epis, zone="low")
mrgc = aaep
# ------------ #

# ----mask---- #
mrgc = dn.rfs_qtgmc(mrgc, aaep, k=1, maps="[29774 30033] [22045 22173] [23714 24033]")

mrgc = dn.rfs_dehalo(mrgc, zone="low")

mrgc = dn.rfs(mrgc, epis, f"[{ED} {EDend-1}]")  # ed
# ------------ #

# ----filt---- #
F1 = dn.filt(mrgc)
# ------------ #

# ----out----- #
clip = dn.out(F1, epname)
clip.set_output()
# ------------ #

# ----save---- #
# dn.pw4(mrgc, 2, 1, epis_back, clip).set_output()
# dn.pw8(mrgc, 4, 7, 2, 5, 6, epis_back, clip, 0, zone='main').set_output()
"""
ef 73202 103478 95642
db 6622 18622 105358 122432 104706 106146
aa 104438 65210 66650
ha 27943 99119 73682 29382
"""
# epis.set_output()
# clip.std.Trim(0, Part_A-1).set_output()
# dn.rfs_dehalo(aaep, zone='main', out_mask=True).set_output()
# ------------ #

# ----err----- #
dn.check_num_frames(epis, clip)
# ------------ #
