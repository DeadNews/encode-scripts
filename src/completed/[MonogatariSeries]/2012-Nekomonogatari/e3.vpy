import dnfunc as dn

# -----in----- #
epname = dn.fname(__file__)
desc_h = 720

OP = 408
OPend = 2568
ED = 35679
EDend = 37839

epis = dn.source(f"./in/{epname}.mkv")
# ------------ #

# ----mrgc---- #
op = dn.oped(epis, name="op1", offset=12, start=OP, end=OPend, desc_h=desc_h)
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
mrgc = dn.rfs(mrgc, aaep, f"[{OP+713} {OP+873}]")

hard = dn.hard(mrgc, mthr=9, yuv=False)
mrgc = dn.rfs_image(mrgc, hard, "2", "[4494 4523]")

stabilize = dn.qtgmc(aaep)
mrgc = dn.rfs(mrgc, stabilize, "[32602 33006] [34640 35109]")
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
F2 = dn.filt(mrgc, sm_thr=30, db_thr=1)
F3 = dn.filt(mrgc, sm_thr=60, db_saveblack=0)
F4 = dn.filt(mrgc, sm_thr=300, db_thr=6, db_mode=1, rt_sigma=4, db_det=128)
F5 = dn.filt(mrgc, sm_thr=38, db_thr=1, rt_sigma=0.6, db_grain=40)
F6 = dn.filt(mrgc, sm_thr=45, db_thr=1, rt_sigma=0.8)

F1 = dn.rfs(F1, F2, "[27487 27522]")
F1 = dn.rfs(F1, F5, "[15502 15519] [16453 16482] [17825 18121]")
F1 = dn.rfs(F1, F6, "[0 407] [2568 3888] [6994 7506]")

F1 = dn.rfs_image(F1, F3, "1", "[29582 29623]")
F1 = dn.rfs_image(F1, F4, "e3 13230", "[13230 13259] [16222 16413]")
# ------------ #

# ----out----- #
clip = dn.out(F1, epname)
clip.set_output()
# ------------ #

# ----save---- #
# dn.pw4(mrgc, 2, 1, epis, clip).set_output()
# epis.set_output()
# clip.std.Trim(32602, 33006).set_output()

# dn.rfs_resc(mrgc, epis, desc_h=desc_h, mthr=50, out_mask=True).set_output()
# ------------ #

# ----err----- #
dn.check_num_frames(epis, clip)
# ------------ #
