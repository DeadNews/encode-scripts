from sys import path

import dnfunc as dn

path.append(".")
from funcs import edname, ext_nc, get_maps, opname

# -----in----- #
epname = dn.fname(__file__)
opname = opname(epname)
edname = edname(epname)

OP = dn.chapt(epname, "OP")
OPend = dn.chapt(epname, "Part_A")
Part_B = dn.chapt(epname, "Part_B")
ED = dn.chapt(epname, "ED")
EDend = dn.chapt(epname, "EDend", "Next")
Next = dn.chapt(epname, "Next")

jpn = dn.source(f"./in/{epname}.mp4")
ita = dn.source(f"./in/ita/{epname}.mp4")[24:]
usa = dn.source(f"./in/usa/{epname}.mp4")[24:]
# ------------ #

# ----mrgc---- #
epis = dn.average([jpn, ita, usa, ita, jpn, ita, jpn, jpn])

rfs_map = [
    (OP, OPend - 1),
    (ED, EDend - 1),
    (OPend, OPend + 120),
    (Part_B - 120, Part_B + 119),
    (Next, epis.num_frames - 1),
]

if maps := get_maps(epname):
    rfs_map.extend(maps)

epis = dn.rfs(epis, jpn, rfs_map)  # jpn_titles
# ------------ #

# ----mrgc---- #
aaep = dn.aa(epis)

op = dn.oped(epis, name=opname, offset=0, start=OP, end=OPend, ext_nc=ext_nc(opname))
ed = dn.oped(epis, name=edname, offset=0, start=ED, end=EDend, ext_nc=ext_nc(edname))

mrgc = (
    aaep.std.Trim(0, OP - 1)
    + op
    + aaep.std.Trim(OPend, ED - 1)
    + ed
    + aaep.std.Trim(EDend, epis.num_frames - 1)
)
# ------------ #

# ----mask---- #
mrgc = dn.rfs_resc(mrgc, epis)  # all
# ------------ #

# ----filt---- #
F1 = dn.filt(mrgc)
F2 = dn.filt(mrgc, zone="op")
F3 = dn.filt(mrgc, zone="ed")

F1 = dn.rfs(F1, F2, (OP, OPend - 1))
F1 = dn.rfs(F1, F3, (ED, EDend - 1))
# ------------ #

# ----out----- #
clip = dn.out(F1, epname)
clip.set_output()
# ------------ #

# ----save---- #
# dn.pw(mrgc, None, None, epis, clip).set_output()
# dn.pw(mrgc, [2, 3, 4, 6], 'main', epis, clip).set_output()
"""
2: 13818 16126 16702 60114! 63300 15272 61266! 17522
2: aa 1496! 18430! 8336 9488 36254! 35081!
6: 180346 183802
"""
# epis.set_output()
# clip.std.Trim(15570, 17970).set_output() #test
# dn.rfs_resc(epis=epis, mthr=65, out_mask=True).set_output()
# ------------ #

# ----err----- #
dn.check_num_frames(epis, clip)
# ------------ #
