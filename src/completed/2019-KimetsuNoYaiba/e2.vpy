from sys import path

import dnfunc as dn

path.append(".")
from funcs import ext_nc

# -----in----- #
epname = dn.fname(__file__)

OP = dn.chapt(epname, "OP")
OPend = dn.chapt(epname, "Part_A")
ED = dn.chapt(epname, "ED")
EDend = dn.chapt(epname, "EDend", "Next")

jpn = dn.source(f"./in/{epname}.mp4")
ita = dn.source(f"./in/ita/{epname}.mp4")[24:]
epis = dn.average([jpn, ita])
# ------------ #

# ----mrgc---- #
aaep = dn.aa(epis)
op = dn.oped(epis, name="op1", offset=0, start=OP, end=OPend, ext_nc=ext_nc("op1"))
ed = dn.oped(epis, name="ed1", offset=0, start=ED, end=EDend, ext_nc=ext_nc("ed1"))

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
mrgc = dn.rfs_hard(mrgc, mrgc, mthr=20, yuv=True, maps=f"[{OP+293} {OP+397}]")
# ------------ #

# ----filt---- #
F1 = dn.filt(mrgc)
F2 = dn.filt(mrgc, zone="noise_1")
F3 = dn.filt(mrgc, zone="noise_4")
F4 = dn.filt(mrgc, zone="noise_op")
F5 = dn.filt(mrgc, zone="grain_op")

F1 = dn.rfs(F1, F2, f"[{ED} {ED+399}]")
F1 = dn.rfs(F1, F3, f"[{EDend} {epis.num_frames-1}]")
F1 = dn.rfs(F1, F4, f"[{OP} {OP+282}]")
F1 = dn.rfs(F1, F5, f"[{OP+1169} {OP+1398}]")
# ------------ #

# ----out----- #
clip = dn.out(F1, epname)
clip.set_output()
# ------------ #

# ----save---- #
# dn.pw(mrgc, None, None, epis, clip).set_output()
# dn.pw(mrgc, [2, 3, 4, 6], 'main', epis, clip).set_output()
# dn.pw(mrgc, [2, 3, 4, 5], 'main', epis, clip).set_output()
"""
2: 19138 26708 3438 5720
"""
# epis.set_output()
# dn.rfs_resc(epis=epis, mthr=148, out_mask=True).set_output()
# ------------ #

# ----err----- #
dn.check_num_frames(epis, clip)
# ------------ #
