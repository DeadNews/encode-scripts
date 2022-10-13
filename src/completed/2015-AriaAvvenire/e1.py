import dnfunc as dn

# -----in----- #
epname = dn.fname(__file__)

Part_B = dn.chapt(epname, "Part_B")
ED = dn.chapt(epname, "ED")
EDend = dn.chapt(epname, "EDend")

epis = dn.source(f"./in/{epname}.mp4")
# ------------ #

# ----mrgc---- #
epis, epis_back, _ = dn.edgefix(epis)

mrgc = dn.aa(epis)
mrgc = dn.rfs_dehalo(mrgc)
# ------------ #

# ----mask---- #
mrgc = dn.rfs_resc(mrgc, epis, zone="resc1", maps=[(Part_B - 88, Part_B - 1)])
mrgc = dn.rfs_resc(mrgc, epis, zone="resc2", maps=[(ED, EDend - 1)])
# ------------ #

# ----filt---- #
F1 = dn.filt(mrgc)
# ------------ #

# ----out----- #
clip = dn.out(F1, epname)
clip.set_output()
# ------------ #

# ----save---- #
# dn.pw(mrgc, None, None, epis_back, clip).set_output()
# dn.pw(mrgc, [2, 3, 4, 6], 'main', epis_back, clip).set_output()
"""
2: 19436 23180 20010
"""
# epis.set_output()
# ------------ #

# ----err----- #
dn.check_num_frames(epis, clip)
# ------------ #
