import dnfunc as dn

# -----in----- #
epname = dn.fname(__file__)

usa = dn.source(f"./in/{epname}.mp4")
ita = dn.source(f"./in/ita/{epname}.mp4")
ita = usa[:97] + ita

epis = dn.average([usa, ita, usa, usa, usa, usa])
# ------------ #

# ----mrgc---- #
epis = dn.crop(epis)[0]

epis, epis_back, _ = dn.edgefix(epis)
# ------------ #

# ----mask---- #
mrgc = dn.rfs_dehalo(epis)
# ------------ #

# ----filt---- #
F1 = dn.filt(mrgc)
# ------------ #

# ----out----- #
clip = dn.out(F1, epname)
clip.set_output()
# ------------ #

# ----save---- #
# dn.pw(mrgc, None, None, epis_back, clip).set_output()
# dn.pw(mrgc, [2, 3, 4, 6], 'main', epis_back, clip).set_output()
"""
2: 53722 107446 225450 137470
6: galo 412414
6: db 322342 655030 530344
"""
# epis.set_output()
# ------------ #

# ----err----- #
dn.check_num_frames(epis, clip)
# ------------ #
