import dnfunc as dn

# -----in----- #
epname = dn.fname(__file__)

OP = dn.chapt(epname, "OP")
OPend = dn.chapt(epname, "Part_A")
ED = dn.chapt(epname, "ED")
EDend = dn.chapt(epname, "EDend", "Next")

epis = dn.source(f"./in/{epname}.mp4")
# ------------ #

# ----mrgc---- #
aaep = dn.aa(epis)
# mrgc = aaep
op = dn.oped(epis, name="op", offset=24, start=OP, end=OPend)
ed = dn.oped(epis, name="ed", offset=24, start=ED, end=EDend)

mrgc = (
    aaep.std.Trim(0, OP - 1)
    + op
    + aaep.std.Trim(OPend, ED - 1)
    + ed
    + aaep.std.Trim(EDend, epis.num_frames - 1)
)
# ------------ #

# ----mask---- #
mrgc = dn.rfs_resc(mrgc, epis, mthr=58)
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
# dn.pw(mrgc, None, None, epis, clip).set_output()
# dn.pw(mrgc, [2, 3, 4, 6], 'main', epis, clip).set_output()
# aa_dn.pw(epis, zones=['bilinear', 'bicubic_1_0']).set_output()
"""
1: 10409 11745 16966 24608
2: 20818 23490 33932 49216  21692 7124 8276 49504 50080
3: 35235
6:
"""
# epis.set_output()
# dn.rfs_resc(epis=epis, mthr=58, out_mask=True).set_output()
# ------------ #

# ----err----- #
dn.check_num_frames(epis, clip)
# ------------ #
