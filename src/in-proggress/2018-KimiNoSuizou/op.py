import dnfunc as dn

# -----in----- #
epname = dn.fname(__file__)

jpn = dn.source(f"./in/{epname}.mp4")
usa = dn.source(f"./in/usa/{epname}.mp4")

epis = dn.average([jpn, usa, usa, jpn])
# ------------ #

# -----ef----- #
epis, epis_back, _ = dn.edgefix(epis)
# ------------ #

# ----mrgc---- #
aaep = dn.aa(epis)

mrgc = dn.rfs_resc(aaep, epis)
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
"""
2: 2192
"""
# epis.set_output()
# ------------ #

# ----err----- #
dn.check_num_frames(epis, clip)
# ------------ #
