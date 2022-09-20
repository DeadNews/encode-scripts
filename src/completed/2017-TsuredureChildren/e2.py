import dnfunc as dn

# -----in----- #
epname = dn.fname(__file__)

OP = dn.chapt(epname, "OP")
OPend = dn.chapt(epname, "Epis")
ED = dn.chapt(epname, "ED")
EDend = dn.chapt(epname, "Next")

epis = dn.source(f"./in/{epname}.mp4")
# ------------ #

# ----mrgc---- #
aaep = dn.aa(epis)
mrgc = aaep
# ------------ #

# ----mask---- #
mrgc = dn.rfs_resc(mrgc, epis, mthr=140, maps=f"[{OP} {OPend-1}]")
mrgc = dn.rfs_resc(mrgc, epis, mthr=130, maps=f"[{ED} {EDend-1}]")

random_signs = "[1677 1770] [5546 5603] [9834 9898] [10193 10323] [14935 14958] [15259 15302] [16678 16690] [19386 19444]"
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
F2 = dn.filt(mrgc, sm_thr=60, db_thr=2.66, cs_val=0.60, db_cs=0, rt_sigma=0.8)

F1 = dn.rfs(F1, F2, "[14967 19324]")
# ------------ #

# ----out----- #
clip = dn.out(F1, epname)
clip.set_output()
# ------------ #

# ----save---- #
# dn.pw4(mrgc, 2, 1, epis, clip).set_output()
# 55478 62198 53298 55698 56178 56658
# epis.set_output()

# dn.rfs_resc(mrgc, epis, mthr=120, out_mask=True).set_output()
# ------------ #

# ----err----- #
dn.check_num_frames(epis, clip)
# ------------ #
