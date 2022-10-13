import dnfunc as dn

# -----in----- #
epname = dn.fname(__file__)

Part_01 = dn.chapt(epname, "Part_01")
Part_07 = dn.chapt(epname, "Part_07")
ED = dn.chapt(epname, "ED")
EDend = dn.chapt(epname, "EDend", "Next")

epis = dn.source(f"./in/{epname}.mp4")
# ------------ #

# ----mrgc---- #
aaep = dn.aa(epis)
mrgc = dn.rfs_dehalo(aaep)
# ------------ #

# ----mask---- #
mrgc = dn.rfs(mrgc, epis, [(0, Part_01), (ED, EDend - 1)])

mrgc = dn.rfs_resc(mrgc, epis, mthr=48)  # all
# ------------ #

# ----filt---- #
F1 = dn.filt(mrgc)
F2 = dn.filt(mrgc, zone="ed")
F3 = dn.filt(mrgc, zone="next")

F1 = dn.rfs(F1, F2, [(ED, EDend - 1)])
F1 = dn.rfs(F1, F3, [(Part_07, ED - 1)])
# ------------ #

# ----out----- #
clip = dn.out(F1, epname)
clip.set_output()
# ------------ #

# ----save---- #
# dn.pw(mrgc, None, None, epis, clip).set_output()
# dn.pw(mrgc, [2, 3, 4, 6], 'main', epis, clip).set_output()
# dn.pw(mrgc, [3, 4, 6], 'next', epis, clip, 'next').set_output()
"""
2: 293984
6: 881956
"""
# epis.set_output()
clip.std.Trim(Part_07, EDend - 1).set_output()
# dn.rfs_resc(epis=epis, mthr=48, out_mask=True).set_output()
# ------------ #

# ----err----- #
dn.check_num_frames(epis, clip)
# ------------ #
