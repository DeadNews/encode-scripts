import dnfunc as dn

# -----in----- #
epname = dn.fname(__file__)

OP = dn.chapt(epname, "OP")
OPend = dn.chapt(epname, "Part_A")
Part_B = dn.chapt(epname, "Part_B")
ED = dn.chapt(epname, "ED")
EDend = dn.chapt(epname, "Next")

epis = dn.source(f"./in/{epname}.mp4")
# ------------ #

# ----mrgc---- #
aaep = dn.aa(epis)
op = dn.oped(epis, name="op", offset=24, start=OP, end=OPend)

mrgc = aaep.std.Trim(0, OP - 1) + op + aaep.std.Trim(OPend, epis.num_frames - 1)
# ------------ #

# ----mask---- #
mrgc = dn.rfs(mrgc, epis, [(ED, EDend - 1)])  # ed

maps = [(EDend, epis.num_frames - 1)]  # next
maps += f" [{OPend} {OPend+189}]"  # title
maps += f" [{Part_B} {Part_B+71}]"  # title

mrgc = dn.rfs_resc(mrgc, epis, mthr=168, maps=maps, zone="resc")
# ------------ #

# ----filt---- #
F1 = dn.filt(mrgc)
F2 = dn.filt(mrgc, zone="ed")

F1 = dn.rfs(F1, F2, [(ED, EDend - 1)])
# ------------ #

# ----out----- #
clip = dn.out(F1, epname)
clip.set_output()
# ------------ #

# ----save---- #
# dn.pw(mrgc, None, None, epis, clip).set_output()
# dn.pw(mrgc, [1, 2, 3, 4, 5, 6], 'main', epis, clip).set_output()
# dn.pw(mrgc, [2, 3, 4, 6], 'main', epis, clip).set_output()
"""
aa(2) 3419 14695 19217 34063 40359
db(8) 122663 124142 125294
db(6) 126448 86680 197950 131794
"""
# epis.set_output()
# dn.rfs_resc(epis=epis, mthr=18, out_mask=True).set_output()
# dn.rfs_resc(epis=epis, mthr=168, out_db_mode=True, zone='resc').set_output()
# ------------ #

# ----err----- #
dn.check_num_frames(epis, clip)
# ------------ #
