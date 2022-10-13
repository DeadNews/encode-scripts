import dnfunc as dn

# -----in----- #
epname = dn.fname(__file__)

ED = 121278

epis = dn.source(f"./in/{epname}.mp4")
mrgc = epis
# ------------ #

# ----filt---- #
"""
def filt_old(
    mrgc=mrgc,
    sm_thr=98,
    dn_pref=3,
    cs_mode=2,
    dn_pref_mul=8,
    cs_val=0.30,
    db_thr=2.2,
    db_mode=3,
    db_det=64,
    db_grain=48,
    db_range=15,
    db_saveblack=0,
    db_cs=2,
    rt_sigma=1.0,
    ag=True,
    ag_str=0.25,
    ag_scaling=12,
    out_mode=0,
):
"""

F1 = dn.filt(mrgc)
F2 = dn.filt(mrgc, db_saveblack=2, ag_str=0)
F3 = dn.filt(mrgc, sm_thr=75, rt_sigma=1.1)
F4 = dn.filt(mrgc, sm_thr=85, rt_sigma=1.1)

F1 = dn.rfs(F1, F2, [(0, 407), (123840, epis.num_frames - 1)])
F1 = dn.rfs(F1, F3, [(74577, 77483)])  # rain
F1 = dn.rfs(F1, F4, [(119319, 119508), (120153, 120296)])
# ------------ #

# ----out----- #
clip = dn.out(F1, epname)
clip.set_output()
# ------------ #

# ----save---- #
# dn.pw4(mrgc, 2, 1, epis, clip).set_output()
"""
176622 180942 195346 336878 255334 301894 318998
"""
# epis.set_output()
# clip.std.Trim(82029, 82029+3000).set_output()
# clip.std.Trim(0, 1139).set_output()
# clip.std.Trim(ED, epis.num_frames-1).set_output()
# ------------ #

# ----err----- #
dn.check_num_frames(epis, clip)
# ------------ #
