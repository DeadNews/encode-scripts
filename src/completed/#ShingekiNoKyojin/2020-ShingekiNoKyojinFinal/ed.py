import dnfunc as dn

# -----in----- #
epname = dn.fname(__file__)

epis = dn.source(f"./in/{epname}.mp4")
# ------------ #

# ----mrgc---- #
aaep = dn.aa(epis)

mrgc = dn.rfs_resc(aaep, epis, zone="oped")
# ------------ #

# ----filt---- #
F1 = dn.filt(mrgc, zone="ed")
F2 = dn.filt(mrgc, zone="ed_hard")

F1 = dn.rfs(F1, F2, [(0, 270), (1333, 1876)])
# ------------ #

# ----out----- #
clip = dn.out(F1, epname)
clip.set_output()
# ------------ #

# ----save---- #
# dn.pw(mrgc, None, None, epis, clip).set_output()
"""
2: 2784 1921
"""
# epis.set_output()
# ------------ #

# ----err----- #
dn.check_num_frames(epis, clip)
# ------------ #
