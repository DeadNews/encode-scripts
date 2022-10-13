import dnfunc as dn

# -----in----- #
epname = dn.fname(__file__)
kernel, desc_h = "bilinear", 720

OP = dn.chapt(epname, "OP")
OPend = dn.chapt(epname, "OPend")
ED = dn.chapt(epname, "ED")
EDend = dn.chapt(epname, "EDend")

epis = dn.source(f"./in/{epname}.mp4")
# ------------ #

# ----mrgc---- #
aaep = dn.aa(epis, desc_h=desc_h, kernel=kernel)
mrgc = aaep
# ------------ #

# ----mask---- #
mrgc = dn.rfs(mrgc, epis, [(ED, EDend)])

mrgc = dn.rfs_hard(mrgc, mrgc, mthr=60, maps=[(ED - 24 + 1785, ED - 24 + 1888)])
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

F1 = dn.filt(mrgc)
F2 = dn.filt(mrgc, sm_thr=150, db_thr=3, ag_str=0.50, cs_val=0.4)
F3 = dn.filt(mrgc, sm_thr=150, db_thr=4, ag_str=0.40)
F4 = dn.filt(
    mrgc,
    sm_thr=200,
    db_thr=5,
    rt_sigma=1,
    ag_str=2.00,
    ag_scaling=0,
    cs_val=0.4,
)
F5 = dn.filt(mrgc, sm_thr=100, ag_str=0.50)
F6 = dn.filt(mrgc, sm_thr=30, db_thr=1.3, rt_sigma=0.7, ag_str=0, db_saveblack=2)

F1 = dn.rfs(F1, F2, [(OP, 32109)])  # OP
F1 = dn.rfs(F1, F3, [(32110, 32853)])
F1 = dn.rfs(F1, F4, [(ED, EDend)])  # ED
F1 = dn.rfs(F1, F5, [(ED - 24 + 552, ED - 24 + 655)])
F1 = dn.rfs(
    F1,
    F6,
    [(ED - 24 + 1067, ED - 24 + 1271), (ED - 24 + 1581, ED - 24 + 1679), (32854, OPend - 1)],
)
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
