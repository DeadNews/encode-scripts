import dnfunc as dn

# -----in----- #
epname = dn.fname(__file__)
desc_h = 720

ED = 34766
EDend = 36923

epis = dn.source(f"./in/{epname}.mkv")
# ------------ #

# ----mrgc---- #
ed = dn.oped(epis, name="ed2", offset=12, start=ED, end=EDend, desc_h=desc_h)

aaep = dn.aa(epis, desc_h=desc_h)

mrgc = aaep.std.Trim(0, ED - 1) + ed + aaep.std.Trim(EDend, epis.num_frames - 1)
# ------------ #

# ----mask---- #
mrgc = dn.rfs_qtgmc(mrgc, aaep, k=0.77, maps=[(14918, 15266), (21764, 21841), (21854, 21965)])

mrgc = dn.rfs_hard(mrgc, mrgc, mthr=99, maps=[(21764, 21841), (21854, 21965)])

hard = dn.hard(mrgc, mthr=20)
mrgc = dn.rfs_image(mrgc, hard, "e1 370", [(370, 405)])
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
F2 = dn.filt(mrgc, rt_sigma=0.7)
F3 = dn.filt(mrgc, rt_sigma=0.8)
F4 = dn.filt(mrgc, db_saveblack=0, rt_sigma=0.8)
F5 = dn.filt(mrgc, sm_thr=25, db_thr=1, rt_sigma=0.5, db_grain=16, db_range=5)
F6 = dn.filt(mrgc, sm_thr=45, db_thr=1, rt_sigma=0.7)
F7 = dn.filt(mrgc, sm_thr=45, db_thr=1, rt_sigma=0.7, db_saveblack=0)
F8 = dn.filt(mrgc, db_mode=2, db_saveblack=0)
F9 = dn.filt(mrgc, db_mode=1)
F10 = dn.filt(mrgc, db_mode=1, rt_sigma=0.8)
F11 = dn.filt(mrgc, db_mode=2, rt_sigma=0.8)
F12 = dn.filt(mrgc, db_saveblack=0, sm_thr=100, db_mode=1, rt_sigma=4, db_grain=58)
F13 = dn.filt(mrgc, db_saveblack=0)

F1 = dn.rfs(F1, F2, [(0, 773)])
F1 = dn.rfs(F1, F3, [(774, 8559), (26491, 26972)])
F1 = dn.rfs(F1, F5, [(241, 309), (690, 773)])
F1 = dn.rfs(F1, F6, [(370, 405), (406, 519), (3503, 3646), (4997, 5035), (5268, 5333)])
F1 = dn.rfs(F1, F9, "[10864 10895] ")
F1 = dn.rfs(F1, F10, [(26491, 26524)])
F1 = dn.rfs(F1, F11, [(26525, 26547), (26660, 26763), (219, 240), (96, 119)])
F1 = dn.rfs_image(F1, F4, "crop", [(2178, 2204), (6339, 6854), (7582, 7623), (2917, 3072)])
F1 = dn.rfs_image(F1, F7, "crop", [(2550, 2633), (2649, 2729), (5370, 5540), (5586, 5781)])
F1 = dn.rfs_image(F1, F8, "crop", [(10, 95), (2140, 2177)])
F1 = dn.rfs_image(F1, F5, "e1 519", [(454, 519)])
F1 = dn.rfs_image(F1, F5, "e1 520", [(520, 543)])
F1 = dn.rfs_image(F1, F5, "e1 405", [(370, 405)])
F1 = dn.rfs_image(F1, F13, "crop", [(5370, 5540)])

sb_filt = dn.rfs_color(F1, F12, mask_src=mrgc)
F1 = dn.rfs_image(
    F1,
    sb_filt,
    "crop",
    [
        (10, 95),
        (1330, 1347),
        (1701, 1718),
        (1836, 1982),
        (2649, 2681),
        (2917, 3072),
        (3835, 3864),
        (4152, 4337),
        (5370, 5540),
        (7408, 7431),
        (7720, 7821),
    ],
)
F1 = dn.rfs_image(F1, sb_filt, "e1 454", [(454, 519)])
# ------------ #

# ----out----- #
clip = dn.out(F1, epname)
clip.set_output()
# ------------ #

# ----save---- #
# dn.pw4(mrgc, 2, 1, epis, clip).set_output()
# epis.set_output()
# clip.std.Trim(0, 773).set_output()
# clip.std.Trim(1836, 1982).set_output()
# output = (
#     clip[10:95]
#     + clip[1330:1347]
#     + clip[1701:1718]
#     + clip[1836:1982]
#     + clip[2649:2681]
#     + clip[2917:3072]
#     + clip[3835:3864]
#     + clip[4152:4337]
#     + clip[5370:5540]
#     + clip[7408:7431]
#     + clip[7720:7821]
# )
# output.set_output()

# dn.rfs_resc(mrgc, epis, desc_h=desc_h, mthr=50, out_mask=True).set_output()
# ------------ #

# ----err----- #
dn.check_num_frames(epis, clip)
# ------------ #
