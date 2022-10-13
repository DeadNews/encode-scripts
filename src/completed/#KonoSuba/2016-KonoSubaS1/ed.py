import dnfunc as dn

# -----in----- #
epname = dn.fname(__file__)

epis = dn.source(f"./in/{epname}.mp4")
# ------------ #

# -----aa----- #
aaep = dn.aa(epis, epname)
mrgc = aaep
mrgc = dn.rfs_dehalo(mrgc)

mrgc = dn.rfs_qtgmc(mrgc, mrgc, k=2, maps=[(26, 197)])
# ------------ #

# ----filt---- #
F1 = dn.filt(mrgc, zone="oped")
# ------------ #

# ----out----- #
clip = dn.out(F1, epname)
clip.set_output()
# ------------ #

# ----save---- #
# dn.pw4(mrgc, 2, 4, epis, clip).set_output()
# epis.set_output()
# ------------ #

# ----err----- #
dn.check_num_frames(epis, clip)
# ------------ #
