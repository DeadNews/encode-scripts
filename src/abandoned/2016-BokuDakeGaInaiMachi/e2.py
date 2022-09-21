from sys import path

import dnfunc as dn

path.append(".")
from funcs import efix, get_maps

# -----in----- #
epname = dn.fname(__file__)

OP = dn.chapt(epname, "OP")
OPend = dn.chapt(epname, "Part_A")
Part_B = dn.chapt(epname, "Part_B")
ED = dn.chapt(epname, "ED")
EDend = dn.chapt(epname, "EDend", "Next")
Next = dn.chapt(epname, "Next")
EOF = dn.chapt(epname, "EOF")

epis = dn.source(f"./in/{epname}.mp4")
# ------------ #

# ----mrgc---- #
efaa = efix(epis, zone="crop")
aaep = dn.aa(epis)

mrgc = dn.rfs(efaa, aaep, maps=get_maps(epname))  # reverse fix 1

mrgc = dn.save_black(aaep, mrgc, threshold=0.08276)  # reverse fix 2
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
# dn.pw(mrgc, [3, 4, 6], 'main', epis, clip, ext_rip=rip).set_output()
"""
1:
2: 1828 914 970
2: 1258 420 56054 (!) 1546
2: 27412
6: 3778 168166 (!)
"""
# epis.set_output()
# dn.rfs_resc(epis=epis, out_mask=True).set_output()
# ------------ #

# ----err----- #
dn.check_num_frames(epis, clip)
# ------------ #
