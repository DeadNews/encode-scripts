import dnfunc as dn

# -----in----- #
epname = dn.fname(__file__)
desc_h = 720

OP = 3477
OPend = 5635
ED = 32610

epis = dn.source(f"./in/{epname}.mkv")
EDend = epis.num_frames - 39
# ------------ #

# ----mrgc---- #
op = dn.oped(epis, name="op3", offset=12, start=OP, end=OPend, desc_h=desc_h)
ed = dn.oped(epis, name="ed1", offset=12, start=ED, end=EDend, desc_h=desc_h)

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
hard = dn.hard(mrgc, mthr=20)
mrgc = dn.rfs_image(mrgc, hard, "e6 9103", "[9103 9129]")
mrgc = dn.rfs_image(mrgc, hard, "e6 13110", "[13110 13147]")
mrgc = dn.rfs_image(mrgc, hard, "e6 22463", "[22463 22510]")
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
F2 = dn.filt(mrgc, rt_sigma=0.8, db_saveblack=0)
F3 = dn.filt(mrgc, db_mode=1, db_saveblack=0)
F4 = dn.filt(mrgc, db_mode=2, db_saveblack=0)
F5 = dn.filt(mrgc, sm_thr=45, db_thr=1, rt_sigma=0.8)
F6 = dn.filt(mrgc, sm_thr=34, db_thr=1, rt_sigma=0.6, db_grain=36)
F7 = dn.filt(mrgc, db_mode=2)

F1 = dn.rfs(F1, F2, f"[{ED} {EDend-1-24}]")
F1 = dn.rfs(F1, F3, f"[{OP+33} {OP+95}]")
F1 = dn.rfs(F1, F4, f"[{OP+96} {OP+157}]")
F1 = dn.rfs(F1, F5, "[20658 20729] [21855 21874] [22463 22532] [25978 26010] [26790 26910]")
F1 = dn.rfs(F1, F6, "[20220 20375]")
F1 = dn.rfs(F1, F7, "[8963 9008]")
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
