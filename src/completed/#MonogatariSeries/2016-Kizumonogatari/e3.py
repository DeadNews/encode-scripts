import dnfunc as dn

# -----in----- #
epname = dn.fname(__file__)
desc_h = 544

ED = 109374

epis = dn.source(f"./in/{epname}.mkv")
epis = epis.std.CropRel(top=132, bottom=132)
# ------------ #

# ----mrgc---- #
epis_ef = epis.edgefixer.Continuity(top=2, bottom=2)
aaep = dn.aa(epis_ef, desc_h=desc_h)

mrgc = aaep
# ------------ #

# ----mask---- #
mrgc = dn.rfs_image(mrgc, epis_ef, maskname="1", maps=[(10695, 10840)])

mrgc = dn.rfs_hard(mrgc, mrgc, mthr=20, yuv=False, maps=[(55170, 55235)])
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
    rt_sigma=0.8,
    out_mode=0,
):
"""

F0 = dn.filt(epis, db_thr=0)

F1 = dn.filt(mrgc)

F1 = dn.rfs(F1, F0, [(ED, epis.num_frames - 1)])
# ------------ #

# ----out----- #
clip = dn.out(F1, epname)
clip.set_output()
# ------------ #

# ----save---- #
# dn.pw4(mrgc, 2, 1, epis, clip).set_output()
# epis.set_output()
# clip.std.Trim(ED, epis.num_frames-1).set_output()

# dn.rfs_resc(mrgc, epis, desc_h=desc_h, mthr=50, out_mask=True).set_output()
# ------------ #

# ----err----- #
dn.check_num_frames(epis, clip)
# ------------ #
