import dnfunc as dn

# -----in----- #
epname = dn.fname(__file__)

OP = dn.chapt(epname, "OP")
OPend = dn.chapt(epname, "Part_A")
ED = dn.chapt(epname, "ED")
EDend = dn.chapt(epname, "EDend")

epis = dn.source(f"./in/{epname}.mp4")
# ------------ #

# ----mrgc---- #
aaep = dn.aa(epis)
op = dn.oped(epis, name="op", offset=0, start=OP, end=OPend)
ed = dn.oped(epis, name="ed", offset=0, start=ED, end=EDend)

mrgc = aaep.std.Trim(0, OP - 1) + op + aaep.std.Trim(OPend, ED - 1) + ed
# ------------ #

# ----mask---- #
mrgc = dn.rfs_resc(mrgc, epis, mthr=148, maps=[(OPend + 7, OPend + 58)])  # title
mrgc = dn.rfs_resc(mrgc, epis, mthr=148, maps=[(6911, 6939), (9874, 9902)])  # signs
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
6: 394 2986
"""
# epis.set_output()
# dn.rfs_resc(epis=epis, mthr=148, out_mask=True).set_output()
# ------------ #

# ----err----- #
dn.check_num_frames(epis, clip)
# ------------ #
