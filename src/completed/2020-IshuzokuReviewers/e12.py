import dnfunc as dn

# -----in----- #
epname = dn.fname(__file__)

Part_B = dn.chapt(epname, "Part_B")
ED = dn.chapt(epname, "ED")
EDend = dn.chapt(epname, "EDend")

epis = dn.source(f"./in/{epname}.mp4")
# ------------ #

# ----mrgc---- #
aaep = dn.aa(epis)
ed = dn.oped(epis, name="ed_e12", offset=24, start=ED, end=EDend)

mrgc = aaep.std.Trim(0, ED - 1) + ed
# ------------ #

# ----mask---- #
mrgc = dn.rfs_dehalo(mrgc)

mrgc = dn.rfs(mrgc, epis, [(Part_B - 120, Part_B + 119)])  # true card

mrgc = dn.rfs_resc(mrgc, epis, mthr=70, maps=[(1991, 2116), (15909, 16040)])  # randon signs
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
# dn.rfs_resc(epis=epis, mthr=70, out_mask=True).set_output()
# ------------ #

# ----err----- #
dn.check_num_frames(epis, clip)
# ------------ #
