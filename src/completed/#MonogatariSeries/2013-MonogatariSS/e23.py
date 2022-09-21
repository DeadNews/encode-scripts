import dnfunc as dn

# -----in----- #
epname = dn.fname(__file__)
desc_h = 720

OP = 1942
Title = 4101
Next = 36924

epis = dn.source(f"./in/{epname}.mkv")
# ------------ #

# ----mrgc---- #
aaep = dn.aa(epis, desc_h=desc_h)
# ------------ #

# ----mask---- #
mrgc = dn.rfs_qtgmc(aaep, aaep, maps="[33507 33620]")

mrgc = dn.rfs_resc(
    mrgc,
    epis,
    desc_h=desc_h,
    mthr=50,
    maps="[31508 31610] [31628 31729] [31841 31948] [31997 32128] [32165 32464] [32541 32803] [32849 32968] [32993 33268] [33351 33638] [33757 33876] [33901 34020] [34134 34253] [34290 34418] [34455 34538]",
)
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
F0 = dn.filt(mrgc, rt_sigma=1)
F2 = dn.filt(mrgc, sm_thr=45, db_thr=1, rt_sigma=0.8)
F3 = dn.filt(mrgc, sm_thr=44, db_thr=1, rt_sigma=0.7)
F6 = dn.filt(mrgc, sm_thr=300, db_thr=6, db_mode=1, rt_sigma=4, db_det=128)

F1 = dn.rfs(F1, F2, "[17851 17970]")
F1 = dn.rfs(F1, F0, f"[{OP} {Title-1}]")
F1 = dn.rfs(F1, F3, "[33879 33941]")

F1 = dn.rfs_image(F1, F6, "e23 27845", "[27845 28039]")
F1 = dn.rfs_image(F1, F6, "e23 29239", "[29239 29388] [29455 29754]")
# ------------ #

# ----out----- #
clip = dn.out(F1, epname)
clip.set_output()
# ------------ #

# ----save---- #
# dn.pw4(mrgc, 2, 1, epis, clip).set_output()
# epis.set_output()
# clip.std.Trim(33507, 33620).set_output()

# dn.rfs_resc(mrgc, epis, desc_h=desc_h, mthr=50, out_mask=True).set_output()
# ------------ #

# ----err----- #
dn.check_num_frames(epis, clip)
# ------------ #
