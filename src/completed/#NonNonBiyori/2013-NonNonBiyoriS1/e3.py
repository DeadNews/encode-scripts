import dnfunc as dn

# -----in----- #
epname = dn.fname(__file__)
desc_h = 846

OP = 2062
OPend = 4221
ED = 31794
EDend = 33951

epis = dn.source(f"./in/{epname}.mkv")
# ------------ #

# ----mrgc---- #
aaep = dn.aa(epis, desc_h=desc_h)
op = dn.oped(epis, name="op1", offset=24, start=OP, end=OPend, desc_h=desc_h)
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
mrgc = dn.rfs(mrgc, aaep, f"[{ED} {ED+344-24}]")
mrgc = dn.rfs(mrgc, epis, f"[{OP+129} {OP+438}]")
# ------------ #

# -----in----- #
"""
def filt_old(
    mrgc=mrgc,
    sm_thr=50,
    tr=48,
    pref=1,
    cs_mode=99,
    cs_val=0.5,
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
F2 = dn.filt(mrgc, db_thr=1)
F3 = dn.filt(mrgc, db_thr=2.1)

F1 = dn.rfs(F1, F2, f"[{ED} {EDend-1}]")
F1 = dn.rfs(F1, F3, f"[{OP} {OPend-1}]")
# ------------ #

# ----out----- #
clip = dn.out(F1, epname)
clip.set_output()
# ------------ #

# ----save---- #
# dn.pw4(mrgc, 2, 1, epis, clip).set_output()
# epis.set_output()
# clip.std.Trim(22991, 25875).set_output()
# ------------ #

# ----err----- #
dn.check_num_frames(epis, clip)
# ------------ #