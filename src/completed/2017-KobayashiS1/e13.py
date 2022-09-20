import dnfunc as dn

# -----in----- #
epname = dn.fname(__file__)

OP = dn.chapt(epname, "OP")
OPend = dn.chapt(epname, "Part_A")
Part_B = dn.chapt(epname, "Part_B")

jpn = dn.source(f"./in/{epname}.mp4")
usa = dn.source(f"./in/usa/{epname}.mp4")[24:]

epis = dn.average([jpn, usa, jpn, jpn, jpn, jpn])
# ------------ #

# ----mrgc---- #
mrgc = dn.rfs(epis, jpn, [(OP, OPend - 1)])
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
6: 138184
"""
# epis.set_output()
# ------------ #

# ----err----- #
dn.check_num_frames(epis, clip)
# ------------ #
