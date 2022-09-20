import dnfunc as dn

# -----in----- #
epname = dn.fname(__file__)
desc_h = 720

ED = 34049 + 148
EDend = 36206

epis = dn.source(f"./in/{epname}.mkv")
# ------------ #

# ----mrgc---- #
ed = dn.oped(epis, name="ed5", offset=165, start=ED, end=EDend, desc_h=desc_h)

aaep = dn.aa(epis, desc_h=desc_h)

mrgc = aaep.std.Trim(0, ED - 1) + ed + aaep.std.Trim(EDend, epis.num_frames - 1)
# ------------ #

# ----mask---- #
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
F0 = F1
F2 = dn.filt(mrgc, sm_thr=45, db_thr=1, rt_sigma=0.8)
F3 = dn.filt(mrgc, sm_thr=44, db_thr=1, rt_sigma=0.7)
F4 = dn.filt(mrgc, sm_thr=38, db_thr=1, rt_sigma=0.6, db_grain=40)
F5 = dn.filt(mrgc, sm_thr=34, db_thr=1, rt_sigma=0.6, db_grain=36)
F6 = dn.filt(mrgc, sm_thr=60, db_thr=4, db_mode=1)
F7 = dn.filt(mrgc, db_mode=2)
F8 = dn.filt(mrgc, db_thr=1, rt_sigma=0.8)

F1 = dn.rfs(
    F1, F2, "[11634 11677] [12501 12578] [19214 19243] [21494 21515] [23316 23333] [28239 28274]"
)
F1 = dn.rfs(
    F1, F3, "[5587 5694] [19796 19873] [20867 20962] [21185 21202] [21398 21445] [8384 8429]"
)
F1 = dn.rfs(F1, F4, "[15107 15130] [18341 18370]")
F1 = dn.rfs(F1, F5, "[20752 20771]")
F1 = dn.rfs(F1, F8, "[28773 34048]")
F1 = dn.rfs(F1, F7, "[30098 30115]")
F1 = dn.rfs(F1, F0, "[29848 29934] [30296 30351]")

F1 = dn.rfs_image(F1, F6, "e16 29848", "[29848 29898]")
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
