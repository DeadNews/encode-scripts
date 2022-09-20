import dnfunc as dn
from vapoursynth import core

# -----in----- #
epname = dn.fname(__file__)

ED = dn.chapt(epname, "ED")
EDend = dn.chapt(epname, "EDend")

epis = dn.source(f"./in/{epname}.mp4")
# ------------ #

# ----mrgc---- #
aaep = dn.aa(epis, epname)
mrgc = dn.rfs_dehalo(aaep)
# ------------ #


def resc_filt(mask):
    mask2 = mask.std.Binarize(threshold=100)
    return core.std.Expr([mask, mask2], ["x y max"])


# ----mask---- #
mrgc = dn.rfs_resc(mrgc, epis, mthr=17, zone="resc", filt=resc_filt)
mrgc = dn.rfs(mrgc, epis, f"[{ED} {EDend-1}] [3810 3983] [0 503]")  # ed; title; avant
# ------------ #

# ----filt---- #
F1 = dn.filt(mrgc)
F2 = dn.filt(mrgc, zone="noise")
F3 = dn.filt(mrgc, zone="limb")
F4 = dn.filt(mrgc, zone="saveblack")
F5 = dn.filt(mrgc, zone="soft1")
F6 = dn.filt(mrgc, zone="soft2")

F1 = dn.rfs(F1, F2, "[34818 35070] [54240 54450] [55626 56562]")
F1 = dn.rfs(F1, F3, "[117772 118023] [39551 39610]")
F1 = dn.rfs(F1, F4, f"[{ED} {EDend-1}]")
F1 = dn.rfs(F1, F5, "[77156 77227] [30890 30907]  [21553 21798] [33449 33580]")
F1 = dn.rfs(
    F1,
    F6,
    "[76451 77155] [30800 30889] [35390 35461] [37386 37574] [60557 60629] [61393 61440] [105791 105854]  [60484 60629] [82435 82515] [38041 38172] [69440 69497] [92662 92749] [95017 95112]",
)
# ------------ #

# ----out----- #
clip = dn.out(F1, epname)
clip.set_output()
# ------------ #

# ----save---- #
# dn.pw(mrgc, None, None, epis, clip).set_output()
# dn.pw(mrgc, [1, 2, 3, 4, 6], 'main', epis, clip).set_output()
# dn.pw(mrgc, [1, 2, 3, 4, 6], 'soft1', epis, clip, 'main').set_output()
"""
aa2  3120 3056 14746 30726 44730 118870 118954 239966 120310 240252 24960 54810 56826 57402
f7   421671 839600 551269 540027 539453 539453 540461 418934
resc 1551 1560 59435 59477 7373 119983 15363 22365
"""
# epis.set_output()
# clip.std.Trim(59445, 59445+4000).set_output()
# clip.std.Trim(59445, 59445+2000).set_output()
# clip.std.Trim(9415, 10799).set_output()
# dn.rfs_resc(epis=epis, mthr=17, out_db_mode=True, zone='resc', filt=resc_filt).set_output()
# ------------ #

# ----err----- #
dn.check_num_frames(epis, clip)
# ------------ #
