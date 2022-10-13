import dnfunc as dn

# -----in----- #
epname = dn.fname(__file__)
desc_h = 720

OP = 1224
OPend = 3381
Next = 34766

epis = dn.source(f"./in/{epname}.mkv")
# ------------ #


def filt_ncop_aa(ncoped_aa):
    return dn.rfs_hard(ncoped_aa, ncoped_aa, mthr=99, maps=[(1391, 1463), (1608, 1635)])


# ----mrgc---- #
aaep = dn.aa(epis, desc_h=desc_h)
op = dn.oped(epis, name="op1", offset=12, start=OP, end=OPend, desc_h=desc_h, filtred=filt_ncop_aa)

mrgc = aaep.std.Trim(0, OP - 1) + op + aaep.std.Trim(OPend, epis.num_frames - 1)
# ------------ #

# ----mask---- #
mrgc = dn.rfs(mrgc, aaep, [(OP + 644, OP + 856)])
mrgc = dn.rfs(mrgc, epis, [(33258, Next - 1)])
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
F5 = dn.filt(mrgc, sm_thr=14, db_thr=1, rt_sigma=0.4, db_grain=16)
F6 = dn.filt(mrgc, sm_thr=300, db_thr=6, db_mode=1, rt_sigma=4, db_det=128)

F1 = dn.rfs(F1, F2, [(3927, 4034), (22877, 22915), (32430, 32513), (3837, 3927), (29763, 29834)])
F1 = dn.rfs(
    F1, F3, [(442, 483), (4934, 5140), (4135, 4234), (4322, 4369), (17521, 17583), (12854, 12876)]
)
F1 = dn.rfs(F1, F4, [(17023, 17067)])

F1 = dn.rfs_image(F1, F5, "e4 3908", [(3837, 3927)])
F1 = dn.rfs_image(F1, F6, "e4 32718", [(32718, 32849)])
F1 = dn.rfs_image(F1, F6, "e4 23739", [(23739, 23948), (24084, 24236), (24280, 24369)])
F1 = dn.rfs_image(F1, F6, "e4 30499", [(30499, 30564)])
# ------------ #

# ----out----- #
clip = dn.out(F1, epname)
clip.set_output()
# ------------ #

# ----save---- #
# dn.pw4(mrgc, 2, 1, epis, clip).set_output()
# epis.set_output()
# clip.std.Trim(0, 3000).set_output()

# dn.rfs_resc(mrgc, epis, desc_h=desc_h, mthr=50, out_mask=True).set_output()
# ------------ #

# ----err----- #
dn.check_num_frames(epis, clip)
# ------------ #
