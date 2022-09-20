import dnfunc as dn

# -----in----- #
epname = dn.fname(__file__)

epis = dn.source(f"./in/{epname}.mp4")
# ------------ #

# ----mrgc---- #
aaep = dn.aa(epis)
mrgc = aaep
# ------------ #

# ----mask---- #
mrgc = dn.rfs_dehalo(mrgc)

End = epis.num_frames
mrgc = dn.rfs_resc(mrgc, epis, maps=f"[{End-144} {End-1}]")  # title
# ------------ #

# ----filt---- #
F1 = dn.filt(mrgc)
# ------------ #

# ----out----- #
# clip = dn.out(F1, epname)
clip = dn.out(F1, epname, fpsnum=24000, fpsden=1001)
clip.set_output()
# ------------ #

# ----save---- #
# dn.pw(mrgc, None, None, epis, clip).set_output()
# dn.pw(mrgc, [2, 3, 4, 6], 'main', epis, clip).set_output()
"""
"""
# epis.set_output()
# ------------ #

# ----err----- #
dn.check_num_frames(epis, clip)
# ------------ #
