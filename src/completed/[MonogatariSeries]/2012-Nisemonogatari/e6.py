import dnfunc as dn

# -----in----- #
epname = dn.fname(__file__)
desc_h = 720

ED = 32608
EDend = 34765

epis = dn.source(f"./in/{epname}.mkv")
# ------------ #

# ----mrgc---- #
ed = dn.oped(epis, name="ed3", offset=12, start=ED, end=EDend, desc_h=desc_h)

aaep = dn.aa(epis, desc_h=desc_h)

mrgc = aaep.std.Trim(0, ED - 1) + ed + aaep.std.Trim(EDend, epis.num_frames - 1)
# ------------ #

# ----mask---- #
mrgc = dn.rfs_qtgmc(mrgc, aaep, k=0.77, maps="[4968 5108] [10638 10716] [23128 23270]")

hard = dn.hard(aaep, mthr=90)
mrgc = dn.rfs_image(mrgc, hard, "e6 3655", "[3479 3655]")

mrgc = dn.rfs_hard(
    mrgc,
    mrgc,
    mthr=99,
    maps="[10501 10522] [10717 10794] [11450 11538] [11671 11805] [14398 14446] [18358 18501] [21365 21427] [23271 23373] [20740 20823]",
)
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
F2 = dn.filt(mrgc, db_mode=1)
F3 = dn.filt(mrgc, db_mode=2)
F4 = dn.filt(mrgc, sm_thr=100)
F5 = dn.filt(mrgc, db_saveblack=0)  # db_thr=1, rt_sigma=0.8
F6 = dn.filt(mrgc, db_saveblack=0, sm_thr=100, db_mode=1, rt_sigma=4, db_grain=58)

F1 = dn.rfs(F1, F2, "[2746 2778] [19713 19724]")
F1 = dn.rfs(F1, F3, "[805 846] [19672 19706]")
F1 = dn.rfs(F1, F4, "[21140 21166]")
F1 = dn.rfs(F1, F5, "[10456 10473] [10551 10601] [11239 11319]")

F1 = dn.rfs_color(F1, F6, mask_src=mrgc, maps="[10456 10473] [10551 10601]")
F1 = dn.rfs_image(F1, F6, "e6 45234", "[11239 11319]")
# ------------ #

# ----out----- #
clip = dn.out(F1, epname)
clip.set_output()
# ------------ #

# ----save---- #
# dn.pw4(mrgc, 2, 1, epis, clip).set_output()
# epis.set_output()
# clip.std.Trim(17199, 17531).set_output()
# output = clip.std.Trim(10456, 10473) + clip.std.Trim(10551, 10601) + clip.std.Trim(11239, 11319); output.set_output()

# dn.rfs_resc(mrgc, epis, desc_h=desc_h, mthr=50, out_mask=True).set_output()
# ------------ #

# ----err----- #
dn.check_num_frames(epis, clip)
# ------------ #
