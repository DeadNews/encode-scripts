import dnfunc as dn

# -----in----- #
epname = dn.fname(__file__)
desc_h = 720

OP = 1726
OPend = 3886
ED = 34767
EDend = 36924

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

mrgc = dn.rfs_qtgmc(mrgc, aaep, maps=[(21546, 21605), (22455, 22519)])

mrgc = dn.rfs_hard(
    mrgc, mrgc, mthr=20, maps=[(4258, 4313), (23240, 23259), (17700, 17734), (22706, 22741)]
)
mrgc = dn.rfs_hard(mrgc, mrgc, mthr=85, maps=[(19019, 19174)])
mrgc = dn.rfs_hard(
    mrgc, mrgc, mthr=99, maps=[(21110, 21181), (21257, 21272), (21282, 21289), (21828, 22073)]
)

hard = dn.hard(mrgc, mthr=2)
mrgc = dn.rfs_image(mrgc, hard, "e5 13701", [(13701, 13817), (14828, 15004), (16018, 16053)])
mrgc = dn.rfs_image(mrgc, hard, "e5 19175", [(19175, 19210)])
mrgc = dn.rfs_image(mrgc, hard, "e5 20660", [(20660, 20710)])
mrgc = dn.rfs_image(mrgc, hard, "e5 21383", [(21360, 21383)])
mrgc = dn.rfs_image(mrgc, hard, "e5 21546", [(21546, 21605), (22455, 22519)])
mrgc = dn.rfs_image(mrgc, hard, "e5 22580", [(22580, 22681)])
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
F4 = dn.filt(mrgc, db_mode=2, db_saveblack=0)

F1 = dn.rfs(F1, F2, [(11023, 12451), (32862, 34345)])
F1 = dn.rfs(F1, F3, [(465, 776), (3982, 4877), (12452, 12811)])
F1 = dn.rfs(F1, F4, [(11802, 12304)])
# ------------ #

# ----out----- #
clip = dn.out(F1, epname)
clip.set_output()
# ------------ #

# ----save---- #
# dn.pw4(mrgc, 2, 1, epis, clip).set_output()
# epis.set_output()
# clip.std.Trim(21546, 21605).set_output()

# dn.rfs_resc(mrgc, epis, desc_h=desc_h, mthr=50, out_mask=True).set_output()
# ------------ #

# ----err----- #
dn.check_num_frames(epis, clip)
# ------------ #
