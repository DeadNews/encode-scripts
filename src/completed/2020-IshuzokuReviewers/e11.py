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
op = dn.oped(epis, name="op", offset=0, start=OP, end=OPend)

mrgc = aaep.std.Trim(0, OP - 1) + op + aaep.std.Trim(OPend, epis.num_frames - 1)
# ------------ #

# ----mask---- #
mrgc = dn.rfs_dehalo(mrgc)

mrgc = dn.rfs(mrgc, epis, f"[{ED} {EDend-1}]")  # ed
mrgc = dn.rfs(mrgc, epis, f"[{epis.num_frames-168} {epis.num_frames-1}]")  # title
mrgc = dn.rfs(mrgc, epis, f"[{Part_B-120} {Part_B+119}]")  # true card

mrgc = dn.rfs_resc(
    mrgc, epis, mthr=50, maps=f"[{OP+1486} {OP+1508}] [{OP+2084} {OP+2159}]"
)  # op cenc
mrgc = dn.rfs_hard(mrgc, mrgc, mthr=99, maps=f"[{OP+2101} {OP+2159}]")  # op_end
# ------------ #

# ----filt---- #
F1 = dn.filt(mrgc)
F2 = dn.filt(mrgc, zone="oped")
F3 = dn.filt(mrgc, zone="ed_lite")

F1 = dn.rfs(F1, F2, f"[{OP} {OPend-1}] [{ED} {EDend-1}]")
F1 = dn.rfs(F1, F3, f"[{ED+1066} {ED+1469}]")
# ------------ #

# ----out----- #
clip = dn.out(F1, epname)
clip.set_output()
# ------------ #

# ----save---- #
# dn.pw(mrgc, None, None, epis, clip).set_output()
# dn.pw(mrgc, [2, 3, 4, 6], 'main', epis, clip).set_output()
"""
"""
# epis.set_output()
# dn.rfs_resc(epis=epis, mthr=70, out_mask=True).set_output()
# ------------ #

# ----err----- #
dn.check_num_frames(epis, clip)
# ------------ #