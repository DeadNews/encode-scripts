import dnfunc as dn

# -----in----- #
epname = dn.fname(__file__)
kernel, desc_h = "bilinear", 720

epis = dn.source(f"./in/{epname}.mp4")
end = epis.num_frames - 1
# ------------ #

# ----mrgc---- #
aaep = dn.aa(epis, desc_h=desc_h, kernel=kernel)
mrgc = aaep
# ------------ #

# ----mask---- #
mrgc = dn.rfs_resc(mrgc, epis, desc_h=desc_h, mthr=40, maps=[(24, 83)])
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

F1 = dn.filt(mrgc, db_thr=2.8, sm_thr=200)
F2 = dn.filt(mrgc, mrgc=epis, db_saveblack=2, ag_str=0)

F1 = dn.rfs(F1, F2, [(0, 23), (end - 139, end)])
# ------------ #

# ----out----- #
clip = dn.out(F1, epname)
clip.set_output()
# ------------ #

# ----save---- #
# dn.pw4(mrgc, 2, 1, epis, clip).set_output()
# epis.set_output()

# dn.rfs_resc(mrgc, epis, desc_h=desc_h, mthr=40, out_mask=True).set_output()
# ------------ #

# ----err----- #
dn.check_num_frames(epis, clip)
# ------------ #
