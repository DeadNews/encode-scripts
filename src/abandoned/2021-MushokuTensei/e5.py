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

# ----epis---- #
epis_back = epis
nc = dn.source(f"./in/nc{epname[1:]}.mp4")

epis = nc + epis.std.Trim(nc.num_frames, epis.num_frames - 1)
# ------------ #

# ----mask---- #
aaep = dn.aa(epis)  # eedi
mrgc = dn.rfs_resc(aaep, epis, zone="resc")  # all
# ------------ #

# ----filt---- #
F1 = dn.filt(mrgc)
F2 = dn.filt(mrgc, zone="past")
F3 = dn.filt(mrgc, zone="lite")

F1 = dn.rfs(F1, F2, (24736, 24867))
F1 = dn.rfs(F1, F3, [(20532, 21521), (25862, 25983), (26168, 26203)])
# ------------ #

# ----out----- #
clip = dn.out(F1, epname)
clip.set_output()
# ------------ #

# ----save---- #
# dn.pw(mrgc, None, None, epis_back, clip).set_output()
# dn.pw(mrgc, [2, 3, 4, 6], 'main', epis, clip).set_output()
# dn.pw(mrgc, [3, 4, 5, 6], 'main', epis, clip).set_output()
"""
1:
2: 41264 44746 51582 51792 54840
6: 155380 51790 123802
"""
# epis.set_output()
# dn.rfs_resc(epis=epis, out_mask=True, zone="resc").set_output()
# ------------ #

# ----err----- #
dn.check_num_frames(epis, clip)
# ------------ #
