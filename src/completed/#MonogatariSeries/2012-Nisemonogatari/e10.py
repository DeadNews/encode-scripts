import dnfunc as dn

# -----in----- #
epname = dn.fname(__file__)
desc_h = 720

OP = 2158
OPend = 4317
ED = 32611
EDend = 34768

epis = dn.source(f"./in/{epname}.mkv")
# ------------ #

# ----mrgc---- #
ed = dn.oped(epis, name="ed1", offset=12, start=ED, end=EDend, desc_h=desc_h)

aaep = dn.aa(epis, desc_h=desc_h)

mrgc = aaep.std.Trim(0, ED - 1) + ed + aaep.std.Trim(EDend, epis.num_frames - 1)
# ------------ #

# ----mask---- #
mrgc = dn.rfs_hard(mrgc, mrgc, mthr=20, maps=[(20770, 20837)])

hard = dn.hard(aaep, mthr=40)
mrgc = dn.rfs_image(mrgc, hard, "e10 26959", [(26959, 26996)])

stabilize = dn.qtgmc(aaep)
mrgc = dn.rfs_image(mrgc, stabilize, "e10 21557", [(21557, 21723)])
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
F2 = dn.filt(mrgc, sm_thr=90)
F3 = dn.filt(mrgc, sm_thr=300, db_thr=6, db_mode=1, rt_sigma=4, db_det=128)
F4 = dn.filt(mrgc, sm_thr=100, db_thr=3, db_mode=1)

F1 = dn.rfs(F1, F2, [(OP, OPend - 1)])
F1 = dn.rfs_image(F1, F3, "e10 11321", [(11321, 11561), (12004, 12052)])
F1 = dn.rfs_image(F1, F4, "e10 81310", [(20286, 20339), (20355, 20399), (20412, 20537)])
# ------------ #

# ----out----- #
clip = dn.out(F1, epname)
clip.set_output()
# ------------ #

# ----save---- #
# dn.pw4(mrgc, 2, 1, epis, clip).set_output()
# epis.set_output()
# clip.std.Trim(21557, 21723).set_output()

# dn.rfs_resc(mrgc, epis, desc_h=desc_h, mthr=50, out_mask=True).set_output()
# ------------ #

# ----err----- #
dn.check_num_frames(epis, clip)
# ------------ #
