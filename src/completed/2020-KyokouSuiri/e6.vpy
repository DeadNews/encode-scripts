import dnfunc as dn

# -----in----- #
epname = dn.fname(__file__)

OP = dn.chapt(epname, "OP")
OPend = dn.chapt(epname, "Part_A")

epis = dn.source(f"./in/{epname}.mp4")
epis, epis_back, edgefixer = dn.edgefix(epis)
# ------------ #

# ----mrgc---- #
aaep = dn.aa(epis)
op = dn.oped(epis_back, name="op", offset=24, start=OP, end=OPend, edgefix=edgefixer)

mrgc = aaep.std.Trim(0, OP - 1) + op + aaep.std.Trim(OPend, epis.num_frames - 1)
# ------------ #

# ----mask---- #
mrgc = dn.rfs_dehalo(mrgc)
mrgc = dn.rfs_resc(mrgc, epis, mthr=148, zone="resc_fix", maps="[31736 32921] [34071 34238]")  # ed
# ------------ #

# ----filt---- #
F1 = dn.filt(mrgc)
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
# dn.rfs_resc(epis=epis, mthr=168, out_db_mode=True, zone='resc_fix').set_output()
# ------------ #

# ----err----- #
dn.check_num_frames(epis, clip)
# ------------ #
