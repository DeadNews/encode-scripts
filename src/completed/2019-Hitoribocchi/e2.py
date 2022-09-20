import dnfunc as dn

# -----in----- #
epname = dn.fname(__file__)

OP = dn.chapt(epname, "OP")
OPend = dn.chapt(epname, "OPend")
ED = dn.chapt(epname, "ED")
EDend = dn.chapt(epname, "EDend")

epis = dn.source(f"./in/{epname}.mp4")
epis, epis_back, edgefixer = dn.edgefix(epis)
# ------------ #

# ----mrgc---- #
aaep = dn.aa(epis)
op = dn.oped(epis_back, name="op", offset=24, start=OP, end=OPend, edgefix=edgefixer)
ed = dn.oped(epis, name="ed1", offset=26, start=ED, end=EDend)

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

mrgc = dn.rfs_resc(mrgc, epis, mthr=17, maps=[(EDend, epis.num_frames - 1)])

mrgc = dn.rfs_resc(mrgc, epis, mthr=17, maps=[(OPend + 2, OPend + 36)])
mrgc = dn.rfs_image(mrgc, aaep, f"title_{epname}", [(OPend + 2, OPend + 36)])

hard_epis = dn.hard(dn.qtgmc(epis), mthr=99)
mrgc = dn.rfs_image(mrgc, hard_epis, f"circles_{epname}", [(OPend + 5, OPend + 33)])
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
103276
"""
# epis.set_output()
# dn.rfs_resc(epis=epis, mthr=65, out_mask=True).set_output()
# ------------ #

# ----err----- #
dn.check_num_frames(epis, clip)
# ------------ #
