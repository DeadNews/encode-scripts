import dnfunc as dn

# -----in----- #
epname = dn.fname(__file__)

jpn = dn.source(f"./in/{epname}.mp4").std.AssumeFPS(fpsnum=24000, fpsden=1001)
usa = dn.source(f"./in/usa/{epname}.mp4")[24:].std.AssumeFPS(fpsnum=24000, fpsden=1001)

epis = dn.average([jpn, usa, jpn, jpn, jpn])
# ------------ #

# -----aa----- #
aaep = dn.aa(epis)
mrgc = dn.rfs_resc(aaep, epis)  # all
# ------------ #

# ----filt---- #
F1 = dn.filt(mrgc, zone="ed")
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
