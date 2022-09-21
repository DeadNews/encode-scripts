import dnfunc as dn
from vapoursynth import core

# -----in----- #
epname = dn.fname(__file__)

epis = dn.source(f"./in/{epname}.mp4")
# ------------ #

# ----mrgc---- #
mrgc = dn.aa(epis, epname)
# ------------ #


def resc_filt(mask):
    mask2 = mask.std.Binarize(threshold=100)
    return core.std.Expr([mask, mask2], ["x y max"])


# ----mask---- #
mrgc = dn.rfs_resc(mrgc, epis, mthr=50, filt=resc_filt)
# ------------ #

# ----filt---- #
F1 = dn.filt(mrgc)
# ------------ #

# ----out----- #
clip = dn.out(F1, epname, fpsnum=30000, fpsden=1001)
clip.set_output()
# ------------ #

# ----save---- #
# dn.pw(mrgc, None, None, epis, clip).set_output()
# dn.pw(mrgc, [1, 2, 3, 4, 6], 'main', epis, clip).set_output()
"""
"""
# epis.set_output()
# dn.rfs_resc(epis=epis, mthr=50, out_db_mode=True, filt=resc_filt).set_output()
# ------------ #

# ----err----- #
dn.check_num_frames(epis, clip)
# ------------ #
