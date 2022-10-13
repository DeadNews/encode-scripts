import dnfunc as dn

# -----in----- #
epname = dn.fname(__file__)
desc_h = 720

OP = 7336
OPend = 9494
ED = 32608
EDend = 34765

epis = dn.source(f"./in/{epname}.mkv")
# ------------ #

# ----mrgc---- #
aaep = dn.aa(epis, desc_h=desc_h)
ed = dn.oped(epis, name="ed4", offset=12, start=ED, end=EDend, desc_h=desc_h)

mrgc = aaep.std.Trim(0, ED - 1) + ed + aaep.std.Trim(EDend, epis.num_frames - 1)
# ------------ #

# ----mask---- #
mrgc = dn.rfs_resc(
    mrgc,
    epis,
    desc_h=desc_h,
    mthr=38,
    maps=[
        (7576, 7671),
        (7852, 7999),
        (8166, 8258),
        (8304, 8397),
        (8456, 8596),
        (8658, 8747),
        (8783, 8895),
        (8946, 9011),
        (9024, 9112),
        (9131, 9209),
        (9224, 9298),
        (9317, 9371),
        (9391, 9443),
    ],
)

hard = dn.hard(epis, desc_h=desc_h, mthr=10)
mrgc = dn.rfs_image(mrgc, hard, "e12 17415", [(17415, 17619), (17983, 18126)])
mrgc = dn.rfs_image(mrgc, hard, "e12 18705", [(18705, 18751), (18924, 19061), (19092, 19307)])
mrgc = dn.rfs_image(mrgc, hard, "e12 19695", [(19695, 19901), (19946, 20075), (20124, 20177)])
mrgc = dn.rfs_image(mrgc, hard, "e12 20420", [(20420, 20476)])
mrgc = dn.rfs_image(mrgc, hard, "e12 21789", [(21789, 21872), (22038, 22187)])
mrgc = dn.rfs_image(mrgc, hard, "e12 21897", [(21897, 22037), (21339, 21452)])

mrgc = dn.rfs_qtgmc(mrgc, mrgc, k=0.77, maps=[(21789, 21872), (22038, 22187)])
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
F3 = dn.filt(mrgc, sm_thr=44, db_thr=1, rt_sigma=0.7)
F4 = dn.filt(mrgc, sm_thr=38, db_thr=1, rt_sigma=0.6, db_grain=40)
F5 = dn.filt(mrgc, sm_thr=34, db_thr=1, rt_sigma=0.6, db_grain=36)
F6 = dn.filt(mrgc, sm_thr=300, db_thr=6, db_mode=1, rt_sigma=4, db_det=128)
F7 = dn.filt(mrgc, db_mode=2)
F8 = dn.filt(mrgc, db_saveblack=0)

F1 = dn.rfs(F1, F2, [(6105, 6266), (6513, 6530), (15661, 15690), (15802, 15819)])
F1 = dn.rfs(F1, F3, [(5459, 5536), (15093, 15223)])
F1 = dn.rfs(F1, F4, [(4828, 4907), (12153, 12212), (12327, 12396)])
F1 = dn.rfs(F1, F5, [(5675, 5740), (6303, 6380)])
F1 = dn.rfs(F1, F7, [(6801, 6836), (6903, 6944)])
F1 = dn.rfs(F1, F8, [(20225, 20311)])
F1 = dn.rfs_image(F1, F6, "e12 27912", [(27912, 27974)])
# ------------ #

# ----out----- #
clip = dn.out(F1, epname)
clip.set_output()
# ------------ #

# ----save---- #
# dn.pw4(mrgc, 2, 1, epis, clip).set_output()
# epis.set_output()
# clip2 = clip.std.Trim(21789, 21872) + clip.std.Trim(22038, 22187); clip2.set_output()

# dn.rfs_resc(mrgc, epis, desc_h=desc_h, mthr=38, out_mask=True).set_output()
# ------------ #

# ----err----- #
dn.check_num_frames(epis, clip)
# ------------ #
