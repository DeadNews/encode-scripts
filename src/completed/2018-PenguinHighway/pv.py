import dnfunc as dn

# -----in----- #
epname = dn.fname(__file__)

epis = dn.source(f"./in/{epname}.mkv")
epis = epis.std.CropRel(top=104, bottom=104)

# -----ef----- #
epis_ef = epis.edgefixer.Continuity(top=2, bottom=2, left=2, right=2)
mrgc = epis_ef
# ------------ #

# ----filt---- #
"""
def filt_old(
    mrgc=mrgc,
    sm_thr=50,
    tr=16,
    pref=1,
    cs_mode=99,
    cs_val=0.5,
    db_thr=2.0,
    db_mode=1,
    db_det=64,
    db_grain=48,
    db_range=15,
    db_saveblack=2,
    rt_sigma=1,
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
# epis.set_output()
# dn.pw4(mrgc, 2, 1, epis, clip).set_output()
# ------------ #

# ----err----- #
dn.check_num_frames(epis, clip)
# ------------ #
