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

mrgc = dn.rfs(mrgc, epis, f"[{ED} {EDend-1}]")  # ed2
# ------------ #-1

# ----filt---- #
F1 = dn.filt(mrgc)
F2 = dn.filt(mrgc, zone="edop")
F3 = dn.filt(mrgc, zone="ed2")
F4 = dn.filt(mrgc, zone="soft2")

F1 = dn.rfs(F1, F2, f"[{OP} {OPend-1}]")
F1 = dn.rfs(F1, F3, f"[{ED} {EDend-1}]")
F1 = dn.rfs(F1, F4, f"[{OP+1818} {OP+1973}]")
# ------------ #

# ----out----- #
clip = dn.out(F1, epname)
clip.set_output()
# ------------ #

# ----save---- #
# dn.pw(mrgc, None, None, epis, clip).set_output()
# dn.pw(mrgc, [1, 2, 3, 4, 6], 'main', epis, clip).set_output()
"""
7: 32149 28068 25457 67527
2: 1314 19102 28374 7446
1: 657 9551 14274
"""
# epis.set_output()
# dn.rfs_resc(epis=epis, mthr=18, out_db_mode=True, zone='868p').set_output()
# ------------ #

# ----err----- #
dn.check_num_frames(epis, clip)
# ------------ #
