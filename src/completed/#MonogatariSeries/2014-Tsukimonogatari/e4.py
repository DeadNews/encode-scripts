import dnfunc as dn

# -----in----- #
epname = dn.fname(__file__)
desc_h = 720

ED = 45315

epis = dn.source(f"./in/{epname}.mkv")
EDend = epis.num_frames - 45
# ------------ #

# ----mrgc---- #
ed = dn.oped(epis, name="ed1", offset=12, start=ED, end=EDend, desc_h=desc_h)

aaep = dn.aa(epis, desc_h=desc_h)

mrgc = aaep.std.Trim(0, ED - 1) + ed + aaep.std.Trim(EDend, epis.num_frames - 1)
# ------------ #

# ----mask---- #
stabilize = dn.qtgmc(aaep, ThSAD1=640 * 2, ThSAD2=256 * 2, ThSCD1=180 * 6, ThSCD2=98 * 6)
mrgc = dn.rfs_image(mrgc, stabilize, "e4 17928", [(17928, 18113)])

hard = dn.hard(mrgc, mthr=40)
mrgc = dn.rfs_image(mrgc, hard, "e4 10937", [(10937, 10960)])
mrgc = dn.rfs_image(mrgc, hard, "e4 40913", [(40913, 41050)])
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
F2 = dn.filt(mrgc, db_mode=1)
F3 = dn.filt(mrgc, db_saveblack=0)
F4 = dn.filt(mrgc, sm_thr=30, db_thr=1, rt_sigma=0.8)

F1 = dn.rfs(F1, F2, [(18951, 19133), (20352, 20531), (40913, 41050), (41333, 41533)])
F1 = dn.rfs(F1, F3, [(35014, 35042)])
F1 = dn.rfs(F1, F4, [(31444, 31503)])
# ------------ #

# ----out----- #
clip = dn.out(F1, epname)
clip.set_output()
# ------------ #

# ----save---- #
# dn.pw4(mrgc, 2, 1, epis, clip).set_output()
# epis.set_output()
# clip.std.Trim(17928, 18113).set_output()

# dn.rfs_resc(mrgc, epis, desc_h=desc_h, mthr=50, out_mask=True).set_output()
# ------------ #

# ----err----- #
dn.check_num_frames(epis, clip)
# ------------ #
