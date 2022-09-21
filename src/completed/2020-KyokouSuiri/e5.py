import dnfunc as dn

# -----in----- #
epname = dn.fname(__file__)

OP = dn.chapt(epname, "OP")
OPend = dn.chapt(epname, "Part_A")
ED = dn.chapt(epname, "ED")
EDend = dn.chapt(epname, "EDend", "Next")

epis = dn.source(f"./in/{epname}.mp4")
epis, epis_back, edgefixer = dn.edgefix(epis)
# ------------ #

# ----mrgc---- #
aaep = dn.aa(epis)
op = dn.oped(epis_back, name="op", offset=24, start=OP, end=OPend, edgefix=edgefixer)
ed = dn.oped(epis_back, name="ed", offset=24, start=ED, end=EDend, edgefix=edgefixer)

mrgc = (
    aaep.std.Trim(0, OP - 1)
    + op
    + aaep.std.Trim(OPend, ED - 1)
    + ed
    + aaep.std.Trim(EDend, epis.num_frames - 1)
)
# ------------ #

# ----mask---- #
mrgc = dn.rfs_dehalo(mrgc)
# ------------ #

# ----filt---- #
F1 = dn.filt(mrgc)
F2 = dn.filt(mrgc, zone="noise")

F1 = dn.rfs(F1, F2, "[27719 28030]")
# ------------ #

# ----out----- #
clip = dn.out(F1, epname)
clip.set_output()
# ------------ #

# ----save---- #
# dn.pw(mrgc, None, None, epis_back, clip).set_output()
# dn.pw(mrgc, [2, 3, 4, 6], 'main', epis_back, clip).set_output()
"""
"""
# epis_back.set_output()
# clip.std.Trim(27719,28030).set_output()
# dn.rfs_resc(epis=epis, mthr=168, out_db_mode=True, zone='resc_fix').set_output()
# ------------ #

# ----err----- #
dn.check_num_frames(epis, clip)
# ------------ #
