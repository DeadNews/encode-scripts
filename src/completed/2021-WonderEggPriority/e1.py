import dnfunc as dn

# -----in----- #
epname = dn.fname(__file__)

OP = dn.chapt(epname, "OP")
OPend = dn.chapt(epname, "Part_A")
ED = dn.chapt(epname, "ED")
EDend = dn.chapt(epname, "Next")

epis = dn.source(f"./in/{epname}.mp4")
# ------------ #

# ----mrgc---- #
aaep = dn.aa(epis)
mrgc = dn.rfs_dehalo(aaep)
# ------------ #

# ----mask---- #
mrgc = dn.rfs_resc(mrgc, epis)

if ED is not None:
    mrgc = dn.rfs(mrgc, epis, (ED, EDend - 1))
# ------------ #

# ----filt---- #
F1 = dn.filt(mrgc)
# ------------ #

# ----out----- #
clip = dn.out(F1, epname)
clip.set_output()
# ------------ #

# ----save---- #
# dn.pw(mrgc, None, None, epis, clip).set_output()
# dn.pw(mrgc, [2, 3, 4, 6], 'main', epis, clip).set_output()
"""
1: 14866 15010 20508 25081
2: 29732 30020 41016 50162
6: 89200 90064 123052 150490
6: 33256
"""
# epis.set_output()
# dn.rfs_resc(epis=epis, out_mask=True).set_output()
# dn.rfs_dehalo(aaep, out_mask=True).set_output()
# ------------ #

# ----err----- #
dn.check_num_frames(epis, clip)
# ------------ #
