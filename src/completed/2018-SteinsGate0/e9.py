import dnfunc as dn

# -----in----- #
epname = dn.fname(__file__)

OP = dn.chapt(epname, "OP")
OPend = dn.chapt(epname, "Part_A")
ED = dn.chapt(epname, "ED")
EDend = dn.chapt(epname, "Part_C", "Next")
Next = dn.chapt(epname, "Next")

epis = dn.source(f"./in/{epname}.mp4")
epis, epis_back, edgefixer = dn.edgefix(epis)
# ------------ #

# ----mrgc---- #
aaep = dn.aa(epis)
op = dn.oped(epis_back, name="op1", offset=24, start=OP, end=OPend, edgefix=edgefixer)
ed = dn.oped(epis_back, name="ed1", offset=0, start=ED, end=EDend, edgefix=edgefixer)

mrgc = (
    aaep.std.Trim(0, OP - 1)
    + op
    + aaep.std.Trim(OPend, ED - 1)
    + ed
    + aaep.std.Trim(EDend, epis.num_frames - 1)
)
# ------------ #

# ----mask---- #
maps = f"[{Next} {epis.num_frames-1}]"  # next
mrgc = dn.rfs_resc(mrgc, epis, mthr=50, maps=maps)
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
F2 = dn.filt(mrgc, sm_thr=50, db_thr=2.1, cs_val=0.55, db_det=64)
F3 = dn.filt(mrgc, sm_thr=50, db_thr=2.2, cs_val=0.50, db_det=64)
F4 = dn.filt(mrgc, db_saveblack=2)

F1 = dn.rfs(F1, F2, f"[{OP} {OPend-1}]")
F1 = dn.rfs(F1, F3, f"[{ED} {EDend-1}]")
F1 = dn.rfs(F1, F4, "[22808 24404]")
# ------------ #

# ----out----- #
clip = dn.out(F1, epname)
clip.set_output()
# ------------ #

# ----save---- #
# dn.pw4(mrgc, 2, 1, epis_back, clip).set_output()
# epis.set_output()

# dn.rfs_resc(mrgc, epis, mthr=50, out_mask=True).set_output()
# 67626
# core.std.Interleave([epis, epis_back]).set_output()
# core.std.Interleave([clip, core.fmtc.bitdepth(epis_back, bits=10)]).set_output()
# ------------ #

# ----err----- #
dn.check_num_frames(epis, clip)
# ------------ #
