import dnfunc as dn

# -----in----- #
epname = dn.fname(__file__)

OP = dn.chapt(epname, "OP")
OPend = dn.chapt(epname, "Part_A")
ED = dn.chapt(epname, "ED")
EDend = dn.chapt(epname, "EDend") - 10

epis = dn.source(f"./in/{epname}.mp4")

# -----ef----- #
epis_back, epis_ef, edgefixer = dn.edgefix(epis)
#
# epis_ef_left  = epis.edgefixer.Continuity(top=2, bottom=3, left=3, right=7)
# epis_ef_right = epis.edgefixer.Continuity(top=2, bottom=3, left=6, right=4)
#
# epis_ef = dn.rfs(epis_ef, epis_ef_left,  "[]") #left fix
# epis_ef = dn.rfs(epis_ef, epis_ef_right, "[]") #right fix
#
epis = epis_ef
# ------------ #

# ----mrgc---- #
aaep = dn.aa(epis)
op = dn.oped(epis_back, name="op4", offset=24, start=OP, end=OPend, edgefix=edgefixer)
ed = dn.oped(epis_back, name="ed2", offset=24, start=ED, end=EDend, edgefix=edgefixer)

mrgc = (
    aaep.std.Trim(0, OP - 1)
    + op
    + aaep.std.Trim(OPend, ED - 1)
    + ed
    + aaep.std.Trim(EDend, epis.num_frames - 1)
)
# ------------ #

# ----mask---- #
# mrgc = dn.rfs_qtgmc(mrgc, aaep, k=1, maps="[]")

mrgc = dn.rfs_dehalo(mrgc)
# ------------ #

# ----filt---- #
F1 = dn.filt(mrgc)
# ------------ #

# ----out----- #
clip = dn.out(F1, epname)
clip.set_output()
# ------------ #

# ----save---- #
# dn.pw4(mrgc, 2, 1, epis_back, clip).set_output()
# dn.pw8(mrgc, 4, 7, 2, 5, 6, epis_back, clip, 0, zone='main').set_output()
"""
41250 47010
"""
# epis.set_output()
# clip.std.Trim(0, Part_A-1).set_output()
# ------------ #

# ----err----- #
dn.check_num_frames(epis, clip)
# ------------ #
