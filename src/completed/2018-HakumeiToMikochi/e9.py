import dnfunc as dn

# -----in----- #
epname = dn.fname(__file__)
aa_str, kernel, desc_h = 0.58, "bicubic", 720

OP = dn.chapt(epname, "OP")
OPend = dn.chapt(epname, "OPend")
PartB = dn.chapt(epname, "Part_B")
ED = dn.chapt(epname, "ED")

epis = dn.source(f"./in/{epname}.mp4")
epis = epis.edgefixer.Continuity(2, 2, 2, 2)
EDend = epis.num_frames
# ------------ #

# ----mrgc---- #
aaep = dn.aa(epis, str=aa_str, kernel=kernel, desc_h=desc_h, yuv=True)
mrgc = aaep
# ------------ #

# ----mask---- #
mrgc = dn.rfs_resc(mrgc, epis, desc_h=desc_h, planes=[0, 1, 2], mthr=50, maps=[(ED, EDend - 1)])
mrgc = dn.rfs_resc(
    mrgc, epis, desc_h=desc_h, planes=[0, 1, 2], mthr=50, maps=[(PartB - 72, PartB - 1)]
)
mrgc = dn.rfs_resc(
    mrgc, epis, desc_h=desc_h, planes=[0, 1, 2], mthr=50, maps=[(20933, 21023)]
)  # e9
# ------------ #

# ----filt---- #
"""
def filt_old(
    mrgc=mrgc,
    sm_thr=50,
    dn_pref=1,
    cs_mode=1,
    cs_val=0.1,
    db_thr=2.4,
    db_mode=3,
    db_det=64,
    db_grain=48,
    db_range=15,
    db_saveblack=0,
    rt_sigma=1.1,
    ag_str=0,
    ag_scaling=12,
    out_mode=0,
):
"""

F1 = dn.filt(mrgc)
F2 = dn.filt(mrgc, sm_thr=70, db_thr=4, db_saveblack=2)

F1 = dn.rfs(F1, F2, [(ED, EDend - 1), (OP, OPend - 1)])
# ------------ #

# ----out----- #
clip = dn.out(F1, epname)
clip.set_output()
# ------------ #

# ----save---- #
# dn.pw4(mrgc, 2, 1, epis, clip).set_output()
# epis.set_output()
# dn.rfs_resc(mrgc, epis, desc_h=desc_h, mthr=50, out_mask=True).set_output()
# ------------ #

# ----err----- #
dn.check_num_frames(epis, clip)
# ------------ #
