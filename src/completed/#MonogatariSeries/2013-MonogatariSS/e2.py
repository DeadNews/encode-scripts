import dnfunc as dn

# -----in----- #
epname = dn.fname(__file__)
desc_h = 720

OP = 2518
OPend = 4675
ED = 32608
EDend = 34765

epis = dn.source(f"./in/{epname}.mkv")
# ------------ #


def filt_ncop_aa(ncoped_aa):
    return dn.rfs_hard(ncoped_aa, ncoped_aa, mthr=99, maps=[(1391, 1463), (1608, 1635)])


# ----mrgc---- #
aaep = dn.aa(epis, desc_h=desc_h)
op = dn.oped(epis, name="op1", offset=12, start=OP, end=OPend, desc_h=desc_h, filtred=filt_ncop_aa)
ed = dn.oped(epis, name="ed1", offset=0, start=ED, end=EDend, desc_h=desc_h)

mrgc = (
    aaep.std.Trim(0, OP - 1)
    + op
    + aaep.std.Trim(OPend, ED - 1)
    + ed
    + aaep.std.Trim(EDend, epis.num_frames - 1)
)
# ------------ #

# ----mask---- #
mrgc = dn.rfs(mrgc, aaep, [(OP + 644, OP + 856)])

mrgc = dn.rfs_hard(mrgc, mrgc, mthr=2, maps=[(5644, 5713), (25103, 25143)])
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
F2 = dn.filt(mrgc, sm_thr=45, db_thr=1, rt_sigma=0.7)
F3 = dn.filt(mrgc, sm_thr=42, db_thr=1, rt_sigma=0.7)
F4 = dn.filt(mrgc, sm_thr=300, db_thr=6, db_mode=1, rt_sigma=4, db_det=128)
F5 = dn.filt(mrgc, db_mode=2)
F0 = dn.filt(mrgc, db_thr=0, sm_thr=0)

F1 = dn.rfs(F1, F2, [(16478, 17027), (17088, 17138)])
F1 = dn.rfs(F1, F3, [(6710, 6799), (7214, 7273), (17516, 18462)])
F1 = dn.rfs(F1, F5, [(21030, 21071)])

F1 = dn.rfs_image(F1, F4, "e2 2150", [(2150, 2177)])
F1 = dn.rfs_image(F1, F0, "e2 17516", [(17516, 18462)])
# ------------ #

# ----out----- #
clip = dn.out(F1, epname)
clip.set_output()
# ------------ #

# ----save---- #
# dn.pw4(mrgc, 2, 1, epis, clip).set_output()
# epis.set_output()
# clip.std.Trim(0, 30).set_output()

# dn.rfs_resc(mrgc, epis, desc_h=desc_h, mthr=50, out_mask=True).set_output()
# ------------ #

# ----err----- #
dn.check_num_frames(epis, clip)
# ------------ #
