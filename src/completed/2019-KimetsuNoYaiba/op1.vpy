import dnfunc as dn

# -----in----- #
epname = dn.fname(__file__)

jpn = dn.source(f"./in/{epname}.mp4")
ita = dn.source(f"./in/ita/{epname}.mp4")
epis = dn.average([jpn, ita])
# ------------ #

# -----aa----- #
aaep = dn.aa(epis, epname)
mrgc = aaep
# ------------ #

# ----mask---- #
mrgc = dn.rfs_hard(mrgc, mrgc, mthr=20, yuv=True, maps="[293 397]")
# mrgc = dn.rfs_qtgmc(mrgc, mrgc, k=1, maps="[293 397]")
# ------------ #

# ----filt---- #
F1 = dn.filt(mrgc)
F2 = dn.filt(mrgc, zone="noise_op")
F3 = dn.filt(mrgc, zone="grain_op")

F1 = dn.rfs(F1, F2, "[0 282]")
F1 = dn.rfs(F1, F3, "[1169 1398]")
# ------------ #

# ----out----- #
clip = dn.out(F1, epname)
clip.set_output()
# ------------ #

# ----save---- #
# dn.pw(mrgc, None, None, epis, clip).set_output()
# epis.set_output()
# clip.std.Trim(0, 302).set_output()
# clip.std.Trim(1100, 1398).set_output()
# clip.std.Trim(293, 397).set_output()
# ------------ #

# ----err----- #
dn.check_num_frames(epis, clip)
# ------------ #
