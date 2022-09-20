import dnfunc as dn

# -----in----- #
epname = dn.fname(__file__)
desc_h = 720

ED = 32608

epis = dn.source(f"./in/{epname}.mkv")
EDend = epis.num_frames - 37
# ------------ #

# ----mrgc---- #
ed = dn.oped(epis, name="ed1", offset=12, start=ED, end=EDend, desc_h=desc_h)

aaep = dn.aa(epis, desc_h=desc_h)

mrgc = aaep.std.Trim(0, ED - 1) + ed + aaep.std.Trim(EDend, epis.num_frames - 1)
# ------------ #

# ----mask---- #
mrgc = dn.rfs_qtgmc(mrgc, aaep, maps="[8137 8184]")

hard_def = dn.hard(mrgc, mthr=20)
mrgc = dn.rfs_image(mrgc, hard_def, "e3 5922", "[5922 6043] [7053 7172]")
mrgc = dn.rfs_image(mrgc, hard_def, "e3 8068", "[8068 8109]")
mrgc = dn.rfs_image(mrgc, hard_def, "e3 8185", "[8185 8220]")
mrgc = dn.rfs_image(
    mrgc,
    hard_def,
    "e3 9479",
    "[9479 9520] [9587 9682] [10034 10093] [10814 10921] [11015 11083] [11779 11856] [12043 12078]",
)
mrgc = dn.rfs_image(mrgc, hard_def, "e3 10334", "[10334 10374] [11186 11203] [11396 11488]")
mrgc = dn.rfs_image(mrgc, hard_def, "e3 10922", "[10922 11014]")
mrgc = dn.rfs_image(mrgc, hard_def, "e3 12127", "[12127 12264]")
mrgc = dn.rfs_image(mrgc, hard_def, "e3 12571", "[12571 12592]")
mrgc = dn.rfs_image(mrgc, hard_def, "e3 12670", "[12670 12735]")
mrgc = dn.rfs_image(mrgc, hard_def, "e3 13276", "[13276 13380]")
mrgc = dn.rfs_image(mrgc, hard_def, "e3 13633", "[13633 13766]")
mrgc = dn.rfs_image(mrgc, hard_def, "e3 13767", "[13767 13885]")
mrgc = dn.rfs_image(mrgc, hard_def, "e3 14094", "[14094 14130]")
mrgc = dn.rfs_image(mrgc, hard_def, "e3 14477", "[14477 14488]")
mrgc = dn.rfs_image(mrgc, hard_def, "e3 16070", "[16070 16141]")
mrgc = dn.rfs_image(
    mrgc, hard_def, "e3 17619", "[17340 17483] [17619 17780] [17871 18017] [18278 18301]"
)
mrgc = dn.rfs_image(mrgc, hard_def, "e3 30754", "[30754 30813]")
mrgc = dn.rfs_image(mrgc, hard_def, "e3 31045", "[31045 31134]")

hard_desc = dn.hard(epis, desc_h=desc_h, mthr=10)
mrgc = dn.rfs_image(mrgc, hard_desc, "e3 4553", "[4553 4648]")
mrgc = dn.rfs_image(mrgc, hard_desc, "e3 4722", "[4722 4769]")
mrgc = dn.rfs_image(mrgc, hard_desc, "e3 18908", "[18908 19099] [19898 20071]")
mrgc = dn.rfs_image(mrgc, hard_desc, "e3 21578", "[21578 21817] [22724 22987] [23126 23181]")
mrgc = dn.rfs_image(mrgc, hard_desc, "e3 23221", "[23221 23248] [23320 23355]")

mrgc = dn.rfs_hard(
    mrgc, mrgc, mthr=20, maps="[9422 9478] [13033 13049] [13134 13149] [15161 15177]"
)
mrgc = dn.rfs_hard(mrgc, mrgc, mthr=85, maps="[8137 8184] [13050 13112] [15388 15423]")
mrgc = dn.rfs_hard(mrgc, mrgc, mthr=99, maps="[15463 15528] [15845 16024] [16577 16618]")

stabilize = dn.qtgmc(mrgc)
mrgc = dn.rfs_image(mrgc, stabilize, "e3 21578", "[21578 21817] [22724 22987] [23126 23181]")
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
F5 = dn.filt(mrgc, sm_thr=300, db_thr=6, db_mode=1, rt_sigma=4, db_det=128)
F6 = dn.filt(mrgc, db_mode=1)
F7 = dn.filt(mrgc, sm_thr=45, db_thr=1, rt_sigma=0.8, db_saveblack=0)

F1 = dn.rfs(F1, F2, f"[{ED} {EDend-1-24}]")
F1 = dn.rfs(
    F1,
    F3,
    "[25176 25223] [25434 30693] [13150 13275] [13381 13462] [13522 13578] [14716 14754] [14805 14910] [14985 15000] [15019 15043] [15178 15201] [15230 15236] [30754 30813] [31045 31134]",
)
F1 = dn.rfs(F1, F4, "[25608 25769] [26998 27057] [30649 30693]")
F1 = dn.rfs(F1, F5, "[9204 9221]")
F1 = dn.rfs(
    F1,
    F6,
    "[4240 4266] [5140 5204] [11857 11934] [15220 15229] [22544 22582] [29779 29826] [29929 29970]",
)
F1 = dn.rfs(F1, F7, "[26647 26769]")
# ------------ #

# ----out----- #
clip = dn.out(F1, epname)
clip.set_output()
# ------------ #

# ----save---- #
# dn.pw4(mrgc, 2, 1, epis, clip).set_output()
# epis.set_output()
# clip.std.Trim(21578, 21817).set_output()

# dn.rfs_resc(mrgc, epis, desc_h=desc_h, mthr=50, out_mask=True).set_output()
# ------------ #

# ----err----- #
dn.check_num_frames(epis, clip)
# ------------ #
