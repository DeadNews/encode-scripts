import dnfunc as dn

# -----in----- #
epname = dn.fname(__file__)
desc_h = 720

OP = 2542
OPend = 4702
ED = 32417
EDend = 34576

epis = dn.source(f"./in/{epname}.mkv")
# ------------ #

# ----mrgc---- #
aaep = dn.aa(epis, desc_h=desc_h)

op = dn.oped(epis, name="op1", offset=12, start=OP, end=OPend, desc_h=desc_h)
ed = dn.oped(epis, name="ed1", offset=12, start=ED, end=EDend, desc_h=desc_h)

mrgc = (
    aaep.std.Trim(0, OP - 1)
    + op
    + aaep.std.Trim(OPend, ED - 1)
    + ed
    + aaep.std.Trim(EDend, epis.num_frames - 1)
)
# ------------ #

# ----mask---- #
mrgc = dn.rfs_hard(
    mrgc,
    mrgc,
    mthr=30,
    maps=[
        (OP - 12 + 1341, OP - 12 + 1372),
        (OP - 12 + 1400, OP - 12 + 1425),
        (OP - 12 + 1453, OP - 12 + 1476),
    ],
)

mrgc = dn.rfs_hard(
    mrgc,
    mrgc,
    mthr=20,
    maps=[
        (12651, 12709),
        (12818, 12897),
        (13452, 13544),
        (14192, 14221),
        (14878, 14937),
        (14987, 15058),
        (15215, 15334),
        (36751, 36810),
    ],
)
mrgc = dn.rfs_hard(mrgc, mrgc, mthr=95, maps=[(14230, 14323), (8260, 8337)])

hard = dn.hard(mrgc, mthr=20)
mrgc = dn.rfs_image(mrgc, hard, "e2 6601", [(6601, 6894)])
mrgc = dn.rfs_image(mrgc, hard, "e2 7105", [(7105, 7155)])
mrgc = dn.rfs_image(mrgc, hard, "e2 8363", [(8363, 8412)])
mrgc = dn.rfs_image(mrgc, hard, "e2 11700", [(11700, 11801)])
mrgc = dn.rfs_image(mrgc, hard, "e2 12710", [(12710, 12745)])
mrgc = dn.rfs_image(mrgc, hard, "e2 13134", [(13134, 13256), (13337, 13373), (13649, 14026)])
mrgc = dn.rfs_image(mrgc, hard, "e2 16081", [(16081, 16122)])
mrgc = dn.rfs_image(mrgc, hard, "e2 16123", [(14444, 14518), (15455, 15694), (16123, 16202)])

stabilize = dn.qtgmc(aaep)
mrgc = dn.rfs_image(mrgc, stabilize, "op 749", [(OP + 749, OP + 786)])
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
F3 = dn.filt(mrgc, rt_sigma=0.8)
F4 = dn.filt(mrgc, db_mode=2)
F5 = dn.filt(mrgc, sm_thr=35, db_thr=1, rt_sigma=0.8)
F6 = dn.filt(mrgc, db_saveblack=0)

F1 = dn.rfs(F1, F2, [(OP - 12 + 1510, OP - 12 + 1546)])
F1 = dn.rfs(F1, F3, [(OP - 12 + 373, OP - 12 + 760)])
F1 = dn.rfs(F1, F4, [(35842, 35919), (35983, 36192), (36427, 36600)])
F1 = dn.rfs(F1, F5, [(26996, 27040), (12977, 13061)])
F1 = dn.rfs(F1, F6, [(29195, 29317), (8719, 8777)])
# ------------ #

# ----out----- #
clip = dn.out(F1, epname)
clip.set_output()
# ------------ #

# ----save---- #
# dn.pw4(mrgc, 2, 1, epis, clip).set_output()
# epis.set_output()
# clip.std.Trim(3291, 3328).set_output()

# dn.rfs_resc(mrgc, epis, desc_h=desc_h, mthr=50, out_mask=True).set_output()
# ------------ #

# ----err----- #
dn.check_num_frames(epis, clip)
# ------------ #
