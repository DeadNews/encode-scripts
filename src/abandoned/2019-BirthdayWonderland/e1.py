import dnfunc as dn

# -----in----- #
epname = dn.fname(__file__)

ita = dn.source(f"./in/ita/{epname}.mp4")
gbr = dn.source(f"./in/gbr/{epname}.mp4")[6:]
spa = dn.source(f"./in/spa/{epname}.mp4")[96:]

epis = dn.average([ita, gbr, ita, spa, ita, gbr, ita, gbr, ita, ita])
# ------------ #

# ----mrgc---- #
mrgc = epis
# ------------ #

# ----filt---- #
F1 = dn.filt(mrgc)
# ------------ #

# ----out----- #
clip = dn.out(F1, epname)
clip.set_output()
# ------------ #

# ----save---- #
# dn.pw(mrgc, None, None, ita, clip).set_output()
# dn.pw(mrgc, [2, 3, 4, 6], 'main', ita, clip).set_output()
"""
1:
2: 51796 164476 266488 254316 267064 232986 234138 244822 245974
6: 801196
"""
# epis.set_output()
# ------------ #

# ----err----- #
dn.check_num_frames(epis, clip)
# ------------ #
