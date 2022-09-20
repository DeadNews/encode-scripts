import dnfunc as dn

# -----in----- #
epname = dn.fname(__file__)

epis = dn.source(f"./in/{epname}.mp4")
# ------------ #

# ----mrgc---- #
epis, epis_back, edgefixer = dn.edgefix(epis)

aaep = dn.aa(epis)
mrgc = aaep
mrgc = dn.rfs_resc(mrgc, epis, mthr=75)
# ------------ #

# ----filt---- #
F1 = dn.filt(mrgc)
# ------------ #

# ----out----- #
clip = dn.out(F1, epname)
clip.set_output()
# ------------ #

# ----save---- #
# dn.pw(mrgc, [3, 4], 'main', epis, clip).set_output()
# dn.pw(mrgc, [1, 2, 3, 4, 5, 6], 'main', epis, clip).set_output()
"""
"""
# epis.set_output()
# dn.rfs_resc(mrgc, epis, mthr=75, out_mask=True).set_output()
# ------------ #

# ----err----- #
dn.check_num_frames(epis, clip)
# ------------ #
