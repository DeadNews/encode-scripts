import dnfunc as dn

# -----in----- #
epname = dn.fname(__file__)

jpn = dn.source(f"./in/{epname}.mp4")
ita = dn.source(f"./in/ita/{epname}.mp4")

epis = dn.average([jpn, ita, jpn, ita, jpn, ita, jpn, jpn])
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
# dn.pw(mrgc, None, None, epis, clip).set_output()
# dn.pw(mrgc, [2, 3, 4, 6], 'main', epis, clip).set_output()
# dn.pw(mrgc, [2, 3, 4, 6], 'main', jpn, clip).set_output()
"""
2: 248764 57725 189986
2: aa 70500 38900
2: 100384 100672 22092 100962
6: 74632 569962 173176 302020 302890
"""
# epis.set_output()
# ------------ #

# ----err----- #
dn.check_num_frames(epis, clip)
# ------------ #
