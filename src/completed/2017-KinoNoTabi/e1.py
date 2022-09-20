import dnfunc as dn

# -----in----- #
epname = dn.fname(__file__)
desc_h = 720

Avant = 0
Part_A = 3117
Part_B = 16376
ED = 30210
EDend = 32368
Next = 33950

epis = dn.source(f"./in/{epname}.mkv")
# ------------ #

# ----mrgc---- #
aaep = dn.aa(epis, desc_h=desc_h)
# mrgc =  aaep

ed = epis.std.Trim(ED, EDend - 1)

mrgc = aaep.std.Trim(0, ED - 1) + ed + aaep.std.Trim(EDend, epis.num_frames - 1)
# ------------ #

# ----mask---- #
mrgc = dn.rfs_hard(mrgc, epis, desc_h=desc_h, mthr=99, yuv=True, maps="[22144 22251]")

mrgc = dn.rfs_resc(
    mrgc, epis, desc_h=desc_h, mthr=50, maps="[298 3572] [29615 29624] [32397 32411]"
)
mrgc = dn.rfs_image(mrgc, epis, "e1 17", "[29625 29705]")
mrgc = dn.rfs_image(mrgc, epis, "e1 18", "[32412 32501]")
# ------------ #

# ----filt---- #
"""
def filt_old(
    mrgc=mrgc,
    sm_thr=100,
    tr=48,
    pref=1,
    cs_mode=99,
    cs_val=0.5,
    db_thr=2.1,
    db_mode=2,
    db_det=64,
    db_grain=52,
    db_range=15,
    db_saveblack=0,
    rt_sigma=1,
    out_mode=0,
):
"""

F1 = dn.filt(mrgc)
F2 = dn.filt(mrgc, sm_thr=60, db_mode=3)

F1 = dn.rfs(F1, F2, "[12916 12959]")
# ------------ #

# ----out----- #
clip = dn.out(F1, epname)
clip.set_output()
# ------------ #

# ----save---- #
# dn.pw4(mrgc, 2, 1, epis, clip).set_output()
# epis.set_output()
# clip.std.Trim(14918, 15266).set_output()
# clip.std.Trim(0, 10).set_output()

# dn.rfs_resc(mrgc, epis, desc_h=desc_h, mthr=50, out_mask=True).set_output()
# ------------ #

# ----err----- #
dn.check_num_frames(epis, clip)
# ------------ #
