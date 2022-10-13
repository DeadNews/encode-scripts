import dnfunc as dn

# -----in----- #
epname = dn.fname(__file__)

Part_B = dn.chapt(epname, "Part_B")
ED = dn.chapt(epname, "ED")

epis = dn.source(f"./in/{epname}.mp4")
# ------------ #

# ----mrgc---- #
aaep = dn.aa(epis)
mrgc = aaep
# ------------ #

# ----mask---- #
maps = [(ED, epis.num_frames - 1)]  # ed
maps += " [821 979]"  # title
maps += f" [{Part_B} {Part_B+71}]"  # title

mrgc = dn.rfs_resc(mrgc, epis, mthr=100, maps=maps, zone="resc")

mrgc = dn.rfs(mrgc, epis, [(32081, 33201)])  # ed window
# ------------ #

# ----filt---- #
F1 = dn.filt(mrgc)
F2 = dn.filt(mrgc, zone="ed2")

F1 = dn.rfs(F1, F2, [(32081, 33201)])  # ed window
# ------------ #

# ----out----- #
clip = dn.out(F1, epname)
clip.set_output()
# ------------ #

# ----save---- #
# dn.pw(mrgc, None, None, epis, clip).set_output()
# dn.pw(mrgc, [2, 3, 4, 6], 'main', epis, clip).set_output()
"""
"""
# epis.set_output()
# dn.rfs_resc(epis=epis, mthr=168, out_db_mode=True, zone='resc').set_output()
# ------------ #

# ----err----- #
dn.check_num_frames(epis, clip)
# ------------ #
