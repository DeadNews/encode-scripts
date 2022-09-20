import dnfunc as dn

# -----in----- #
epname = dn.fname(__file__)
desc_h = 720

ED = 14146

epis = dn.source(f"./in/{epname}.mkv")
EDend = epis.num_frames - 14
# ------------ #

# ----mrgc---- #
ed = dn.oped(epis, name="ed1", offset=12, start=ED, end=EDend, desc_h=desc_h)

aaep = dn.aa(epis, desc_h=desc_h)

mrgc = aaep.std.Trim(0, ED - 1) + ed + aaep.std.Trim(EDend, epis.num_frames - 1)
# ------------ #

# ----mask---- #
# mrgc = dn.rfs_hard(mrgc, epis, mthr=99, sangnomPP=False, yuv=False, maps="[26123 26181]")
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
    rt_sigma=0.9,
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
# clip.std.Trim(0, 3000).set_output()

# dn.rfs_resc(mrgc, epis, desc_h=desc_h, mthr=50, out_mask=True).set_output()
# ------------ #

# ----err----- #
dn.check_num_frames(epis, clip)
# ------------ #
