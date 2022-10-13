import dnfunc as dn

# -----in----- #
epname = dn.fname(__file__)

ED = 0

epis = dn.source(f"./in/{epname}.mp4")
# ------------ #

# -----aa----- #
mrgc = epis

mrgc = dn.rfs_repair(mrgc, maps=[(ED + 748, ED + 2157)])  # ed repair
# ------------ #

# ----filt---- #
F1 = dn.filt(mrgc, zone="ed")
F2 = dn.filt(mrgc, zone="ed_grain")

F1 = dn.rfs(F1, F2, [(ED + 24, ED + 275), (ED + 748, ED + 1562), (ED + 1910, ED + 2157)])
# ------------ #

# ----out----- #
# clip = dn.out(F1, epname)
clip = dn.out(F1, epname, fpsnum=24000, fpsden=1001)
clip.set_output()
# ------------ #

# ----save---- #
# dn.pw(mrgc, [2, 3, 4, 6], 'ed', epis, clip).set_output()
# epis.set_output()
# ------------ #

# ----err----- #
dn.check_num_frames(epis, clip)
# ------------ #
