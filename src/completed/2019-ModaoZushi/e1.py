from sys import path

import dnfunc as dn

path.append(".")
from funcs import epis_add, epis_crop

# -----in----- #
epname = dn.fname(__file__)

OP = dn.chapt(epname, "OP")
OPend = dn.chapt(epname, "Part_A")
Part_B = dn.chapt(epname, "Part_B")
ED = dn.chapt(epname, "ED")
EDend = dn.chapt(epname, "Next", "EOF")

epis = dn.source(f"./in/{epname}.mp4")
# ------------ #

# ----mrgc---- #
epis_back = epis
epis = dn.crop(epis)[0]
# ------------ #

# ----mask---- #
epis_epis = epis_crop(epis_back)

mrgc = dn.rfs_dehalo(epis_epis)
mrgc = dn.aa(mrgc)

mrgc = epis_add(mrgc)

mrgc_ed = dn.aa(epis, zone="ed")
mrgc_ed = dn.rfs_resc(mrgc_ed, epis, zone="resc_ed")

mrgc = dn.rfs(mrgc, epis, [(OP, OPend - 1)])
mrgc = dn.rfs(mrgc, mrgc_ed, [(ED, EDend - 1)])
# ------------ #

# ----filt---- #
F1 = dn.filt(mrgc)
F2 = dn.filt(mrgc, zone="op")
F3 = dn.filt(mrgc, zone="ed")

F1 = dn.rfs(F1, F2, [(OP, OPend - 1)])
F1 = dn.rfs(F1, F3, [(ED, EDend - 1)])
# ------------ #

# ----out----- #
clip = dn.out(F1, epname)
clip.set_output()
# ------------ #

# ----save---- #
# dn.pw(mrgc, None, None, epis, clip).set_output()
# dn.pw(mrgc, [2, 3, 4, 6], 'main', epis, clip).set_output()
"""
1: aa 67472 13418 12842 28223
2: 66234
"""
# epis.set_output()
# dn.rfs_resc(epis=epis, out_mask=True, zone='resc_ed').set_output()
# ------------ #

# ----err----- #
dn.check_num_frames(epis, clip)
# ------------ #
