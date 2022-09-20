import dnfunc as dn

# -----in----- #
epname = dn.fname(__file__)

epis = dn.source(f"./in/{epname}.mp4")
# ------------ #

# ----mrgc---- #
aaep = dn.aa(epis, yuv=False)
aaep = dn.rfs_dehalo(aaep)
mrgc = aaep
# ------------ #

# ----mask---- #
mrgc = dn.rfs_resc(mrgc, epis, mthr=110)
# ------------ #

# ----filt---- #
F1 = dn.filt(mrgc, db_saveblack=2)
# ------------ #

# ----out----- #
clip = dn.out(F1, epname, fpsnum=24000, fpsden=1001)
clip.set_output()
# ------------ #

# ----save---- #
# dn.pw4(mrgc, 2, 1, epis, clip).set_output()
# dn.pw8(mrgc, 4, 7, 2, 5, 6, epis, clip, 0, zone='main').set_output()
"""
"""
# epis.set_output()
# clip.std.Trim(Next, epis.num_frames-1).set_output()
# clip.std.Trim(ED, EDend-1).set_output()

# dn.rfs_resc(epis=epis, mthr=110, out_db_mode=True, zone='resc_fix').set_output()
# dn.rfs_dehalo(aaep, zone='main', out_mask=True).set_output()
# dn.planes(clip)[2].set_output()
# ------------ #

# ----err----- #
dn.check_num_frames(epis, clip)
# ------------ #
