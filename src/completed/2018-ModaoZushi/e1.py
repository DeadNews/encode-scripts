from sys import path

import dnfunc as dn

path.append(".")
from funcs import ef, ef_ed

# -----in----- #
epname = dn.fname(__file__)

OP = dn.chapt(epname, "OP")
OPend = dn.chapt(epname, "Part_A")
Part_B = dn.chapt(epname, "Part_B")
ED = dn.chapt(epname, "ED")
EDend = dn.chapt(epname, "EDend")

epis = dn.source(f"./in/{epname}.mp4")
# ------------ #

# ----mrgc---- #
epis = dn.crop(epis)[0]

epis_back = epis
epis = ef(epis)
epis_ed = ef_ed(epis)

epis = dn.rfs(epis, epis_ed, [(ED, EDend - 1)])
# ------------ #

# ----mask---- #
deha = dn.rfs_dehalo(epis)
mrgc = dn.aa(deha)

mrgc = dn.rfs(mrgc, deha, [(ED, EDend - 1)])
mrgc = dn.rfs(mrgc, epis_back, [(OP, OPend - 1)])
# ------------ #

# ----filt---- #
F1 = dn.filt(mrgc)
F2 = dn.filt(mrgc, zone="op")

F1 = dn.rfs(F1, F2, [(OP, OPend - 1)])
# ------------ #

# ----out----- #
clip = dn.out(F1, epname)
clip.set_output()
# ------------ #

# ----save---- #
# dn.pw(mrgc, None, None, epis_back, clip).set_output()
# dn.pw(mrgc, [2, 3, 4, 6], 'main', epis_back, clip).set_output()
"""
1: 6908 8348 20128 20560 21568 33365 36961 37105 38257 39697 47512
2: ef 96464 96432
2: 40256 41120 43136 66730 73922 74210 76514 79394 95024 13816 16696 21712 25456
6: 120772 123364 129412 200194 221770 222634 229546 238186 285076
"""
# epis.set_output()
# ------------ #

# ----err----- #
dn.check_num_frames(epis, clip)
# ------------ #
