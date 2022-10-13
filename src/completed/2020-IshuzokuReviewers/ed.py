import dnfunc as dn

# -----in----- #
epname = dn.fname(__file__)

ED = 0

epis = dn.source(f"./in/{epname}.mp4")
# ------------ #

# -----aa----- #
mrgc = epis
# ------------ #

# ----filt---- #
F1 = dn.filt(mrgc, zone="oped")
F2 = dn.filt(mrgc, zone="ed_lite")

F1 = dn.rfs(F1, F2, [(ED + 1066, ED + 1469)])
# ------------ #

# ----out----- #
clip = dn.out(F1, epname)
clip.set_output()
# ------------ #

# ----save---- #
# epis.set_output()
# ------------ #

# ----err----- #
dn.check_num_frames(epis, clip)
# ------------ #
