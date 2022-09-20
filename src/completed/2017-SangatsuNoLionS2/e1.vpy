import dnfunc as dn

# -----in----- #
epname = dn.fname(__file__)
kernel, desc_h = "bilinear", 720

OP = dn.chapt(epname, "OP")
OPend = dn.chapt(epname, "OPend")
ED = dn.chapt(epname, "ED")
EDend = dn.chapt(epname, "EDend", "Next")
Next = dn.chapt(epname, "Next")

epis = dn.source(f"./in/{epname}.mp4")
# ------------ #

# ----mrgc---- #
aaep = dn.aa(epis, desc_h=desc_h, kernel=kernel)
op = dn.oped(epis, name="op1", offset=30, start=OP, end=OPend, desc_h=desc_h)
ed = dn.oped(epis, name="ed2", offset=24, start=ED, end=EDend, desc_h=desc_h)

mrgc = (
    aaep.std.Trim(0, OP - 1)
    + op
    + aaep.std.Trim(OPend, ED - 1)
    + ed
    + aaep.std.Trim(EDend, epis.num_frames - 1)
)
# ------------ #

# ----mask---- #
mrgc = dn.rfs(mrgc, epis, f"[{Next} {epis.num_frames-1}]")
mrgc = dn.rfs_resc(mrgc, epis, desc_h=desc_h, kernel=kernel, mthr=40, maps="[7274 8142]")
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
F3 = dn.filt(mrgc, db_saveblack=0, db_thr=3.9)  # op1
F4 = dn.filt(mrgc, sm_thr=30)

F1 = dn.rfs(F1, F2, f"[{ED} {EDend-1}]")
F1 = dn.rfs(F1, F3, f"[{OP} {OPend-1}]")
F1 = dn.rfs(F1, F4, "[1486 1557]")
# ------------ #

# ----out----- #
clip = dn.out(F1, epname)
clip.set_output()
# ------------ #

# ----save---- #
# dn.pw4(mrgc, 2, 1, epis, clip).set_output()
# epis.set_output()
# clip.std.Trim(0, OP-1).set_output()
# ------------ #

# ----err----- #
dn.check_num_frames(epis, clip)
# ------------ #
