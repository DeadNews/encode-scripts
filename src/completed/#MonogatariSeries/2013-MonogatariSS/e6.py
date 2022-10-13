import dnfunc as dn

# -----in----- #
epname = dn.fname(__file__)
desc_h = 720

ED = 34766
EDend = 36923

epis = dn.source(f"./in/{epname}.mkv")
# ------------ #

# ----mrgc---- #
aaep = dn.aa(epis, desc_h=desc_h)

ed = dn.oped(epis, name="ed3", offset=0, start=ED, end=EDend, desc_h=desc_h)

mrgc = aaep.std.Trim(0, ED - 1) + ed + aaep.std.Trim(EDend, epis.num_frames - 1)
# ------------ #

# ----mask---- #
mrgc = dn.rfs_qtgmc(mrgc, aaep, maps=[(4944, 5081)])

hard = dn.hard(mrgc, mthr=20)
mrgc = dn.rfs_image(mrgc, hard, "e6 8928", [(8928, 8945)])

mrgc = dn.rfs_hard(mrgc, mrgc, mthr=95, maps=[(5715, 5729), (1331, 1342)])
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
F7 = dn.filt(mrgc, db_mode=1)

F1 = dn.rfs(F1, F2, [(19519, 24607)])
F1 = dn.rfs(
    F1, F3, [(638, 673), (1034, 1081), (2102, 2173), (3578, 3595), (12118, 12132), (25801, 25845)]
)
F1 = dn.rfs(F1, F4, [(15154, 15315), (20309, 20458)])
F1 = dn.rfs(F1, F5, [(23161, 23231)])
F1 = dn.rfs(F1, F7, [(4527, 4544), (1181, 1204), (1289, 1330)])

F1 = dn.rfs_image(F1, F6, "e6 22171", [(22171, 22263)])
F1 = dn.rfs_image(F1, F6, "e6 19755", [(19755, 19800)])
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
