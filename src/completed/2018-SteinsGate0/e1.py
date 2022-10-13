import dnfunc as dn

# -----in----- #
epname = dn.fname(__file__)

Part_A = dn.chapt(epname, "Part_A")
ED = dn.chapt(epname, "ED")  # 32009
EDend = dn.chapt(epname, "Part_C", "Next")
Next = dn.chapt(epname, "Next")

epis = dn.source(f"./in/{epname}.mp4")
epis, epis_back, edgefixer = dn.edgefix(epis)
# ------------ #

# ----mrgc---- #
aaep = dn.aa(epis)
mrgc = aaep
# ------------ #

# ----mask---- #
maps = [(Next, epis.num_frames - 1)]  # next
maps += " [0 971]"  # titles

mrgc = dn.rfs_resc(mrgc, epis, mthr=50, maps=maps)
mrgc = dn.rfs_resc(mrgc, epis, mthr=30, maps=[(Part_A - 113, Part_A - 1)])  # prePart_A
mrgc = dn.rfs(mrgc, epis, [(ED, EDend - 1)])  # ed
# ------------ #

# ----filt---- #
# 1.1=2.0
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
F2 = dn.filt(mrgc, mrgc=epis_back, db_saveblack=2)

F1 = dn.rfs(F1, F2, [(ED, EDend - 1)])
# ------------ #

# ----out----- #
clip = dn.out(F1, epname)
clip.set_output()
# ------------ #

# ----save---- #
# dn.pw4(mrgc, 2, 1, epis_back, clip).set_output()
# aa 20534 55694
# db 2047 99694 97294 88654
# epis.set_output()
# clip.std.Trim(0, Part_A-1).set_output()
# clip.std.Trim(EDend, epis.num_frames-1).set_output()

# dn.rfs_resc(mrgc, epis, mthr=50, out_mask=True).set_output()
# ------------ #

# ----err----- #
dn.check_num_frames(epis, clip)
# ------------ #
