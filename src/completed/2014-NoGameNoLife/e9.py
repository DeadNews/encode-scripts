import dnfunc as dn

# -----in----- #
epname = dn.fname(__file__)

OPend = dn.chapt(epname, "Promo_1", "Part_A")
ED = dn.chapt(epname, "ED")
EDend = dn.chapt(epname, "Part_C", "Next")
Next = dn.chapt(epname, "Next")
Nextend = dn.chapt(epname, "Promo_2")

epis = dn.source(f"./in/{epname}.mp4")
# ------------ #

# ----mrgc---- #
epis, epis_back, edgefixer = dn.edgefix(epis)

aaep = dn.aa(epis)
ed = dn.oped(epis_back, name="ed", offset=0, start=ED, end=EDend)

mrgc = aaep.std.Trim(0, ED - 1) + ed + aaep.std.Trim(EDend, epis.num_frames - 1)
# ------------ #

# ----mask---- #
maps = [(Next, Nextend - 1)]  # next
maps += f" [0 {OPend-1}]"  # op on epis

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
