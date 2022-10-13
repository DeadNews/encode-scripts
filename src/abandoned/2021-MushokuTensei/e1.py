import dnfunc as dn

# -----in----- #
epname = dn.fname(__file__)

OP = dn.chapt(epname, "OP")
OPend = dn.chapt(epname, "Part_A")
Part_B = dn.chapt(epname, "Part_B")
ED = dn.chapt(epname, "ED")
EDend = dn.chapt(epname, "EDend", "Next")
Next = dn.chapt(epname, "Next")
EOF = dn.chapt(epname, "EOF")

epis = dn.source(f"./in/{epname}.mp4")
# ------------ #

# -----ef----- #
ef, epis_back, _ = dn.edgefix(epis)

epis = dn.rfs(epis, ef, maps=[(30833, 30904), (31037, 31204)])
# ------------ #

# ----mask---- #
aaep = dn.aa(epis)  # eedi
mrgc = dn.rfs_resc(aaep, epis, zone="resc")  # all

mrgc = dn.rfs(mrgc, epis, maps=[(ED, EDend - 1)])  # ed
# ------------ #

# ----filt---- #
F1 = dn.filt(mrgc)
F2 = dn.filt(mrgc, zone="past")
F3 = dn.filt(mrgc, zone="lite")

F1 = dn.rfs(F1, F2, (0, 2283))
F1 = dn.rfs(F1, F3, (31121, 31204))
# ------------ #

# ----out----- #
clip = dn.out(F1, epname)
clip.set_output()
# ------------ #

# ----save---- #
# dn.pw(mrgc, None, None, epis_back, clip).set_output()
# dn.pw(mrgc, [2, 3, 4, 6], "main", epis_back, clip).set_output()
# dn.pw(mrgc, [3, 4, 6, 7], 'main', epis_back, clip).set_output()
"""
1: 23498 685 33671 23209
2: real 1818
2: 26250 44400 46418 46996 24778 33958 19498
2: 62074 62362 62238
6: 58498 187090 62362
"""
# epis.set_output()
# dn.rfs_resc(epis=epis, out_mask=True, zone="resc").set_output()
# clip.std.Trim(31037, 31120).set_output()
# clip.std.Trim(31037, 31220).set_output()
# ------------ #

# ----err----- #
dn.check_num_frames(epis, clip)
# ------------ #
