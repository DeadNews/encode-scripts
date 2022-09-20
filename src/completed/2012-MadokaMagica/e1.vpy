import dnfunc as dn

# -----in----- #
epname = dn.fname(__file__)
desc_h = 720
kernel, desc_h = "bicubic", 720

OP = 4786
OPend = 6574
ED = 180981
EDend = 188381

epis = dn.source(f"./in/{epname}.mp4")
# ------------ #

# ----mrgc---- #
aaep = dn.aa(epis, desc_h=desc_h, kernel=kernel)
op = dn.oped(epis, name="op1", offset=390, start=OP, end=OPend, desc_h=desc_h)

mrgc = (
    aaep.std.Trim(0, OP - 1)
    + op
    + aaep.std.Trim(OPend, ED - 1)
    + epis.std.Trim(ED, epis.num_frames - 1)
)
# ------------ #

# ----mask---- #
mrgc = dn.rfs_qtgmc(mrgc, aaep, k=2, maps="[168853 169295] [164242 164261] [164716 164781]")

stabilize = dn.qtgmc(mrgc, k=2)
mrgc = dn.rfs_image(
    mrgc, stabilize, "e1 164435", "[164435 164467] [165147 165561] [165864 166020] [166631 166768]"
)

mrgc = dn.rfs_hard(
    mrgc, mrgc, mthr=2, maps="[169404 169679] [170118 170189] [170220 170480] [168853 169295]"
)

hardd = dn.hard(mrgc, mthr=2)
hardy = dn.hard(mrgc, mthr=40)
mrgc = dn.rfs_image(mrgc, hardy, "14683", "[14683 14883]")
mrgc = dn.rfs_image(mrgc, hardd, "169296", "[169296 169403]")
# ------------ #

# -----in----- #
"""
def filt_old(
    mrgc=mrgc,
    sm_thr=48,
    tr=48,
    pref=1,
    cs_mode=99,
    cs_val=0.55,
    db_thr=1.0,
    db_mode=3,
    db_det=64,
    db_grain=48,
    db_range=10,
    db_saveblack=2,
    rt_sigma=0.9,
    out_mode=0,
):
"""

F1 = dn.filt(mrgc)
F2 = dn.filt(mrgc, db_thr=0, cs_mode=0)
F3 = dn.filt(mrgc, db_saveblack=0)
F4 = dn.filt(mrgc, db_saveblack=0, db_thr=1.1, sm_thr=50)
F5 = dn.filt(mrgc, db_thr=1.1, sm_thr=50)
F6 = dn.filt(mrgc, db_saveblack=0, sm_thr=42)
F7 = dn.filt(mrgc, sm_thr=36)
F8 = dn.filt(mrgc, sm_thr=46, rt_sigma=0.8)
F9 = dn.filt(mrgc, db_thr=2.1, sm_thr=50)
F10 = dn.filt(mrgc, db_saveblack=0, sm_thr=46, rt_sigma=0.8)

F1 = dn.rfs(F1, F2, f"[{ED} {EDend-1}]")
F1 = dn.rfs(
    F1,
    F3,
    "[14683 14883] [14992 15236] [39631 39711] [52806 52851] [61646 61826] [61903 61932] [63661 63734] [81676 82065] [82542 82565] [83102 83133] [88523 88760] [101620 101762] [117990 118235] [118272 118416] [118781 118960] [119492 120985] [135849 135890] [135945 136040]",
)  # [81676 82401]
F1 = dn.rfs(
    F1,
    F4,
    "[47938 48039] [51999 52106] [52314 52344] [92105 92161] [101009 101081] [102046 102177] [113658 113699] [121712 121810]",
)
F1 = dn.rfs(
    F1,
    F5,
    "[52493 52709] [61827 61871] [78322 78537] [78898 78987] [79305 79340] [91160 91543] [91733 91829] [92162 92245] [93083 93112] [102478 102513] [102592 102641] [130756 130842] [136869 136934] [137559 137807] [164782 164817] [177891 177939]",
)
F1 = dn.rfs(F1, F6, "[62114 62197] [155950 155991]")
F1 = dn.rfs(F1, F7, "[78538 78897] [79127 79162] [79235 79279] [80462 80485] [80639 80656]")
F1 = dn.rfs(
    F1,
    F8,
    "[79718 79930] [81349 81384] [84915 84935] [90926 90943] [98819 98902] [107417 107443] [111814 111867] [113612 113657] [116402 116739] [122110 122133] [127502 127518] [174128 174166] [174911 174976] [175736 175780] [5222 5292]",
)
F1 = dn.rfs(
    F1,
    F9,
    "[136311 136328] [136416 136517] [136614 136868] [136935 136959] [137020 137121] [137287 137308] [137334 137357] [137523 137558] [137808 138161] [138462 138521] [163993 164052] [168853 170189] [170220 170654] [179683 179737]",
)
F1 = dn.rfs(F1, F10, "[175007 175049]")
# ------------ #

# ----out----- #
clip = dn.out(F1, epname)
clip.set_output()
# ------------ #

# ----save---- #
# dn.pw4(mrgc, 2, 1, epis, clip).set_output()
# epis.set_output()
# clip.std.Trim(160050, 160200).set_output()
# clip.std.Trim(168853, 169295).set_output()
# ------------ #

# ----err----- #
dn.check_num_frames(epis, clip)
# ------------ #
