import dnfunc as dn

# -----in----- #
epname = dn.fname(__file__)

epis = dn.source(f"./in/{epname}.mp4", fpsnum=24000, fpsden=1001)
# ------------ #

# -----aa----- #
aaep = dn.aa(epis, epname)
mrgc = aaep
# ------------ #

# ----filt---- #
F1 = dn.filt(mrgc, zone="ed2")
# ------------ #

# ----out----- #
clip = dn.out(F1, epname)
clip.set_output()
# ------------ #

# ----save---- #
# dn.pw(mrgc, None, None, epis, clip).set_output()
# epis.set_output()
# ------------ #

# ----err----- #
dn.check_num_frames(epis, clip)
# ------------ #