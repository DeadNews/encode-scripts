import dnfunc as dn

# -----in----- #
epname = dn.fname(__file__)

OP = dn.chapt(epname, "OP")
OPend = dn.chapt(epname, "Part_A")
Part_B = dn.chapt(epname, "Part_B")
ED = dn.chapt(epname, "ED")
EDend = dn.chapt(epname, "Next", "EOF")

epis = dn.source(f"./in/{epname}.mp4")
# ------------ #

# ----mrgc---- #
deha = dn.rfs_dehalo(epis)
aaep = dn.aa(deha)
mrgc = dn.rfs_dehalo(aaep, zone="2nd")
mrgc = dn.rfs_dehalo(mrgc, zone="3nd")

mrgc = dn.rfs(mrgc, aaep, [(OP, OPend - 1), (33022, EDend - 1)])
# ------------ #

# ----mask---- #
mrgc = dn.rfs_resc(mrgc, epis)
mrgc = dn.rfs_resc(mrgc, epis, zone="oped", maps=[(OP, OPend - 1), (ED, EDend - 1)])

mrgc = dn.rfs(mrgc, epis, [(Part_B - 120, Part_B - 1)])
# ------------ #

# ----filt---- #
F1 = dn.filt(mrgc)
F2 = dn.filt(mrgc, zone="op")
F3 = dn.filt(mrgc, zone="ed")
F4 = dn.filt(mrgc, zone="ed_hard")

F1 = dn.rfs(F1, F2, [(OP, OPend - 1)])
F1 = dn.rfs(F1, F3, [(33022, EDend - 1)])
F1 = dn.rfs(F1, F4, [(33272, 33816)])
# ------------ #

# ----out----- #
clip = dn.out(F1, epname)
clip.set_output()
# ------------ #

# ----save---- #
# dn.pw(mrgc, None, None, epis, clip).set_output()
# dn.pw(mrgc, [2, 3, 4, 6], "main", epis, clip).set_output()
"""
1: 10809
2: aa 21906 21618 56838 39910 7710
2; db 24786 39622 39334
"""
# epis.set_output()
# dn.rfs_resc(epis=epis, out_mask=True).set_output()
# dn.rfs_resc(epis=epis, out_mask=True, zone="oped").set_output()
# ------------ #

# ----err----- #
dn.check_num_frames(epis, clip)
# ------------ #
