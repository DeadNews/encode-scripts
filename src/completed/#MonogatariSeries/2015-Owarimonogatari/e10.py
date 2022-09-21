import dnfunc as dn

# -----in----- #
epname = dn.fname(__file__)
desc_h = 720

OP = 3789
OPend = 5227
ED = 32609

epis = dn.source(f"./in/{epname}.mkv")
EDend = epis.num_frames - 48
# ------------ #

# ----mrgc---- #
ed = dn.oped(epis, name="ed2", offset=12, start=ED, end=EDend, desc_h=desc_h)

aaep = dn.aa(epis, desc_h=desc_h)

mrgc = aaep.std.Trim(0, ED - 1) + ed + aaep.std.Trim(EDend, epis.num_frames - 1)
# ------------ #

# ----mask---- #
mrgc = dn.rfs_hard(mrgc, mrgc, mthr=99, maps="[2274 2507]")

hard = dn.hard(mrgc, mthr=20)
mrgc = dn.rfs_image(mrgc, hard, "e10 7534", "[7534 8016] [8118 8315] [8436 8537]")
mrgc = dn.rfs_image(mrgc, hard, "e10 23017", "[22934 23017]")
mrgc = dn.rfs_image(mrgc, hard, "e10 24191", "[24191 24409]")
mrgc = dn.rfs_image(mrgc, hard, "e10 24485", "[24485 24556]")
mrgc = dn.rfs_image(mrgc, hard, "e10 25235", "[25235 25342]")
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
F2 = dn.filt(mrgc, sm_thr=45, db_thr=1, rt_sigma=0.8)
F3 = dn.filt(mrgc, rt_sigma=0.8, db_saveblack=0)
F4 = dn.filt(mrgc, sm_thr=44, db_thr=1, rt_sigma=0.7)
F5 = dn.filt(mrgc, sm_thr=38, db_thr=1, rt_sigma=0.6, db_grain=40)
F6 = dn.filt(mrgc, sm_thr=300, db_thr=6, db_mode=1, rt_sigma=4, db_det=128)
F7 = dn.filt(mrgc, db_mode=1, db_saveblack=0)
F8 = dn.filt(mrgc, db_mode=1)
F9 = dn.filt(mrgc, db_thr=1, rt_sigma=0.8, db_saveblack=0)

F1 = dn.rfs(
    F1,
    F2,
    f"[{OP} {OPend-1}] [5992 6018] [8538 8615] [9636 12796] [12911 13493] [14835 15350] [20342 20626] [20741 22435]",
)
F1 = dn.rfs(F1, F3, f"[{ED} {EDend-1-24}]")
F1 = dn.rfs(F1, F4, "[15351 15404] [1865 1882] [13950 14027] [15405 15628] [19961 20104]")
F1 = dn.rfs(
    F1, F5, "[10389 10490] [19529 19735] [19817 19876] [20174 20341] [13788 13829] [14291 14312]"
)
F1 = dn.rfs(F1, F7, "[29564 29773] [29900 30175] [31817 32164]")
F1 = dn.rfs(F1, F8, "[30176 30421] [31010 31105]")
F1 = dn.rfs(F1, F9, "[3557 3585]")

F1 = dn.rfs_image(
    F1, F6, "e10 12691", "[12691 12784] [12972 13162] [13181 13412] [13434 13493] [15279 15350]"
)
F1 = dn.rfs_image(
    F1,
    F6,
    "e10 15917",
    "[15917 16069] [16118 16153] [16268 16432] [16528 16725] [17183 17230] [17755 17994] [18854 18973]",
)
# ------------ #

# ----out----- #
clip = dn.out(F1, epname)
clip.set_output()
# ------------ #

# ----save---- #
# dn.pw4(mrgc, 2, 1, epis, clip).set_output()
# epis.set_output()
# clip.std.Trim(28021, 29491).set_output()
# ------------ #

# ----err----- #
dn.check_num_frames(epis, clip)
# ------------ #
