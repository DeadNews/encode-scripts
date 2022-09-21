import dnfunc as dn

# -----in----- #
epname = dn.fname(__file__)

ED = dn.chapt(epname, "ED")
ART = dn.chapt(epname, "EOF") - 132
EOF = dn.chapt(epname, "EOF")

epis = dn.source(f"./in/{epname}.mp4")
# ------------ #

# ----mask---- #
mrgc = dn.aa(epis)

mrgc = dn.rfs_resc(mrgc, epis, maps=(0, ED - 1))
mrgc = dn.rfs_resc(mrgc, epis, maps=(ED, ART - 1), zone="resc2")
mrgc = dn.rfs(mrgc, epis, maps=(ART, EOF - 1))
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
# dn.rfs_resc(epis=epis, out_mask=True).set_output()
# ------------ #

# ----err----- #
dn.check_num_frames(epis, clip)
# ------------ #
