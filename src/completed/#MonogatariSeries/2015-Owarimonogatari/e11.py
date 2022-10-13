import dnfunc as dn

# -----in----- #
epname = dn.fname(__file__)
desc_h = 720

OP = 3021
OPend = 4460
ED = 34047

epis = dn.source(f"./in/{epname}.mkv")
EDend = epis.num_frames - 38
# ------------ #

# ----mrgc---- #
ed = dn.oped(epis, name="ed2", offset=12, start=ED, end=EDend, desc_h=desc_h)

aaep = dn.aa(epis, desc_h=desc_h)

mrgc = aaep.std.Trim(0, ED - 1) + ed + aaep.std.Trim(EDend, epis.num_frames - 1)
# ------------ #

# ----mask---- #
hard = dn.hard(mrgc, mthr=20)
mrgc = dn.rfs_image(mrgc, hard, "e11 6701", [(6701, 6781)])
mrgc = dn.rfs_image(mrgc, hard, "e11 18393", [(18393, 18491)])
mrgc = dn.rfs_image(mrgc, hard, "e11 19410", [(19410, 19484)])
mrgc = dn.rfs_image(mrgc, hard, "e11 19605", [(19605, 19646)])
mrgc = dn.rfs_image(mrgc, hard, "e11 23225", [(23225, 23419)])
mrgc = dn.rfs_image(mrgc, hard, "e11 29043", [(29043, 29249), (29337, 29615), (29922, 30053)])

mrgc = dn.rfs_hard(mrgc, mrgc, mthr=20, maps=[(18099, 18350)])
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
F3 = dn.filt(mrgc, rt_sigma=0.8, db_saveblack=0)
F4 = dn.filt(mrgc, sm_thr=300, db_thr=6, db_mode=1, rt_sigma=4, db_det=128)
F5 = dn.filt(mrgc, db_mode=1)

F1 = dn.rfs(F1, F2, [(OP, OPend - 1), (9103, 9269), (9360, 9393), (9586, 9675)])
F1 = dn.rfs(F1, F3, [(ED, EDend - 1 - 24)])
F1 = dn.rfs(F1, F5, [(32802, 32873)])

F1 = dn.rfs_image(F1, F4, "e11 32873", [(32802, 32873)])
# ------------ #

# ----out----- #
clip = dn.out(F1, epname)
clip.set_output()
# ------------ #

# ----save---- #
# dn.pw4(mrgc, 2, 1, epis, clip).set_output()
# epis.set_output()
# clip.std.Trim(30000, 32800).set_output()

# dn.rfs_resc(mrgc, epis, desc_h=desc_h, mthr=50, out_mask=True).set_output()
# ------------ #

# ----err----- #
dn.check_num_frames(epis, clip)
# ------------ #
