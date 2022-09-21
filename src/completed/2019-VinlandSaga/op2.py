import dnfunc as dn

# -----in----- #
epname = dn.fname(__file__)

epis = dn.source(f"./in/{epname}.mp4")
# ------------ #

# -----aa----- #
aaep = dn.aa(epis, epname, zone="868p")
mrgc = aaep

mrgc = dn.rfs_resc(mrgc, epis, mthr=18, zone="868p")

mrgc = dn.rfs_dehalo(mrgc)
# ------------ #

# ----filt---- #
F1 = dn.filt(mrgc, zone="ed2")
F2 = dn.filt(mrgc, zone="soft2")

F1 = dn.rfs(F1, F2, "[1866 2021]")
# ------------ #

# ----out----- #
clip = dn.out(F1, epname)
# clip = dn.out(F1, epname, fpsnum=24000, fpsden=1001)
clip.set_output()
# ------------ #

# ----save---- #
# dn.pw(mrgc, None, None, epis, clip).set_output()
"""
2: 2404 3844 1254 674 1314
1: 1202 627 337 657 772
"""
# epis.set_output()
# dn.rfs_resc(epis=epis, mthr=18, out_db_mode=True, zone='868p').set_output()
# ------------ #

# ----err----- #
dn.check_num_frames(epis, clip)
# ------------ #
