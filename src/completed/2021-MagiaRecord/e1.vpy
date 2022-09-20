import dnfunc as dn

# -----in----- #
epname = dn.fname(__file__)

OP = dn.chapt(epname, "OP")
OPend = dn.chapt(epname, "Part_A")
Part_B = dn.chapt(epname, "Part_B")
ED = dn.chapt(epname, "ED")
EDend = dn.chapt(epname, "EDend", "Part_C")
Next = dn.chapt(epname, "Next")
EOF = dn.chapt(epname, "EOF")

epis = dn.source(f"./in/{epname}.mp4")
# ------------ #

# ----mrgc---- #
mrgc = epis
# ------------ #

# ----filt---- #
F1 = dn.filt(mrgc)
F3 = dn.filt(mrgc, zone="harder_e1")

F1 = dn.rfs_image(F1, F3, "e1", maps=(ED, 31423))
# ------------ #

# ----out----- #
clip = dn.out(F1, epname)
clip.set_output()
# ------------ #

# ----save---- #
# dn.pw(mrgc, None, None, epis, clip).set_output()
# dn.pw(mrgc, [2, 3, 4, 6], 'main', epis, clip).set_output()
"""
1:
2: 19108 16516 19396 62356
2: 63766
6:
"""
# epis.set_output()
# ------------ #

# ----err----- #
dn.check_num_frames(epis, clip)
# ------------ #
