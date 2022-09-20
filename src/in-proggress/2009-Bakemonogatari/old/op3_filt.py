from pathlib import Path

import dnfunc as dn

# -----in----- #
epname = "op3"
desc_h = 720

epis = dn.source(f"./in/{epname}.mp4")
# ------------ #

# -----aa----- #
if Path(f"./temp/{epname}_aa_lossless.mp4").is_file():
    aaep = dn.source(f"./temp/{epname}_aa_lossless.mp4")
else:
    aaep = dn.aa(epis, desc_h=desc_h)

mrgc = aaep
# ------------ #

# ----mask---- #
mrgc = dn.rfs_qtgmc(mrgc, aaep, k=0.77, maps="[12 233] [1179 1420] [1742 1772] [1795 1913]")
# ------------ #

# ----out----- #
clip = mrgc
clip.set_output()
# ------------ #

# ----save---- #
# dn.pw4(mrgc, 2, 1, epis, clip).set_output()
# epis.set_output()
# clip.std.Trim(0, 3000).set_output()
# ------------ #

# ----err----- #
dn.check_num_frames(epis, clip)
# ------------ #
