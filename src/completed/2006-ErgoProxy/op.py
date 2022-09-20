import dnfunc as dn

# -----in----- #
epname = dn.fname(__file__)

jpn = dn.source(f"./in/{epname}.mp4")
ita = dn.source(f"./in/2nd/{epname}.mp4")
epis = dn.average([jpn, ita])

epis, epis_back, edgefixer = dn.edgefix(epis)
# ------------ #

# -----aa----- #
aaep = dn.aa(epis, epname)
mrgc = dn.rfs_image(aaep, epis, "ef")  # fix bot
# ------------ #

# ----filt---- #
F1 = dn.filt(mrgc, zone="op")
# ------------ #

# ----out----- #
clip = dn.out(F1, epname, fpsnum=24000, fpsden=1001)
clip.set_output()
# ------------ #

# ----save---- #
# dn.pw(mrgc, None, None, epis, clip).set_output()
# dn.pw(mrgc, [2, 3, 4, 6], 'main', epis, clip).set_output()
"""
1818 2396
"""
# epis.set_output()
# ------------ #

# ----err----- #
dn.check_num_frames(epis, clip)
# ------------ #
