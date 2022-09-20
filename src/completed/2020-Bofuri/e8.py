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

mrgc = aaep.std.Trim(0, OP - 1) + op + aaep.std.Trim(OPend, epis.num_frames - 1)
# ------------ #

# ----mask---- #
mrgc = dn.rfs_resc(mrgc, epis, mthr=168, maps="[32041 32433]")
mrgc = dn.rfs_resc(mrgc, epis, mthr=68, maps=f"[{ED} {EDend}]")
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
2: 65964
"""
# epis.set_output()
# dn.rfs_resc(epis=epis, mthr=68, out_mask=True).set_output()
# ------------ #

# ----err----- #
dn.check_num_frames(epis, clip)
# ------------ #
