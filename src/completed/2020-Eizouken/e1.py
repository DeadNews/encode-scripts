import dnfunc as dn

# -----in----- #
epname = dn.fname(__file__)

OP = dn.chapt(epname, "OP")
OPend = dn.chapt(epname, "Part_A")
ED = dn.chapt(epname, "ED")
EDend = dn.chapt(epname, "EDend")

epis = dn.source(f"./in/{epname}.mp4")
# ------------ #

# ----mrgc---- #
aaep = dn.aa(epis, zone="eedi3")  # 1080
mrgc = aaep
# ------------ #

# ----mask---- #
mrgc = dn.rfs_dehalo(mrgc)

mrgc = dn.rfs(mrgc, epis, [(OP, OPend - 1), (ED, EDend - 1)])  # op ed

mrgc = dn.rfs_repair(mrgc, maps=[(ED + 724, ED + 2133)])  # ed repair
# ------------ #

# ----filt---- #
F1 = dn.filt(mrgc)
F2 = dn.filt(mrgc, zone="op")
F3 = dn.filt(mrgc, zone="ed")
F4 = dn.filt(mrgc, zone="ed_grain")
F5 = dn.filt(mrgc, zone="lite")
F6 = dn.filt(mrgc, zone="hard")

F1 = dn.rfs(F1, F2, [(OP, OPend - 1)])
F1 = dn.rfs(F1, F3, [(ED, EDend - 1)])
F1 = dn.rfs(F1, F4, [(ED, ED + 251), (ED + 724, ED + 1538), (ED + 1886, ED + 2133)])
F1 = dn.rfs(F1, F5, [(2960, 3132), (3171, 3266)])
F1 = dn.rfs(F1, F6, [(11836, 12095), (12156, 12359), (12500, 12691)])
# ------------ #

# ----out----- #
clip = dn.out(F1, epname)
clip.set_output()
# ------------ #

# ----save---- #
# dn.pw(mrgc, None, None, epis, clip).set_output()
# dn.pw(mrgc, [2, 3, 4, 6], 'main', epis, clip).set_output()
"""
1: 1507 3049 4869 10264 13979 14123 34720 34864 10696
2: aa 28246 6098! 3014 20528 9738 69440 69728 68102 21392 13912
2: db 23092 27958 28644 26330 28634 31226 32090 32954 43898 45914 28932 51166
6: 69274 137746 126215
6: 78994 83878 85906 86800 93682 96274 98866 131698 137746 153498
"""
# epis.set_output()
# ------------ #

# ----err----- #
dn.check_num_frames(epis, clip)
# ------------ #
