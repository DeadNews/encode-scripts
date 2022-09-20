import dnfunc as dn

# -----in----- #
epname = dn.fname(__file__)

epis = dn.source(f"./in/{epname}.mp4")
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
# dn.pw(mrgc, None, None, epis, clip).set_output()
# dn.pw(mrgc, [2, 3, 4, 6], 'main', epis, clip).set_output()
"""
1:
2: 22178 51946 23908 25636 26788 28804 29668
6:
"""
# epis.set_output()
# dn.rfs_resc(epis=epis, out_mask=True).set_output()
# ------------ #

# ----err----- #
dn.check_num_frames(epis, clip)
# ------------ #
