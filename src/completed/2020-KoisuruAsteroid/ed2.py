import dnfunc as dn

# -----in----- #
epname = dn.fname(__file__)

ED = 0
EDend = 2182

epis = dn.source(f"./in/{epname}.mp4")
# ------------ #

# -----aa----- #
aaep = dn.aa(epis, epname)
mrgc = dn.rfs_dehalo(aaep)
mrgc = dn.rfs_resc(mrgc, epis, mthr=18)  # all
# ------------ #

# ----filt---- #
F1 = dn.filt(mrgc)
F2 = dn.filt(mrgc, zone="ed1")
F3 = dn.filt(mrgc, zone="ed2")

F1 = dn.rfs(F1, F2, f"[{ED} {ED+875}]")
F1 = dn.rfs(F1, F3, f"[{ED+876} {EDend-1}]")
# ------------ #

# ----mask---- #
F1 = dn.rfs_black_crop(F1, top=158, bot=158, maps=f"[{ED+36} {EDend-1}]")
# ------------ #

# ----out----- #
# clip = dn.out(F1, epname)
clip = dn.out(F1, epname, fpsnum=24000, fpsden=1001)
clip.set_output()
# ------------ #

# ----save---- #
# dn.pw(mrgc, None, None, epis, clip).set_output()
# dn.pw(mrgc, [2, 3, 4, 6], 'main', epis, clip).set_output()
# epis.set_output()
# ------------ #

# ----err----- #
dn.check_num_frames(epis, clip)
# ------------ #
