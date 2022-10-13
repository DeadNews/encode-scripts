import dnfunc as dn

# -----in----- #
epname = dn.fname(__file__)
str, kernel, desc_h = 0.5, "bicubic", 720

OP = dn.chapt(epname, "OP")
OPend = dn.chapt(epname, "Part_A")
ED = dn.chapt(epname, "ED")
EDend = dn.chapt(epname, "Epilog")

epis = dn.source(f"./in/{epname}.mp4")
# ------------ #

# ----mrgc---- #
aaep = dn.aa(epis, str=str, kernel=kernel, desc_h=desc_h)
op = dn.oped(epis, name="op1", offset=24, start=OP, end=OPend, desc_h=desc_h)

mrgc = aaep.std.Trim(0, OP - 1) + op + aaep.std.Trim(OPend, epis.num_frames - 1)
# ------------ #

# ----mask---- #
mrgc = dn.rfs_resc(mrgc, epis, desc_h=desc_h, kernel=kernel, mthr=30, maps=[(ED, EDend - 1)])
# ------------ #

# ----filt---- #
"""
def filt_old(
    mrgc=mrgc,
    sm_thr=91,
    dn_pref=1,
    cs_mode=1,
    cs_val=0.44,
    db_thr=2.0,
    db_mode=3,
    db_det=64,
    db_grain=48,
    db_range=15,
    db_saveblack=0,
    rt_sigma=0.91,
    ag_str=0,
    ag_scaling=12,
    out_mode=0,
):
"""

F1 = dn.filt(mrgc)
F2 = dn.filt(mrgc, sm_thr=150, rt_sigma=0.95, cs_val=0.32)
F3 = dn.filt(mrgc, sm_thr=100, rt_sigma=0.95, cs_val=0.32)

F1 = dn.rfs(F1, F2, [(0, OP - 1)])
F1 = dn.rfs(F1, F3, [(OP, OPend - 1), (ED, EDend - 1)])
# ------------ #

# ----out----- #
clip = dn.out(F1, epname)
clip.set_output()
# ------------ #

# ----save---- #
# dn.pw4(mrgc, 2, 1, epis, clip).set_output()
# 110258 94894 95374 97294 99694
# epis.set_output()
# clip.std.Trim(0, 3011).set_output()
# clip.std.Trim(23414, 23414+3000).set_output()

# dn.rfs_resc(mrgc, epis, desc_h=desc_h, kernel=kernel, mthr=30, out_mask=True).set_output()
# ------------ #

# ----err----- #
dn.check_num_frames(epis, clip)
# ------------ #
