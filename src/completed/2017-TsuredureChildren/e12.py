import dnfunc as dn

# -----in----- #
epname = dn.fname(__file__)

OP = dn.chapt(epname, "OP")
OPend = dn.chapt(epname, "Epis")
ED = dn.chapt(epname, "ED")

epis = dn.source(f"./in/{epname}.mp4")
EDend = epis.num_frames - 1
# ------------ #

# ----mrgc---- #
aaep = dn.aa(epis)
mrgc = aaep
# ------------ #

# ----mask---- #
mrgc = dn.rfs_resc(mrgc, epis, mthr=140, maps=f"[{OP} {OPend-1}]")
mrgc = dn.rfs_resc(mrgc, epis, mthr=130, maps=f"[{ED} {EDend-1}]")

random_signs = "[1728 1793] [8828 8893]"
mrgc = dn.rfs_resc(mrgc, epis, mthr=120, maps=random_signs)
# ------------ #

# ----filt---- #
"""
def filt_old(
    mrgc=mrgc,
    sm_thr=70,
    dn_pref=1,
    cs_mode=1,
    cs_val=0.50,
    db_thr=3.0,
    db_mode=3,
    db_det=64,
    db_grain=48,
    db_range=15,
    db_saveblack=0,
    db_cs=2,
    rt_sigma=0.9,
    ag_str=0,
    ag_scaling=12,
    out_mode=0,
):
"""

F1 = dn.filt(mrgc)
# ------------ #

# ----out----- #
clip = dn.out(F1, epname)
clip.set_output()
# ------------ #

# ----save---- #
# dn.pw4(mrgc, 2, 1, epis, clip).set_output()
# epis.set_output()

# dn.rfs_resc(mrgc, epis, mthr=120, out_mask=True).set_output()
# ------------ #

# ----err----- #
dn.check_num_frames(epis, clip)
# ------------ #
