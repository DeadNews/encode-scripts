import dnfunc as dn

# -----in----- #
epname = dn.fname(__file__)

epis = dn.source(f"./in/{epname}.mp4", fpsnum=24000, fpsden=1001)
# ------------ #

# -----aa----- #
aaep = dn.aa(epis, epname)
mrgc = dn.rfs_resc(aaep, epis, mthr=20)
# ------------ #

# ----filt---- #
F1 = dn.filt(mrgc, zone="me")
# ------------ #

# ----out----- #
clip = dn.out(F1, epname)
clip.set_output()
# ------------ #

# ----save---- #
# dn.pw(mrgc, None, None, epis, clip).set_output()
# epis.set_output()
# dn.rfs_resc(epis=epis, mthr=20, out_mask=True).set_output()
# ------------ #

# ----err----- #
dn.check_num_frames(epis, clip)
# ------------ #
