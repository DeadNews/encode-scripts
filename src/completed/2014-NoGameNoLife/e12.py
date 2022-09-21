import dnfunc as dn

# -----in----- #
epname = dn.fname(__file__)

Promo_1 = dn.chapt(epname, "Promo_1")
Promo_2 = dn.chapt(epname, "Promo_2")

epis = dn.source(f"./in/{epname}.mp4")
# ------------ #

# ----mrgc---- #
epis, epis_back, edgefixer = dn.edgefix(epis)

aaep = dn.aa(epis)
mrgc = aaep
# ------------ #

# ----mask---- #
mrgc = dn.rfs_qtgmc(mrgc, mrgc, k=1, maps="[30300 30368]")

maps = f"[{Promo_2-74} {Promo_2-1}]"  # logo
maps += f" [0 331]"  # titles on epis
maps += f" [1450 1895]"  # titles on epis
maps += f" [30747 32418]"  # titles on epis

mrgc = dn.rfs_resc(mrgc, epis, mthr=75, maps=maps)
# ------------ #

# ----filt---- #
F1 = dn.filt(mrgc)
# ------------ #

# ----out----- #
clip = dn.out(F1, epname)
clip.set_output()
# ------------ #

# ----save---- #
# dn.pw(mrgc, [3, 4], 'main', epis, clip).set_output()
# dn.pw(mrgc, [1, 2, 3, 4, 5, 6], 'main', epis, clip).set_output()
"""
"""
# epis.set_output()
# dn.rfs_resc(mrgc, epis, mthr=75, out_mask=True).set_output()
# ------------ #

# ----err----- #
dn.check_num_frames(epis, clip)
# ------------ #
