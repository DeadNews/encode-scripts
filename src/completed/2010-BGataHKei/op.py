import dnfunc as dn

# -----in----- #
epname = dn.fname(__file__)

epis = dn.source(f"./in/{epname}.mp4").std.AssumeFPS(fpsnum=24000, fpsden=1001)
# ------------ #

# -----aa----- #
aaep = dn.aa(epis)
aaep = dn.aa(aaep, zone="eedi3")

mrgc = dn.rfs_dehalo(aaep)
mrgc = dn.rfs_dehalo(mrgc, zone="2nd")
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
# epis.set_output()
# ------------ #

# ----err----- #
dn.check_num_frames(epis, clip)
# ------------ #
