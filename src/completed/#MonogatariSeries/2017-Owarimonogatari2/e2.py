import dnfunc as dn

# -----in----- #
epname = dn.fname(__file__)
desc_h = 720

OP = 2398
OPend = 4557
ED = 28868
EDend = 31026

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
F3 = dn.filt(mrgc, sm_thr=30, db_thr=1, rt_sigma=0.4)

F1 = dn.rfs(F1, F2, f"[{ED} {ED+112}] [26558 26641]")
F1 = dn.rfs(F1, F3, "[26354 26467]")
# ------------ #

# ----out----- #
clip = dn.out(F1, epname)
clip.set_output()
# ------------ #

# ----save---- #
# dn.pw4(mrgc, 2, 1, epis, clip).set_output()
# epis.set_output()
# clip.std.Trim(16569,16628).set_output()

# dn.rfs_resc(mrgc, epis, desc_h=desc_h, mthr=50, out_mask=True).set_output()
# ------------ #

# ----err----- #
dn.check_num_frames(epis, clip)
# ------------ #
