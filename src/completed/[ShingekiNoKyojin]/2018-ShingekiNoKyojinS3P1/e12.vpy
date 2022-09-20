from sys import path

import dnfunc as dn

path.append(".")
from funcs import ext_nc, get_maps

# -----in----- #
epname = dn.fname(__file__)

OP = dn.chapt(epname, "OP")
OPend = dn.chapt(epname, "Part_A")
Part_B = dn.chapt(epname, "Part_B")
ED1 = dn.chapt(epname, "ED1")
Next = dn.chapt(epname, "Next")
ED2 = dn.chapt(epname, "ED2")
EOF = dn.chapt(epname, "EOF")

jpn = dn.source(f"./in/{epname}.mp4")
usa = dn.source(f"./in/usa/{epname}.mp4")[24:]
# ------------ #

# ----mrgc---- #
epis = dn.average([jpn, usa, jpn, jpn, jpn, jpn, jpn, jpn, jpn])

rfs_map = [
    (OP, OPend - 1),
    (OPend, OPend + 120),
    (Part_B - 120, Part_B),
    (ED1, Next - 1),
    (ED2, EOF - 1),
]

if maps := get_maps(epname):
    rfs_map.extend(maps)

epis = dn.rfs(epis, jpn, rfs_map)  # jpn_titles
# ------------ #

# ----mrgc---- #
aaep = dn.aa(epis)

op = dn.oped(epis, name="op", offset=0, start=OP, end=OPend, ext_nc=ext_nc("op"))

mrgc = aaep.std.Trim(0, OP - 1) + op + aaep.std.Trim(OPend, EOF - 1)
# ------------ #

# ----mask---- #
mrgc = dn.rfs_resc(mrgc, epis)  # all
# ------------ #

# ----filt---- #
F1 = dn.filt(mrgc)
F2 = dn.filt(mrgc, zone="op")
F4 = dn.filt(mrgc, zone="ti")

F1 = dn.rfs(F1, F2, (OP, OPend - 1))
F1 = dn.rfs(F1, F4, (OPend, OPend + 120))
# ------------ #

# ----out----- #
clip = dn.out(F1, epname)
clip.set_output()
# ------------ #

# ----save---- #
# dn.pw(mrgc, None, None, epis, clip).set_output()
# dn.pw(mrgc, [2, 3, 4, 6], 'main', epis, clip).set_output()
"""
2: 33048 60556
"""
# epis.set_output()
# dn.rfs_resc(epis=epis, out_mask=True).set_output()
# ------------ #

# ----err----- #
dn.check_num_frames(epis, clip)
# ------------ #
