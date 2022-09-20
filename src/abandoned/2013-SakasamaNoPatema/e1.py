import dnfunc as dn

# -----in----- #
epname = dn.fname(__file__)

epis = dn.source(f"./in/{epname}.mp4")
# ------------ #

# ----mrgc---- #
aaep = dn.aa(epis)
aaep = dn.rfs_dehalo(aaep)
mrgc = dn.rfs(aaep, epis, f"[0 792]")
# ------------ #

# ----filt---- #
F1 = dn.filt(mrgc)
F2 = dn.filt(mrgc, db_saveblack=2, ag_str=0)

F1 = dn.rfs(F1, F2, "[0 792] [138814 142175]")
# ------------ #

# ----out----- #
clip = dn.out(F1, epname)
clip.set_output()
# ------------ #

# ----save---- #
# dn.pw(mrgc, [1, 2, 3, 4, 5, 6], 'main', epis, clip).set_output()
"""
aa 53030 110006 259942 116174
db 364494 570342 373390 302782 454526 274462 450902
"""
# epis.set_output()
clip.std.Trim(56359, 58072).set_output()
# ------------ #

# ----err----- #
dn.check_num_frames(epis, clip)
# ------------ #
