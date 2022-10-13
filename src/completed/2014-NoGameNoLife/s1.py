import dnfunc as dn

# -----in----- #
epname = dn.fname(__file__)

epis = dn.source(f"./in/{epname}.mp4")
# ------------ #

# ----mrgc---- #
aaep = dn.aa(epis)
mrgc = aaep

mrgc = dn.rfs(mrgc, epis, [(4003, epis.num_frames - 1)])  # ed
# ------------ #

# ----filt---- #
F1 = dn.filt(mrgc)
# ------------ #

# ----out----- #
clip = dn.out(F1, epname)
clip.set_output()
# ------------ #

# ----save---- #
# dn.pw4(mrgc, 2, 1, epis, clip).set_output()
# dn.pw8(mrgc, 4, 7, 2, 5, 6, epis, clip, 0, zone='main').set_output()
"""
"""
# epis.set_output()
# dn.rfs_resc(mrgc, epis, mthr=75, out_mask=True).set_output()
# ------------ #

# ----err----- #
dn.check_num_frames(epis, clip)
# ------------ #
