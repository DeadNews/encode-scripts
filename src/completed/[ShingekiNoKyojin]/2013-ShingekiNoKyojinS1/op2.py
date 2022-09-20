import dnfunc as dn

# -----in----- #
epname = dn.fname(__file__)

jpn = dn.source(f"./in/{epname}.mp4")
ita = (
    dn.source(f"./in/ita/{epname}.mp4")[24:]
    .std.DuplicateFrames(324)
    .std.DuplicateFrames(324)
    .std.DeleteFrames(927)
    .std.DeleteFrames(927)
)
ita = dn.rfs(ita, jpn, [(324, 433)])

epis = dn.average([jpn, ita, jpn, ita, jpn, ita, jpn, ita, jpn, ita])
# ------------ #

# -----aa----- #
aaep = dn.aa(epis)
mrgc = dn.rfs_resc(aaep, epis)  # all
# ------------ #

# ----filt---- #
F1 = dn.filt(mrgc, zone="op")
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
