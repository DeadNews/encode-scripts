import dnfunc as dn

# -----in----- #
epname = dn.fname(__file__)
aa_str, kernel, desc_h = 0.5, "bicubic", 720

ED = dn.chapt(epname, "ED")

epis = dn.source(f"./in/{epname}.mp4")
# ------------ #

# ----mrgc---- #
aaep = dn.aa(epis, str=aa_str, kernel=kernel, desc_h=desc_h)
mrgc = aaep
# ------------ #

# ----mask---- #
mrgc = dn.rfs_resc(
    mrgc, epis, desc_h=desc_h, kernel=kernel, mthr=30, maps=[(ED, epis.num_frames - 1)]
)
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
F2 = dn.filt(mrgc, db_saveblack=2)

F1 = dn.rfs(F1, F2, [(ED, epis.num_frames - 1)])
# ------------ #

# ----out----- #
clip = dn.out(F1, epname)
clip.set_output()
# ------------ #

# ----save---- #
# dn.pw4(mrgc, 2, 1, epis, clip).set_output()
# epis.set_output()
# ------------ #

# ----err----- #
dn.check_num_frames(epis, clip)
# ------------ #
