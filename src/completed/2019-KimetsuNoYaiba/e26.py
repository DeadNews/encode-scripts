import dnfunc as dn

# -----in----- #
epname = dn.fname(__file__)

ED = dn.chapt(epname, "ED")
EDend = dn.chapt(epname, "EDend", "Next") - 24

jpn = dn.source(f"./in/{epname}.mp4")
ita = dn.source(f"./in/ita/{epname}.mp4")[24:]
epis = dn.average([jpn, ita])
# ------------ #

# ----mrgc---- #
aaep = dn.aa(epis)
mrgc = aaep
# ------------ #

# ----mask---- #
mrgc = dn.rfs_dehalo(mrgc)
mrgc = dn.rfs(mrgc, epis, f"[{ED} {EDend-1}]")  # custom ed
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
# dn.pw(mrgc, [2, 3, 4, 5], 'main', epis, clip).set_output()
"""
"""
# epis.set_output()
# dn.rfs_resc(epis=epis, mthr=148, out_mask=True).set_output()
# ------------ #

# ----err----- #
dn.check_num_frames(epis, clip)
# ------------ #
