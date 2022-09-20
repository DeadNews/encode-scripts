import dnfunc as dn

# -----in----- #
epname = dn.fname(__file__)

epis = dn.source(f"./in/{epname}.mp4")

epis = epis.std.Trim(0, 11) + epis.std.Trim(0, 1) + epis
# ------------ #

# ----mrgc---- #
m1 = dn.edge_detect(epis, mode="kirsch2")
mrgc = dn.aa(epis, ext_db_mode=m1)  # eedi3

mrgc = dn.rfs_dehalo(mrgc, ext_db_mode=m1)
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
1400 7663 8528
"""
# epis.set_output()
# ------------ #

# ----err----- #
dn.check_num_frames(epis, clip)
# ------------ #
