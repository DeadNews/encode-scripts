import dnfunc as dn

# -----in----- #
epname = dn.fname(__file__)

OP = dn.chapt(epname, "OP")
OPend = dn.chapt(epname, "Part_A")
ED = dn.chapt(epname, "ED")
EDend = dn.chapt(epname, "Next", "EDend")

jpn = dn.source(f"./in/{epname}.mp4")
ita = dn.source(f"./in/2nd/{epname}.mp4")
epis = dn.average([jpn, ita])

epis, epis_back, edgefixer = dn.edgefix(epis)
# ------------ #

# ----mrgc---- #
aaep = dn.aa(epis)
mrgc = dn.rfs_image(aaep, epis, "ef")  # fix bot
# ------------ #

# ----mask---- #
mrgc = dn.rfs(mrgc, epis_back, [(ED, EDend - 1)])  # ed
mrgc = dn.rfs_repair(mrgc, maps=[(ED, EDend - 1)])  # ed repair
# ------------ #

# ----filt---- #
F1 = dn.filt(mrgc)
F2 = dn.filt(mrgc, zone="op")
F3 = dn.filt(mrgc, zone="ed")
F4 = dn.filt(mrgc, zone="noise")

F1 = dn.rfs(F1, F2, [(OP, OPend - 1)])
F1 = dn.rfs(F1, F3, [(ED, EDend - 1)])
F1 = dn.rfs(F1, F4, [(576, 2812)])
# ------------ #

# ----out----- #
clip = dn.out(F1, epname)
clip.set_output()
# ------------ #

# ----save---- #
# dn.pw(mrgc, None, None, epis_back, clip).set_output()
# dn.pw(mrgc, [2, 3, 4, 6], 'main', epis_back, clip).set_output()
"""
"""
# epis.set_output()
# clip.std.Trim(576, 2812).set_output()
# ------------ #

# ----err----- #
dn.check_num_frames(epis, clip)
# ------------ #
