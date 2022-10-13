import dnfunc as dn

# -----in----- #
epname = dn.fname(__file__)
desc_h = 720

OP = 1594
OPend = 3753
ED = 32931
EDend = 35091

epis = dn.source(f"./in/{epname}.mkv")
# ------------ #

# ----mrgc---- #
aaep = dn.aa(epis, desc_h=desc_h)
op = dn.oped(epis, name="op1", offset=12, start=OP, end=OPend, desc_h=desc_h)
ed = dn.oped(epis, name="ed1", offset=12, start=ED, end=EDend, desc_h=desc_h)

mrgc = (
    aaep.std.Trim(0, OP - 1)
    + op
    + aaep.std.Trim(OPend, ED - 1)
    + ed
    + aaep.std.Trim(EDend, epis.num_frames - 1)
)
# ------------ #

# ----mask---- #
mrgc = dn.rfs_hard(mrgc, mrgc, mthr=39, maps=[(10435, 10470)])
# ------------ #

# ----filt---- #
"""
def filt_old(
    mrgc=mrgc,
    sm_thr=50,
    tr=48,
    pref=1,
    cs_mode=99,
    cs_val=0.55,
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
F2 = dn.filt(mrgc, rt_sigma=0.8)
F3 = dn.filt(mrgc, db_mode=1, rt_sigma=0.8)
F4 = dn.filt(mrgc, db_mode=2, rt_sigma=0.8)
F5 = dn.filt(mrgc, db_mode=2, rt_sigma=0.7)
F6 = dn.filt(mrgc, sm_thr=300, db_thr=6, db_mode=1, rt_sigma=4, db_det=128)
F7 = dn.filt(mrgc, sm_thr=40, db_thr=1, rt_sigma=0.8)

F1 = dn.rfs(F1, F2, [(105, 407)])
F1 = dn.rfs(F1, F3, [(231, 257), (26732, 26971), (28754, 28807), (28829, 28900)])
F1 = dn.rfs(F1, F4, [(135, 230), (246, 293), (320, 371)])
F1 = dn.rfs(F1, F5, [(294, 319)])
F1 = dn.rfs(F1, F7, [(25385, 25537)])

F1 = dn.rfs_image(F1, F3, "e1 105", [(105, 134)])
F1 = dn.rfs_image(F1, F6, "e1 5803", [(5669, 5803)])
F1 = dn.rfs_image(
    F1, F6, "e1 29249", [(29249, 29371), (29983, 30240), (30857, 30909), (31519, 31590)]
)
# ------------ #

# ----out----- #
clip = dn.out(F1, epname)
clip.set_output()
# ------------ #

# ----save---- #
# dn.pw4(mrgc, 2, 1, epis, clip).set_output()
# epis.set_output()
# clip.std.Trim(0, 1593).set_output()
# ------------ #

# ----err----- #
dn.check_num_frames(epis, clip)
# ------------ #
