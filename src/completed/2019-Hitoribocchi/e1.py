import dnfunc as dn

# -----in----- #
epname = dn.fname(__file__)

# op in the end
OP = dn.chapt(epname, "OP")
OPend = dn.chapt(epname, "OPend")

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

mrgc = dn.rfs_resc(mrgc, epis, mthr=17, maps=[(OPend, epis.num_frames - 1)])

_OPend = 1450
mrgc = dn.rfs_resc(mrgc, epis, mthr=17, maps=[(_OPend + 2, _OPend + 36)])
mrgc = dn.rfs_image(mrgc, aaep, f"title_{epname}", [(_OPend + 2, _OPend + 36)])

hard_epis = dn.hard(dn.qtgmc(epis), mthr=99)
mrgc = dn.rfs_image(mrgc, hard_epis, f"circles_{epname}", [(_OPend + 5, _OPend + 33)])

mrgc = dn.rfs_hard(mrgc, mrgc, mthr=20, maps=[(1936, 1994)])
mrgc = dn.rfs_resc(
    mrgc,
    epis,
    mthr=50,
    maps=[
        (30093, 30171),
        (30189, 30275),
        (30322, 30406),
        (30479, 30562),
        (30615, 30698),
        (30746, 30823),
        (31144, 31217),
        (31242, 31312),
        (31338, 31409),
        (31611, 31694),
        (31718, 31780),
        (31812, 31894),
    ],
)
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
17310
"""
# epis.set_output()
# dn.rfs_resc(epis=epis, mthr=65, out_mask=True).set_output()
# ------------ #

# ----err----- #
dn.check_num_frames(epis, clip)
# ------------ #
