import dnfunc as dn

# ----in---- #
epname = dn.fname(__file__)
epis = dn.source(f"./in/{epname}.mp4")
# ---------- #

# ----ef---- #
epis, _crop = dn.crop(epis)
epis_back, epis, edgefixer = dn.edgefix(epis)
mrgc = epis
# ---------- #

# ----in---- #
F1 = dn.filt(mrgc, zone="op")
# ---------- #

# ---out---- #
clip = dn.out(F1, epname)
clip.set_output()
# ---------- #

# ---save--- #
# dn.pw4(mrgc, 2, 1, epis, clip).set_output()
# epis.set_output()

# ---err---- #
dn.check_num_frames(epis, clip)
# ---------- #
