import dnfunc as dn

# -----in----- #
epname = dn.fname(__file__)
kernel, desc_h = "bilinear", 719

OP = dn.chapt(epname, "OP")
OPend = dn.chapt(epname, "OPend")
ED = dn.chapt(epname, "ED")
EDend = dn.chapt(epname, "EDend")
Next = dn.chapt(epname, "Next")

epis = dn.source(f"./in/{epname}.mp4")
# ------------ #

# ----mrgc---- #
aaep = dn.aa(epis, desc_h=desc_h, kernel=kernel)
op = dn.oped(epis, name="op1", offset=36, start=OP, end=OPend, desc_h=desc_h)
ed = dn.oped(epis, name="ed1", offset=24, start=ED, end=EDend, desc_h=desc_h)

mrgc = (
    aaep.std.Trim(0, OP - 1)
    + op
    + aaep.std.Trim(OPend, ED - 1)
    + ed
    + aaep.std.Trim(EDend, epis.num_frames - 1)
)
# ------------ #

# ----mask---- #
mrgc = dn.rfs(mrgc, epis, [(Next, epis.num_frames - 1)])  # next
mrgc = dn.rfs_resc(mrgc, epis, desc_h=desc_h + 1, mthr=30, maps=[(OP + 515, OP + 657)])  # op1
mrgc = dn.rfs_resc(mrgc, epis, desc_h=desc_h + 1, mthr=30, maps=[(ED + 805, ED + 916)])  # ed1

mrgc = dn.rfs_qtgmc(mrgc, aaep, k=1, maps=[(8170, 8423)])
# ------------ #

# ----filt---- #
"""
def filt_old(
    mrgc=mrgc,
    sm_thr=50,
    dn_pref=1,
    cs_mode=1,
    cs_val=0.5,
    db_thr=1.9,
    db_mode=3,
    db_det=64,
    db_grain=48,
    db_range=10,
    db_saveblack=2,
    db_cs=False,
    rt_sigma=0.85,
    ag_str=0,
    ag_scaling=12,
    out_mode=0,
):
"""

F1 = dn.filt(mrgc)
F2 = dn.filt(mrgc, db_saveblack=0)
F3 = dn.filt(mrgc, sm_thr=40, db_thr=1.0, rt_sigma=0.6)

F1 = dn.rfs(F1, F2, [(OP, OPend - 1), (ED, EDend - 1)])
F1 = dn.rfs(F1, F3, [(OPend - 177, OPend - 1)])  # op1
# ------------ #

# ----out----- #
clip = dn.out(F1, epname)
clip.set_output()
# ------------ #

# ----save---- #
# dn.pw4(mrgc, 2, 1, epis, clip).set_output()
# epis.set_output()
# clip.std.Trim(8170, 8423).set_output()
# ------------ #

# ----err----- #
dn.check_num_frames(epis, clip)
# ------------ #
