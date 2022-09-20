import dnfunc as dn

# -----in----- #
epname = dn.fname(__file__)

OP = dn.chapt(epname, "OP")
OPend = dn.chapt(epname, "Part_C", "Next")
Next = dn.chapt(epname, "Next")
Nextend = dn.chapt(epname, "Promo_2")

epis = dn.source(f"./in/{epname}.mp4")
# ------------ #

# ----mrgc---- #
epis, epis_back, edgefixer = dn.edgefix(epis)

aaep = dn.aa(epis)
op = dn.oped(epis_back, name="op", offset=0, start=OP, end=OPend, edgefix=edgefixer)

mrgc = aaep.std.Trim(0, OP - 1) + op + aaep.std.Trim(OPend, epis.num_frames - 1)
# ------------ #

# ----mask---- #
maps = f"[{Next} {Nextend-1}]"  # next
maps += f" [34105 {Next-1}]"  # before next
maps += f" [29221 {OP-1}]"  # before ed(op)

mrgc = dn.rfs_resc(mrgc, epis, mthr=75, maps=maps)
# ------------ #

# ----filt---- #
F1 = dn.filt(mrgc)
F2 = dn.filt(mrgc, zone="black1")

F1 = dn.rfs(F1, F2, "[7159 10644] [11346 11850]")
# ------------ #

# ----out----- #
clip = dn.out(F1, epname)
clip.set_output()
# ------------ #

# ----save---- #
# dn.pw(mrgc, [3, 4], 'main', epis, clip).set_output()
# dn.pw(mrgc, [1, 2, 3, 4, 5, 6], 'main', epis, clip).set_output()
"""
aa 105022
db 35646 37086 114174  108893 67190 88790 42366  125694
-8-
177805
"""
# epis.set_output()
# clip.std.Trim(8885, 11851).set_output()
# clip.std.Trim(25563, 28602).set_output()
# dn.rfs_resc(mrgc, epis, mthr=75, out_mask=True).set_output()
# ------------ #

# ----err----- #
dn.check_num_frames(epis, clip)
# ------------ #
