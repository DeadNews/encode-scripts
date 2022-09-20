import dnfunc as dn

# -----in----- #
epname = dn.fname(__file__)

epis = dn.source(f"./in/{epname}.mp4")
# ------------ #

# -----ef----- #
epis, epis_back, _ = dn.edgefix(epis)
epis = dn.rfs(epis, epis_back, (1206, 1244))
# ------------ #

# ----mrgc---- #
mrgc = dn.aa(epis)

# fox op
mrgc = dn.rfs_qtgmc(mrgc, mrgc, maps=(110, 672))
# ------------ #

# ----filt---- #
F1 = dn.filt(mrgc, zone="op")
# ------------ #

# ----out----- #
clip = dn.out(F1, epname)
clip.set_output()
# ------------ #

# ----save---- #
# epis.set_output()
# ------------ #

# ----err----- #
dn.check_num_frames(epis, clip)
# ------------ #
