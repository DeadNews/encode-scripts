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
# sharp = dn.rfs_sharp(aaep, sag_str=0.1)
# mrgc  = sharp
# ------------ #

# ----mask---- #
mrgc = dn.rfs_resc(mrgc, epis, mthr=140, maps=[(OP, OPend - 1)])
mrgc = dn.rfs_resc(mrgc, epis, mthr=130, maps=[(ED, EDend - 1)])

random_signs = [
    (1945, 1975),
    (5519, 5558),
    (5838, 5941),
    (8962, 9000),
    (9275, 9323),
    (12797, 12856),
    (13440, 13500),
    (17954, 18005),
]
mrgc = dn.rfs_resc(mrgc, epis, mthr=110, maps=random_signs)
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
# 11007 23000 56426  3082
# aa 14846 15806 23963 25402 26362 29242 54987 5782 27946 28426 30346 68950
# epis.set_output()
# clip.std.Trim(7183, 10178).set_output()

# dn.rfs_resc(mrgc, epis, mthr=120, out_mask=True).set_output()
# dn.rfs_sharp(F1, sag_str=0.1, out_mask=True).set_output()
# ------------ #

# ----err----- #
dn.check_num_frames(epis, clip)
# ------------ #
