import dnfunc as dn

# -----in----- #
epname = dn.fname(__file__)

epis = dn.source(f"./in/{epname}.mp4")
# ------------ #

# -----aa----- #
mrgc = epis
# ------------ #

# ----mask---- #
mrgc = dn.rfs_hard(mrgc, mrgc, mthr=60, maps=[(1785, 1888)])
# ------------ #

# ----filt---- #
"""
def filt_old(
    mrgc=mrgc,
    sm_thr=100,
    dn_pref=3,
    cs_mode=1,
    cs_val=0.6,
    db_thr=2.3,
    db_mode=3,
    db_det=64,
    db_grain=58,
    db_range=15,
    db_saveblack=0,
    db_cs=True,
    rt_sigma=0.9,
    ag=True,
    ag_str=0.33,
    ag_scaling=12,
    out_mode=0,
):
"""

F1 = dn.filt(
    mrgc,
    sm_thr=200,
    db_thr=5,
    rt_sigma=1,
    ag_str=2.00,
    ag_scaling=0,
    cs_val=0.4,
)
F2 = dn.filt(mrgc, sm_thr=100, ag_str=0.50)
F3 = dn.filt(mrgc, sm_thr=30, db_thr=1.3, rt_sigma=0.7, ag_str=0, db_saveblack=2)

F1 = dn.rfs(F1, F2, [(552, 655)])
F1 = dn.rfs(F1, F3, [(1067, 1271), (1581, 1679)])
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
