import dnfunc as dn

# -----in----- #
epname = dn.fname(__file__)

OP = dn.chapt(epname, "OP")
OPend = dn.chapt(epname, "Part_A")
ED = dn.chapt(epname, "ED")
EDend = dn.chapt(epname, "Next")
oped_maps = [(OP, OPend - 1), (ED, EDend - 1)]

epis = dn.source(f"./in/{epname}.mp4")
# ------------ #

# ----mrgc---- #
aaep = dn.aa(epis)
mrgc = dn.rfs_dehalo(aaep, epis, mode="kirsch", max_c=2, min_c=1)
mrgc = dn.rfs_dehalo(aaep, epis, mode="kirsch", max_c=4, min_c=1, maps=oped_maps)

mrgc = dn.rfs_resc(mrgc, epis, desc_h=938, mthr=33)
mrgc = dn.rfs_resc(mrgc, epis, desc_h=938, mthr=17, maps=oped_maps)
# ------------ #

# ----filt---- #
"""
def filt_old(
    mrgc=mrgc,
    sm_thr=50,
    dn_pref=1,
    cs_mode=1,
    cs_val=0.20,
    db_thr=2.3,
    db_mode=3,
    db_det=64,
    db_grain=48,
    db_range=15,
    db_saveblack=2,
    db_cs=2,
    rt_sigma=1.0,
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

# dn.rfs_resc(mrgc, epis, desc_h=938, mthr=32, out_mask=True).set_output()
# dn.rfs_dehalo(aaep, epis, mode='kirsch', max_c=1, min_c=1, maps=None, out_mask=True).set_output()
# ------------ #

# ----err----- #
dn.check_num_frames(epis, clip)
# ------------ #
