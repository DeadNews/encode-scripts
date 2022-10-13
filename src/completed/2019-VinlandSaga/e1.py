import dnfunc as dn

# -----in----- #
epname = dn.fname(__file__)

OP = dn.chapt(epname, "OP")
OPend = dn.chapt(epname, "Part_A") - 72
ED = dn.chapt(epname, "ED")
EDend = dn.chapt(epname, "End")

epis = dn.source(f"./in/{epname}.mp4")
# ------------ #

# ----mrgc---- #
aaep = dn.aa(epis)
op = dn.oped(epis, name="op1", offset=0, start=OP, end=OPend)

mrgc = aaep.std.Trim(0, OP - 1) + op + aaep.std.Trim(OPend, epis.num_frames - 1)
# ------------ #

# ----mask---- #
mrgc = dn.rfs_dehalo(mrgc)

mrgc = dn.rfs(mrgc, epis, [(ED, EDend - 1)])  # ed1

maps = dn.load_map(epname, "signs")
mrgc = dn.rfs_resc(mrgc, epis, mthr=68, maps=maps)

mrgc = dn.rfs_qtgmc(mrgc, mrgc, k=0.6, maps=[(24233, 24539)])
# ------------ #

# ----filt---- #
F1 = dn.filt(mrgc)
F2 = dn.filt(mrgc, zone="edop")
F3 = dn.filt(mrgc, zone="soft")

F1 = dn.rfs(F1, F2, [(OP, OPend - 1), (ED, EDend - 1)])
F1 = dn.rfs(F1, F3, [(869, 5070)])
# ------------ #

# ----out----- #
clip = dn.out(F1, epname)
clip.set_output()
# ------------ #

# ----save---- #
# dn.pw(mrgc, None, None, epis, clip).set_output()
# dn.pw(mrgc, [1, 2, 3, 4, 6], 'main', epis, clip).set_output()
"""
2: 60022
7: 164708 24604 100098 101106 28635 250710 7803
"""
# epis.set_output()
# dn.rfs_resc(epis=epis, mthr=68, out_mask=True).set_output()
# clip.std.Trim(23764, 24610).set_output()
# clip.std.Trim(15883, 16099).set_output()
# ------------ #

# ----err----- #
dn.check_num_frames(epis, clip)
# ------------ #
