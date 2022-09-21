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
aaep = dn.aa(epis, zone="868p")
op = dn.oped(epis, name="op1", offset=0, start=OP, end=OPend)

mrgc = aaep.std.Trim(0, OP - 1) + op + aaep.std.Trim(OPend, epis.num_frames - 1)
# ------------ #

# ----mask---- #
mrgc = dn.rfs_resc(mrgc, epis, mthr=18, zone="868p", maps=f"[0 {OP-1}] [{OPend} {ED-1}]")

mrgc = dn.rfs_dehalo(mrgc)

mrgc = dn.rfs(mrgc, epis, f"[{ED} {EDend-1}]")  # ed1
# ------------ #-1

# ----filt---- #
F1 = dn.filt(mrgc)
F2 = dn.filt(mrgc, zone="edop")

F1 = dn.rfs(F1, F2, f"[{OP} {OPend-1}] [{ED} {EDend-1}]")
# ------------ #

# ----out----- #
clip = dn.out(F1, epname)
clip.set_output()
# ------------ #

# ----save---- #
# dn.pw(mrgc, None, None, epis, clip).set_output()
# dn.pw(mrgc, [1, 2, 3, 4, 6], 'main', epis, clip).set_output()
"""
2: 19698 28050 31218
7: 149567 180892 195851 216837 204153 216249
"""
# epis.set_output()
# dn.rfs_resc(epis=epis, mthr=18, out_db_mode=True, zone='868p').set_output()
# ------------ #

# ----err----- #
dn.check_num_frames(epis, clip)
# ------------ #
