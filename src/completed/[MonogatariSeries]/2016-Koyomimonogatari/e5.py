import dnfunc as dn

# -----in----- #
epname = dn.fname(__file__)
desc_h = 720

Chapter_5 = 8789
ED = 13521

epis = dn.source(f"./in/{epname}.mkv")
EDend = epis.num_frames - 15
# ------------ #

# ----mrgc---- #
ed = dn.oped(epis, name="ed1", offset=12, start=ED, end=EDend, desc_h=desc_h)

aaep = dn.aa(epis, desc_h=desc_h)

mrgc = aaep.std.Trim(0, ED - 1) + ed + aaep.std.Trim(EDend, epis.num_frames - 1)
# ------------ #

# ----mask---- #
mrgc = dn.rfs_image(mrgc, epis, f"{epname} 587", "[494 625]")
mrgc = dn.rfs_resc(
    mrgc,
    epis,
    desc_h=desc_h,
    mthr=50,
    maps="[53 146] [626 685] [767 835] [870 1015] [1049 1309] [1488 1596] [1626 1721] [1776 1877] [1925 1965] [2032 2180]",
)

hard = dn.hard(mrgc, mthr=20)
mrgc = dn.rfs_image(mrgc, hard, "e5 6521", "[6521 6574]")
# ------------ #

# ----filt---- #
"""
def filt_old(
    mrgc=mrgc,
    sm_thr=50,
    tr=48,
    pref=1,
    cs_mode=99,
    cs_val=0.55,
    db_thr=1.1,
    db_mode=3,
    db_det=64,
    db_grain=48,
    db_range=15,
    db_saveblack=2,
    rt_sigma=0.9,
    out_mode=0,
):
"""

F1 = dn.filt(mrgc)
F2 = dn.filt(mrgc, sm_thr=120, db_mode=2)
F3 = dn.filt(mrgc, sm_thr=30, db_thr=1)
F4 = dn.filt(mrgc, sm_thr=300, db_thr=6, db_mode=1, rt_sigma=4, db_det=128)

F1 = dn.rfs(F1, F2, f"[{Chapter_5} {ED-1}]")
F1 = dn.rfs(F1, F3, "[7594 7759] [8007 8146] [8465 8686]")
F1 = dn.rfs_image(F1, F4, "e5 11207", "[2585 2818] [2838 2942]")
# ------------ #

# ----out----- #
clip = dn.out(F1, epname)
clip.set_output()
# ------------ #

# ----save---- #
# dn.pw4(mrgc, 2, 1, epis, clip).set_output()
# epis.set_output()
# clip.std.Trim(2585, 2818).set_output()

# dn.rfs_resc(mrgc, epis, desc_h=desc_h, mthr=50, out_mask=True).set_output()
# ------------ #

# ----err----- #
dn.check_num_frames(epis, clip)
# ------------ #
