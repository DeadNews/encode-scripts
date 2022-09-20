import dnfunc as dn

# -----in----- #
epname = dn.fname(__file__)
desc_h = 720

OP = 2830
OPend = 4269
ED = 32611

epis = dn.source(f"./in/{epname}.mkv")
EDend = epis.num_frames - 38
# ------------ #

# ----mrgc---- #
ed = dn.oped(epis, name="ed2", offset=12, start=ED, end=EDend, desc_h=desc_h)

aaep = dn.aa(epis, desc_h=desc_h)

mrgc = aaep.std.Trim(0, ED - 1) + ed + aaep.std.Trim(EDend, epis.num_frames - 1)
# ------------ #

# ----mask---- #
mrgc = dn.rfs_qtgmc(mrgc, aaep, maps="[891 1175] [23226 23321] [24145 24178]")

mrgc = dn.rfs_hard(mrgc, epis, desc_h=desc_h, mthr=30, maps="[4714 4742]")

mrgc = dn.rfs_hard(mrgc, mrgc, mthr=20, maps="[1772 1804]")
mrgc = dn.rfs_hard(
    mrgc,
    mrgc,
    mthr=99,
    maps="[1341 1397] [2123 2179] [17967 18325] [18397 18428] [18841 18886] [18948 18989] [19734 19901] [21051 21074] [21126 21269] [21318 21389] [21423 21542] [24761 24820] [28459 28620]",
)

hard = dn.hard(mrgc, mthr=20)
mrgc = dn.rfs_image(mrgc, hard, "e8 620", "[620 824]")
mrgc = dn.rfs_image(mrgc, hard, "e8 1284", "[1284 1340]")
mrgc = dn.rfs_image(mrgc, hard, "e8 1455", "[1455 1572]")
mrgc = dn.rfs_image(
    mrgc,
    hard,
    "e8 11396",
    "[11396 11734] [11789 12107] [12503 12823] [13103 13201] [13274 13633] [13726 13980]",
)
mrgc = dn.rfs_image(
    mrgc,
    hard,
    "e8 6339-2",
    "[6339 6585] [6703 7020] [8007 8205] [8704 9003] [9409 9560] [9810 9964]",
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
F2 = dn.filt(mrgc, sm_thr=45, db_thr=1, rt_sigma=0.8)
F3 = dn.filt(mrgc, rt_sigma=0.8, db_saveblack=0)
F4 = dn.filt(mrgc, sm_thr=44, db_thr=1, rt_sigma=0.7)
F5 = dn.filt(mrgc, sm_thr=38, db_thr=1, rt_sigma=0.6, db_grain=40)
F6 = dn.filt(mrgc, sm_thr=300, db_thr=6, db_mode=1, rt_sigma=4, db_det=128)
F7 = dn.filt(mrgc, db_mode=1)
F8 = dn.filt(mrgc, db_mode=2)
F9 = dn.filt(mrgc, sm_thr=45, db_thr=1, rt_sigma=0.8, db_saveblack=0)
F10 = dn.filt(mrgc, db_mode=2, db_saveblack=0)

F1 = dn.rfs(
    F1, F2, f"[{OP} {OPend-1}] [2395 2454] [5134 25789] [29368 29397] [31890 31925]"
)  # vse
F1 = dn.rfs(F1, F3, f"[{ED} {EDend-1-24}]")
F1 = dn.rfs(
    F1,
    F4,
    "[17664 18334] [19431 19493] [20445 20561] [21075 21101] [21423 21542] [22190 22243] [23226 23321] [24657 24683] [25313 25381] [31768 31793]",
)
F1 = dn.rfs(F1, F5, "[16525 16548] [21543 21605]")
F1 = dn.rfs(F1, F7, "[566 619] [1176 1226] [1883 1923] [14032 14097] [16729 16773] [2623 2787]")
F1 = dn.rfs(F1, F8, "[4770 4859] [5675 6148] [13634 13696] [15712 15948] [21606 21718] ")
F1 = dn.rfs(
    F1,
    F9,
    "[17685 17720] [18590 18646] [19008 19094] [19932 20212] [20259 20444] [20562 20771] [21051 21074] [21126 21269] [21738 21746] [22869 22928] [24821 24892] [24929 24982] [25031 25180]",
)
F1 = dn.rfs(F1, F10, "[22506 22537] [22582 22680] [24145 24178] [24761 24820] [25382 25429]")

F1 = dn.rfs_image(F1, F6, "e8 5320", "[5320 5602]")
F1 = dn.rfs_image(
    F1, F6, "e8 6339", "[6339 6585] [6703 7020] [8007 8205] [8704 9003] [9409 9560] [9810 9964]"
)
F1 = dn.rfs_image(F1, F6, "e8 9597", "[9597 9632]")
F1 = dn.rfs_image(
    F1,
    F6,
    "e8 11396-2",
    "[11396 11734] [11789 12107] [12503 12823] [13103 13201] [13274 13633] [13726 13980]",
)
F1 = dn.rfs_image(F1, F6, "e8 27538", "[27538 27687]")
F1 = dn.rfs_image(F1, F6, "e8 28291", "[28291 28458]")
F1 = dn.rfs_image(F1, F9, "e8 18488", "[18488 18523] [18554 18589]")
# ------------ #

# ----out----- #
clip = dn.out(F1, epname)
clip.set_output()
# ------------ #

# ----save---- #
# dn.pw4(mrgc, 2, 1, epis, clip).set_output()
# epis.set_output()
# clip.std.Trim(18488, 18523).set_output()

# dn.rfs_resc(mrgc, epis, desc_h=desc_h, mthr=50, out_mask=True).set_output()
# ------------ #

# ----err----- #
dn.check_num_frames(epis, clip)
# ------------ #
