import dnfunc as dn

# -----in----- #
epname = dn.fname(__file__)
desc_h = 720

ED = 32609

epis = dn.source(f"./in/{epname}.mkv")
EDend = epis.num_frames - 48
# ------------ #

# ----mrgc---- #
ed = dn.oped(epis, name="ed1", offset=12, start=ED, end=EDend, desc_h=desc_h)

aaep = dn.aa(epis, desc_h=desc_h)

mrgc = aaep.std.Trim(0, ED - 1) + ed + aaep.std.Trim(EDend, epis.num_frames - 1)
# ------------ #

# ----mask---- #
mrgc = dn.rfs_qtgmc(mrgc, aaep, maps="[12426 12923] [18463 18563] [16989 17305]")

mrgc = dn.rfs_hard(mrgc, mrgc, mthr=20, maps="[5412 5447] [6905 7060] [18663 18705] [19807 19824]")
mrgc = dn.rfs_hard(mrgc, mrgc, mthr=99, maps="[19744 19762] [12426 12683]")

hard = dn.hard(mrgc, mthr=20)
mrgc = dn.rfs_image(mrgc, hard, "e4 14400", "[14400 14428] [15194 15454]")
mrgc = dn.rfs_image(mrgc, hard, "e4 17612", "[17612 17641]")
mrgc = dn.rfs_image(mrgc, hard, "e4 19825", "[19825 19884]")
mrgc = dn.rfs_image(mrgc, hard, "e4 22615", "[22615 22680]")
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
F2 = dn.filt(mrgc, rt_sigma=0.8, db_saveblack=0)
F3 = dn.filt(mrgc, sm_thr=45, db_thr=1, rt_sigma=0.8)
F4 = dn.filt(mrgc, sm_thr=44, db_thr=1, rt_sigma=0.7)
F5 = dn.filt(mrgc, sm_thr=38, db_thr=1, rt_sigma=0.6, db_grain=40)
F6 = dn.filt(mrgc, db_mode=1)
F7 = dn.filt(mrgc, cs_val=0.99)
F8 = dn.filt(mrgc, db_saveblack=0, sm_thr=46, db_thr=1, rt_sigma=0.8)

F1 = dn.rfs(F1, F2, f"[{ED} {EDend-1-24}]")
F1 = dn.rfs(F1, F3, "[14756 14794]")
F1 = dn.rfs(F1, F4, "[24463 24498]")
F1 = dn.rfs(F1, F5, "[23866 23967] [25446 25469] [26168 26208] [26968 27042]")
F1 = dn.rfs(F1, F6, "[18612 18662] [19996 20091]")
F1 = dn.rfs(F1, F7, "[16989 17305]")
F1 = dn.rfs(F1, F8, "[22097 22188]")
# ------------ #

# ----out----- #
clip = dn.out(F1, epname)
clip.set_output()
# ------------ #

# ----save---- #
# dn.pw4(mrgc, 2, 1, epis, clip).set_output()
# epis.set_output()
# clip.std.Trim(16989, 17305).set_output()
# ------------ #

# ----err----- #
dn.check_num_frames(epis, clip)
# ------------ #
