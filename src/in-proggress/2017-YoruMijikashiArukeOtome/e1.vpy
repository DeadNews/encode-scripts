import dnfunc as dn

# -----in----- #
epname = dn.fname(__file__)

OP = dn.chapt(epname, "Opening")
ED = dn.chapt(epname, "Ending")
EOF = dn.chapt(epname, "EOF")

jpn = dn.source(f"./in/{epname}.mp4")
ger = dn.source(f"./in/ger/{epname}.mp4")[624:]
gbr = dn.source(f"./in/gbr/{epname}.mp4")[624:]

epis = dn.average([jpn, ger, jpn, gbr, jpn, ger, jpn, ger, jpn])
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
"""
1:
2: 27420 27708 28860
6: 86584
"""
# epis.set_output()
# ------------ #

# ----err----- #
dn.check_num_frames(epis, clip)
# ------------ #
