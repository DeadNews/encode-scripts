import dnfunc as dn

# -----in----- #
epname = dn.fname(__file__)

OP = dn.chapt(epname, "OP")
OPend = dn.chapt(epname, "Part_A")
PreED = dn.chapt(epname, "ED")
ED = dn.chapt(epname, "realED", "ED")
EDend = dn.chapt(epname, "EDend")

epis = dn.source(source=f"./in/{epname}.mp4")
# ------------ #

# ----mrgc---- #
aaep = dn.aa(epis)
op = dn.oped(epis, name="op4", offset=0, start=OP, end=OPend)
ed = dn.oped(epis, name="ed4", offset=0, start=ED, end=EDend)

mrgc = aaep.std.Trim(0, OP - 1) + op + aaep.std.Trim(OPend, ED - 1) + ed
# ------------ #

# ----mask---- #
maps = [(OPend, OPend + 130)] if PreED == ED else [(OPend, OPend + 130), (PreED, ED - 1)]

mrgc = dn.rfs_resc(mrgc, epis, desc_h=873 + 1, b=0.33, c=0.33, mthr=40, maps=maps)
# ------------ #

# ----filt---- #
"""
def filt_old(
    mrgc=mrgc,
    sm_thr=50,
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
# ------------ #

# ----out----- #
clip = dn.out(F1, epname)
clip.set_output()
# ------------ #

# ----save---- #
# dn.pw4(mrgc, 2, 1, epis, clip).set_output()
# epis.set_output()
# ------------ #

# ----err----- #
dn.check_num_frames(epis, clip)
# ------------ #
