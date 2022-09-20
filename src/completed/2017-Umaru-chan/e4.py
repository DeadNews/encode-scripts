import dnfunc as dn

# -----in----- #
epname = dn.fname(__file__)

OP = dn.chapt(epname, "OP")
OPend = dn.chapt(epname, "Part_A")
Part_B = dn.chapt(epname, "Part_B")
ED = dn.chapt(epname, "ED")
EDend = dn.chapt(epname, "Next", "Epilog")
Next = dn.chapt(epname, "Next")

epis = dn.source(f"./in/{epname}.mp4")
# ------------ #

# ----mrgc---- #
aaep = dn.aa(epis)
op = dn.oped(epis, name="op", offset=24, start=OP, end=OPend)
ed = dn.oped(epis, name="ed", offset=24, start=ED, end=EDend)

mrgc = (
    aaep.std.Trim(0, OP - 1)
    + op
    + aaep.std.Trim(OPend, ED - 1)
    + ed
    + aaep.std.Trim(EDend, epis.num_frames - 1)
)
# ------------ #

# ----mask---- #
signs_map = f"[3112 3209] [{Part_B-95} {Part_B+92}] [{Next} {epis.num_frames-1}]"
mrgc = dn.rfs_resc(mrgc, epis, mthr=60, maps=signs_map)
# ------------ #

# -----in----- #
"""
def filt_old(
    mrgc=mrgc,
    sm_thr=60,
    dn_pref=1,
    cs_mode=1,
    cs_val=0.5,
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
F2 = dn.filt(mrgc, db_saveblack=2, db_thr=2.5)
F3 = dn.filt(mrgc, db_thr=2.2)

F1 = dn.rfs(F1, F2, f"[{OP} {OPend-1}] [{ED} {EDend-1}]")
F1 = dn.rfs(F1, F3, "[13360 15831]")
# ------------ #

# ----out----- #
clip = dn.out(F1, epname)
clip.set_output()
# ------------ #

# ----save---- #
# dn.pw4(mrgc, 2, 1, epis, clip).set_output()
# 59002 62842
# epis.set_output()

# dn.rfs_resc(mrgc, epis, mthr=60, out_mask=True).set_output()
# ------------ #

# ----err----- #
dn.check_num_frames(epis, clip)
# ------------ #
