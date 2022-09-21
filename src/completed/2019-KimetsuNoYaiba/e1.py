from sys import path

import dnfunc as dn

path.append(".")
from funcs import ext_nc

# -----in----- #
epname = dn.fname(__file__)

OP = dn.chapt(epname, "OP")
OPend = dn.chapt(epname, "ED")
ED = dn.chapt(epname, "ED")
EDend = dn.chapt(epname, "EDend", "Next") - 24

jpn = dn.source(f"./in/{epname}.mp4")
ita = dn.source(f"./in/ita/{epname}.mp4")[24:]
epis = dn.average([jpn, ita])
# ------------ #

# ----mrgc---- #
aaep = dn.aa(epis)
op = dn.oped(epis, name="op1", offset=0, start=OP, end=OPend, ext_nc=ext_nc("op1"))

mrgc = aaep.std.Trim(0, OP - 1) + op + aaep.std.Trim(OPend, epis.num_frames - 1)
# ------------ #

# ----mask---- #
mrgc = dn.rfs_dehalo(mrgc)
mrgc = dn.rfs_hard(mrgc, mrgc, mthr=20, yuv=True, maps=f"[{OP+293} {OP+397}]")
mrgc = dn.rfs(mrgc, epis, f"[{ED} {EDend-1}]")  # custom ed
# ------------ #

# ----filt---- #
F1 = dn.filt(mrgc)
F2 = dn.filt(mrgc, zone="noise_1")
F4 = dn.filt(mrgc, zone="noise_op")
F5 = dn.filt(mrgc, zone="grain_op")
F6 = dn.filt(mrgc, zone="main")
F7 = dn.filt(mrgc, zone="noise_2")

F1 = dn.rfs(F1, F2, "[12451 30449]")  # film grain
F1 = dn.rfs(F1, F4, f"[{OP} {OP+282}]")
F1 = dn.rfs(F1, F5, f"[{OP+1169} {OP+1398}]")
# back
F1 = dn.rfs(F1, F6, "[13898 13929] [12605 12700] [13709 13795] [15135 15311]")
# back2
F1 = dn.rfs(
    F1, F7, "[17127 17203] [12547 12604] [12857 12976] [13091 13222] [13796 13839] [16143 16250]"
)
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
2: 3776 62390 64460 63948 6008 4641 17970 64044 26346 27806!! 34384 38128 42448 13386 11078 37804
6: 121672 6010 18028 102022 192472! 4066  151534 191848 83422
"""
# epis.set_output()
# clip.std.Trim(15570, 17970).set_output() #test
# clip.std.Trim(13898, 13929).set_output() #fix1
# clip.std.Trim(17127, 17229-1).set_output() #fix2
# dn.rfs_resc(epis=epis, mthr=100, out_mask=True).set_output()
# ------------ #

# ----err----- #
dn.check_num_frames(epis, clip)
# ------------ #
