import dnfunc as dn

# -----in----- #
epname = dn.fname(__file__)

Next = dn.chapt(epname, "Next")

epis = dn.source(f"./in/{epname}.mp4")
epis, epis_back, edgefixer = dn.edgefix(epis)
# ------------ #

# ----mrgc---- #
aaep = dn.aa(epis)
mrgc = aaep
# ------------ #

# ----mask---- #
maps = f"[{Next} {epis.num_frames-1}]"  # next
maps += " [671 2304]"  # op on epis
maps += " [30479 31600] [33916 34046]"  # ed on epis

mrgc = dn.rfs_resc(mrgc, epis, mthr=50, maps=maps)
mrgc = dn.rfs(mrgc, epis, "[32686 33915]")  # ed black
# ------------ #

# ----filt---- #
"""
def filt_old(
    mrgc=mrgc,
    sm_thr=40,
    dn_pref=1,
    cs_mode=1,
    cs_val=0.70,
    db_thr=2.1,
    db_mode=3,
    db_det=60,
    db_grain=48,
    db_range=15,
    db_saveblack=1,
    db_cs=2,
    rt_sigma=0.9,
    ag_str=0,
    ag_scaling=12,
    out_mode=0,
):
"""

F1 = dn.filt(mrgc)
F3 = dn.filt(mrgc, db_saveblack=2)

F1 = dn.rfs(F1, F3, "[32686 34046]")  # ed black
# ------------ #

# ----out----- #
clip = dn.out(F1, epname)
clip.set_output()
# ------------ #

# ----save---- #
# dn.pw4(mrgc, 2, 1, epis_back, clip).set_output()
# epis.set_output()

# dn.rfs_resc(mrgc, epis, mthr=50, out_mask=True).set_output()
# ------------ #

# ----err----- #
dn.check_num_frames(epis, clip)
# ------------ #
