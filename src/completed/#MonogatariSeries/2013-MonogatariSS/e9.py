import dnfunc as dn

# -----in----- #
epname = dn.fname(__file__)
desc_h = 720

Preview = 36924

epis = dn.source(f"./in/{epname}.mkv")
# ------------ #

# ----mrgc---- #
aaep = dn.aa(epis, desc_h=desc_h)

mrgc = dn.rfs_resc(
    aaep,
    epis,
    desc_h=desc_h,
    mthr=50,
    maps="[29471 30316] [30343 30825] [30858 31043] [31139 31210] [31249 31335] [31355 31437]",
)
# ------------ #

# ----mask---- #
stabilize = dn.qtgmc(aaep)
mrgc = dn.rfs_image(mrgc, stabilize, "e9 32474", "[32474 32596]")

mrgc = dn.rfs_hard(mrgc, mrgc, mthr=60, maps="[26710 26757]")
mrgc = dn.rfs_hard(mrgc, mrgc, mthr=99, maps="[19870 19917] [32474 32596]")
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
F6 = dn.filt(mrgc, sm_thr=300, db_thr=6, db_mode=1, rt_sigma=4, db_det=128)
# F7 = dn.filt(mrgc, sm_thr=45, db_thr=1, rt_sigma=0.8, db_saveblack=0)
F8 = dn.filt(mrgc, db_thr=1, rt_sigma=0.8)
F9 = dn.filt(mrgc, db_mode=1)
F10 = dn.filt(mrgc, db_mode=2)
F11 = dn.filt(mrgc, sm_thr=60, db_thr=4, db_mode=1)
F12 = dn.filt(mrgc, db_saveblack=0, sm_thr=120, db_mode=1, rt_sigma=4, db_grain=58)

F1 = dn.rfs(F1, F2, "[13587 13651] [34410 34420] [33932 33968]")
F1 = dn.rfs(F1, F3, "[19918 20079] [20687 20837]")
F1 = dn.rfs(F1, F4, "[482 498] [1129 1151] [3930 3962]")
F1 = dn.rfs(F1, F5, "[4245 4336] [20986 21057]")
# F1 = dn.rfs(F1, F7, "[14010 14126] [29208 29231] [30833 30850]")
F1 = dn.rfs(F1, F8, "[25627 28409]")
F1 = dn.rfs(F1, F9, "[26649 26709]")
F1 = dn.rfs(F1, F10, "[26236 26355] [27036 27202] [27447 27518] [28638 28721]")
F1 = dn.rfs(F1, F0, "[26380 26534] [26788 27035] [27254 27410] [27519 27602] [28722 28829]")

F1 = dn.rfs_image(F1, F6, "e9 20495", "[20495 20542]")
F1 = dn.rfs_image(F1, F6, "e9 25837", "[25837 25878] [26123 26235] [26535 26648]")
F1 = dn.rfs_image(F1, F6, "e9 27834", "[27834 27881]")
F1 = dn.rfs_image(F1, F6, "e9 27882", "[27882 28164]")
F1 = dn.rfs_image(F1, F6, "e9 25759", "[25759 25836]")
F1 = dn.rfs_image(F1, F11, "e9 27603", "[27603 27644]")
F1 = dn.rfs_image(F1, F11, "e9 27675", "[27675 27749]")
F1 = dn.rfs_image(F1, F11, "e9 28164", "[28164 28213]")

F1 = dn.rfs_color(F1, F12, mask_src=mrgc, maps="[14010 14126] [29208 29231] [30833 30850]")
# ------------ #

# ----out----- #
clip = dn.out(F1, epname)
clip.set_output()
# ------------ #

# ----save---- #
# dn.pw4(mrgc, 2, 1, epis, clip).set_output()
# epis.set_output()
# clip.std.Trim(14010, 14126).set_output()

# dn.rfs_resc(mrgc, epis, desc_h=desc_h, mthr=50, out_mask=True).set_output()
# ------------ #

# ----err----- #
dn.check_num_frames(epis, clip)
# ------------ #
