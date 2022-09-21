import dnfunc as dn

# -----in----- #
epname = dn.fname(__file__)

CR = dn.chapt(epname, "Credit")
CRend = dn.chapt(epname, "Prologue", "OP")

epis = dn.source(f"./in/{epname}.mp4")
# ------------ #

# ----mask---- #
mrgc = epis
# ------------ #

# ----filt---- #
F1 = dn.filt(mrgc)
F2 = dn.filt(mrgc, zone="cr")

F1 = dn.rfs(F1, F2, [(CR, CRend - 1)])
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
# ------------ #

# ----err----- #
dn.check_num_frames(epis, clip)
# ------------ #
