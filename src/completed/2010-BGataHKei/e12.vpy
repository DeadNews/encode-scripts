import dnfunc as dn

# -----in----- #
epname = dn.fname(__file__)

Epilog = dn.chapt(epname, "Epilog")
EOF = dn.chapt(epname, "EOF")

epis = dn.source(f"./in/{epname}.mp4")
# ------------ #

# -----aa----- #
aaep = dn.aa(epis)
aaep = dn.aa(aaep, zone="eedi3")

mrgc = dn.rfs_dehalo(aaep)
mrgc = dn.rfs_dehalo(mrgc, zone="2nd")
# ------------ #

# ----mask---- #
eedi = dn.aa(epis, zone="eedi3")
mrgc = dn.rfs_resc(mrgc, eedi, maps=[(0, 148), (Epilog, EOF - 1)])
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
"""
# epis.set_output()
# ------------ #

# ----err----- #
dn.check_num_frames(epis, clip)
# ------------ #
