import dnfunc as dn

# -----in----- #
epname = dn.fname(__file__)

ED = dn.chapt(epname, "ED")
EDend = dn.chapt(epname, "EDend", "Next")

epis = dn.source(f"./in/{epname}.mp4")
epis, epis_back, edgefixer = dn.edgefix(epis)
# ------------ #

# ----mrgc---- #
aaep = dn.aa(epis)
ed = dn.oped(epis_back, name="ed", offset=24, start=ED, end=EDend, edgefix=edgefixer)

mrgc = aaep.std.Trim(0, ED - 1) + ed + aaep.std.Trim(EDend, epis.num_frames - 1)
# ------------ #

# ----mask---- #
mrgc = dn.rfs_dehalo(mrgc)
mrgc = dn.rfs_resc(mrgc, epis, mthr=168, zone="resc_fix", maps="[0 1980]")  # op
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
2: 1724
6: 116014 47620 98380 88474
"""
# epis_back.set_output()
# dn.rfs_resc(epis=epis, mthr=168, out_db_mode=True, zone='resc_fix').set_output()
# ------------ #

# ----err----- #
dn.check_num_frames(epis, clip)
# ------------ #
