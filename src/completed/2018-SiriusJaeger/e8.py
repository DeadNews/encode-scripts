import dnfunc as dn

# -----in----- #
epname = dn.fname(__file__)

OP = dn.chapt(epname, "OP")
OPend = dn.chapt(epname, "Part_A")
Part_B = dn.chapt(epname, "Part_B")
ED = dn.chapt(epname, "ED")
EDend = dn.chapt(epname, "Part_C", "Next")
Next = dn.chapt(epname, "Next")
End = dn.chapt(epname, "End")

map_op = [(OP, OPend - 1)]
map_ed = [(ED, EDend - 1)]
map_next = [(Next, End - 1)]
map_title = [(ED - 60, ED - 1)]
map_mid = [(Part_B - 48, Part_B - 1)]

epis = dn.source(f"./in/{epname}.mp4")
epis, epis_back, edgefixer = dn.edgefix(epis)
# ------------ #

# ----mrgc---- #
aaep = dn.aa(epis)
aaep = dn.rfs_dehalo(aaep)
ed = dn.oped(epis_back, name="ed", offset=0, start=ED, end=EDend)

mrgc = aaep.std.Trim(0, ED - 1) + ed + aaep.std.Trim(EDend, epis.num_frames - 1)
# ------------ #

# ----mask---- #
mrgc = dn.rfs(mrgc, epis_back, map_op)
mrgc = dn.rfs(mrgc, epis, map_next)
mrgc = dn.rfs(mrgc, epis, map_title)
mrgc = dn.rfs(mrgc, epis, map_mid)
# ------------ #

# ----filt---- #
F1 = dn.filt(mrgc)
F2 = dn.filt(mrgc, zone="ed")
F3 = dn.filt(mrgc, zone="op")
F4 = dn.filt(mrgc, zone="next")
F5 = dn.filt(mrgc, zone="title")

F1 = dn.rfs(F1, F2, map_ed)
F1 = dn.rfs(F1, F3, map_op)
F1 = dn.rfs(F1, F4, map_next)
F1 = dn.rfs(F1, F5, map_title)
# ------------ #

# ----out----- #
clip = dn.out(F1, epname)
clip.set_output()
# ------------ #

# ----save---- #
# dn.pw4(mrgc, 2, 1, epis_back, clip).set_output()
# dn.pw8(mrgc, 4, 7, 2, 5, 6, epis_back, clip, 0, zone='main').set_output()
"""
"""
# epis.set_output()
# clip.std.Trim(Next, epis.num_frames-1).set_output()
# ------------ #

# ----err----- #
dn.check_num_frames(epis, clip)
# ------------ #
