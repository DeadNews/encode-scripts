import dnfunc as dn

# -----in----- #
epname = dn.fname(__file__)

OP = dn.chapt(epname, "OP")
OPend = dn.chapt(epname, "Part_A")
ED = dn.chapt(epname, "ED")
EDend = dn.chapt(epname, "End")

epis = dn.source(f"./in/{epname}.mp4")
# ------------ #

# ----mrgc---- #
aaep = dn.aa(epis, zone="868p")
mrgc = aaep
mrgc = dn.rfs_resc(mrgc, epis, mthr=18, zone="868p")
# ------------ #

# ----mask---- #
mrgc = dn.rfs_dehalo(mrgc)

mrgc = dn.rfs(mrgc, epis, [(ED, EDend - 1)])  # ed2
# ------------ #-1

# ----filt---- #
F1 = dn.filt(mrgc, zone="soft")  # <<
F2 = dn.filt(mrgc, zone="edop")
F3 = dn.filt(mrgc, zone="ed2")
F4 = dn.filt(mrgc, zone="soft2")

F1 = dn.rfs(F1, F2, [(OP, OPend - 1)])
F1 = dn.rfs(F1, F3, [(ED, EDend - 1)])
F1 = dn.rfs(F1, F4, [(11358, 14024), (OP + 1818, OP + 1973)])
# ------------ #

# ----out----- #
clip = dn.out(F1, epname)
clip.set_output()
# ------------ #

# ----save---- #
# dn.pw(mrgc, None, None, epis, clip).set_output()
# dn.pw(mrgc, [1, 2, 3, 4, 6], 'main', epis, clip).set_output()
"""
68780 81310 84334 155021
"""
# epis.set_output()
# dn.rfs_resc(epis=epis, mthr=18, out_db_mode=True, zone='868p').set_output()
# ------------ #

# ----err----- #
dn.check_num_frames(epis, clip)
# ------------ #
