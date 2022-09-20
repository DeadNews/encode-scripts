import dnfunc as dn

# -----in----- #
epname = dn.fname(__file__)

epis = dn.source(f"./in/{epname}.mp4")
# ------------ #

# -----aa----- #
aaep = dn.aa(epis, epname)
mrgc = dn.rfs_dehalo(aaep)
mrgc = dn.rfs_resc(mrgc, epis, mthr=18)  # all
# ------------ #

# ----filt---- #
F1 = dn.filt(mrgc)
# ------------ #

# ----out----- #
clip = dn.out(F1, epname, fpsnum=24000, fpsden=1001)
clip.set_output()
# ------------ #

# ----save---- #
# epis.set_output()
# ------------ #

# ----err----- #
dn.check_num_frames(epis, clip)
# ------------ #
