import dnfunc as dn

# -----in----- #
epname = dn.fname(__file__)

Part_A = dn.chapt(epname, "Part_A")
Part_B = dn.chapt(epname, "Part_B")
ED = dn.chapt(epname, "ED")
EDend = dn.chapt(epname, "EDend")

epis = dn.source(f"./in/{epname}.mp4")
# ------------ #

# ----mrgc---- #
aaep = dn.aa(epis)
mrgc = aaep
# ------------ #

# ----mask---- #
eedi = dn.aa(epis, zone="eedi3")
mrgc = dn.rfs(mrgc, eedi, [(Part_B, Part_B + 71)])

mrgc = dn.rfs_dehalo(mrgc)

mrgc = dn.rfs(mrgc, epis, [(ED, EDend - 1)])  # ed

mrgc = dn.rfs_resc(mrgc, epis, maps=[(0, 143)])  # title
# ------------ #

# ----filt---- #
F1 = dn.filt(mrgc)
F2 = dn.filt(mrgc, zone="ed")

F1 = dn.rfs(F1, F2, [(ED, EDend - 1)])
# ------------ #

# ----out----- #
clip = dn.out(F1, epname)
clip.set_output()
# ------------ #

# ----save---- #
# dn.pw(mrgc, None, None, epis, clip).set_output()
# dn.pw(mrgc, [2, 3, 4, 6], 'main', epis, clip).set_output()
"""
"""
# epis.set_output()
# ------------ #

# ----err----- #
dn.check_num_frames(epis, clip)
# ------------ #
