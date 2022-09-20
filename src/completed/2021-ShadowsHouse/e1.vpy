import dnfunc as dn

# -----in----- #
epname = dn.fname(__file__)

OP = dn.chapt(epname, "OP")
OPend = dn.chapt(epname, "Part_A")
Part_B = dn.chapt(epname, "Part_B")
ED = dn.chapt(epname, "ED")
EDend = dn.chapt(epname, "Next", "EOF")
Next = dn.chapt(epname, "Next")
EOF = dn.chapt(epname, "EOF")

epis = dn.source(f"./in/{epname}.mp4")
# ------------ #

# ----mrgc---- #
aaep = dn.aa(epis)

mrgc = dn.rfs_resc(aaep, epis, maps=[(OP, OPend - 1), (ED, EDend - 1)], zone="resc")
# ------------ #

# ----filt---- #
F1 = dn.filt(mrgc)
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
2: 60594 61170 62322 66564 58290 58002 27482 18652
6:
"""
# epis.set_output()
# dn.rfs_resc(epis=epis, out_mask=True, zone="resc").set_output()
# ------------ #

# ----err----- #
dn.check_num_frames(epis, clip)
# ------------ #
