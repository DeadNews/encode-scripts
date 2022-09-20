import dnfunc as dn

# -----in----- #
epname = dn.fname(__file__)

ep1 = 0
ep2 = 32330
ep3 = 63596
ep4 = 94862
ep5 = 126216
ep6 = 156714
end = 189456

epis = dn.source(f"./in/{epname}.mp4")
# ------------ #

# ----mrgc---- #
aaep = dn.aa(epis)

mrgc = dn.rfs(
    aaep,
    epis,
    f"[63495 {ep3-1}] [94766 {ep4-1}] [126106 {ep6-1}] [36618 36677] [66357 66413] [96904 96963] [158220 158279]",
)

mrgc = dn.rfs_hard(mrgc, epis, mthr=99, maps="[26123 26181]")
mrgc = dn.rfs_hard(mrgc, aaep, mthr=69, maps="[110403 110515]")
# ------------ #

# ----filt---- #
F10 = dn.filt(mrgc)
F11 = dn.filt(mrgc, sm_thr=60, db_thr=2.1, db_det=24, db_grain=32)
F12 = dn.filt(mrgc, sm_thr=60, db_thr=2.0, cs_val=0.80)
F13 = dn.filt(mrgc, sm_thr=110, cs_val=0.87, db_thr=2.1)
F14 = dn.filt(mrgc, sm_thr=100, db_thr=2.2, rt_sigma=0.7, ag_scaling=12, ag_str=0.3)
F15 = dn.filt(mrgc, sm_thr=54, db_thr=2.0, cs_val=0.87, rt_sigma=0.7)
F01 = dn.filt(mrgc, sm_thr=74, db_thr=1.8, cs_val=0.87)
F16 = dn.filt(mrgc, sm_thr=70, db_thr=2.1, cs_val=0.87)
F17 = dn.filt(mrgc, sm_thr=140, ag_str=0.5, ag_scaling=3)
F18 = dn.filt(mrgc, sm_thr=100)
F19 = dn.filt(mrgc, sm_thr=110, cs_val=0.87, rt_sigma=0.7)
F20 = dn.filt(mrgc, zone="e5")
F21 = dn.filt(mrgc, zone="e5", sm_thr=70, db_thr=2.0)
F22 = dn.filt(mrgc, zone="e5", db_thr=2.1)
F23 = dn.filt(mrgc, zone="e5", sm_thr=400, ag_str=1, ag_scaling=3)
F24 = dn.filt(mrgc, zone="e5", ag_str=0.75, ag_scaling=3)
F0 = dn.filt(epis, db_thr=0, sm_thr=70, ag_str=0)

F1 = dn.rfs(F10, F0, f"[{end} {epis.num_frames-1}]")
F1 = dn.rfs(F1, F11, "[92124 92445] [17358 17466]  [63836 64023]")
F1 = dn.rfs(F1, F12, "[44186 44390] [188505 188635]")
F1 = dn.rfs(
    F1,
    F13,
    "[43736 43830] [45000 45106] [46970 47166] [47345 47759] [48017 48141] [48693 48902] [22893 22999] [24511 24713] [167386 167777] [23737 23768]",
)
F1 = dn.rfs(F1, F14, "[25 3990]")
F1 = dn.rfs(F1, F15, "[21517 21612] [65601 66064] [114071 114348] [114978 115339]")
F1 = dn.rfs(F1, F16, "[84786 85037] [79044 79150] [79434 79589]")
F1 = dn.rfs(F1, F17, "[32330 34334] [34378 35586]")
F1 = dn.rfs(F1, F18, "[63603 63835] [64024 66301]")
F1 = dn.rfs(F1, F19, "[88326 88332] [88628 88680] [89149 89279] [92988 93028] [159297 159498]")
F1 = dn.rfs(F1, F01, "[113140 113198]")
#
F1 = dn.rfs(F1, F20, f"[126106 {ep6-1}]")
F1 = dn.rfs(F1, F21, "[140063 140086] [140111 140169]")
F1 = dn.rfs(F1, F22, "[153930 154621]")
F1 = dn.rfs(F1, F23, "[126216 129126]")
F1 = dn.rfs(
    F1, F24, "[143359 143777] [143847 143970] [144603 144685] [144885 145448] [145521 145620]"
)
# ------------ #

# ----out----- #
clip = dn.out(F1, epname)
clip.set_output()
# ------------ #

# ----save---- #
# dn.pw(mrgc, [1, 2, 3, 4, 5, 6], 'main', epis, clip).set_output()
# dn.pw(mrgc, [1, 2, 3, 4, 5, 6], 'e5', epis, clip, 'e5').set_output()
# dn.pw(mrgc, [1, 2, 3, 4, 5, 6], 'main', epis, clip, 'old').set_output()
# dn.pw(mrgc, [1, 2, 3, 4, 5, 6], 'main', epis, clip, 'main').set_output()
"""
aa 377778
db 43326 45246
---
aa 835597 500373
db 52757 376085 379925 257421 155909 156869 160709 165845 711762 1018616
db 436109 236630 511326 18365 8421 8854 12189 17749 156557 518165 171277 921037
"""
# epis.set_output()
# clip.std.Trim(ep2+23215, ep2+26307).set_output()
# clip.std.Trim(32330, 34334).set_output()
# clip.std.Trim(0, 4094).set_output()
# clip.std.Trim(126216, 129126-1500).set_output()
# clip.std.Trim(144885, 145448).set_output()
# ------------ #

# ----err----- #
dn.check_num_frames(epis, clip)
# ------------ #
