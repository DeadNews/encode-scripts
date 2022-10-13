import dnfunc as dn

# -----in----- #
epname = dn.fname(__file__)
desc_h = 720

OP = 2326
OPend = 4484
ED = 34766
EDend = 36923

epis = dn.source(f"./in/{epname}.mkv")
# ------------ #

# ----mrgc---- #
op = dn.oped(epis, name="op3", offset=0, start=OP, end=OPend, desc_h=desc_h)
ed = dn.oped(epis, name="ed4", offset=12, start=ED, end=EDend, desc_h=desc_h)

aaep = dn.aa(epis, desc_h=desc_h)

mrgc = (
    aaep.std.Trim(0, OP - 1)
    + op
    + aaep.std.Trim(OPend, ED - 1)
    + ed
    + aaep.std.Trim(EDend, epis.num_frames - 1)
)
# ------------ #

# ----mask---- #
mrgc = dn.rfs(mrgc, aaep, [(OP + 339, OP + 486)])

stabilize_1 = dn.qtgmc(aaep, k=0.5)
mrgc = dn.rfs_image(mrgc, stabilize_1, "e11 32975", [(32975, 33142)])

stabilize_2 = dn.qtgmc(aaep)
mrgc = dn.rfs_image(mrgc, stabilize_2, "e11 11228", [(5613, 5683)])

hard = dn.hard(mrgc, mthr=20)
mrgc = dn.rfs_image(mrgc, hard, "e11 6253", [(6253, 6444)])
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
F3 = dn.filt(mrgc, db_mode=1, sm_thr=100)
F4 = dn.filt(mrgc, db_mode=1, db_saveblack=0)
F5 = dn.filt(mrgc, sm_thr=34, db_thr=1, rt_sigma=0.6, db_grain=36)

F1 = dn.rfs(F1, F2, [(19014, 19407), (22642, 22689)])
F1 = dn.rfs(F1, F3, [(11258, 11297)])
F1 = dn.rfs(F1, F4, [(33449, 33487)])
F1 = dn.rfs(F1, F5, [(7024, 7041)])
# ------------ #

# ----out----- #
clip = dn.out(F1, epname)
clip.set_output()
# ------------ #

# ----save---- #
# dn.pw4(mrgc, 2, 1, epis, clip).set_output()
# epis.set_output()
# clip.std.Trim(5590, 5710).set_output()

# dn.rfs_resc(mrgc, epis, desc_h=desc_h, mthr=50, out_mask=True).set_output()
# ------------ #

# ----err----- #
dn.check_num_frames(epis, clip)
# ------------ #
