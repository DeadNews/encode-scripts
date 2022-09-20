import dnfunc as dn

# -----in----- #
epname = dn.fname(__file__)
kernel, desc_h = "bicubic", 720

OP = 6347
OPend = 8134
ED = 150405
EDend = 158273

epis = dn.source(f"./in/{epname}.mp4")
# ------------ #

# ----mrgc---- #
aaep = dn.aa(epis, desc_h=desc_h, kernel=kernel)
op = dn.oped(epis, name="op1", offset=390, start=OP, end=OPend, desc_h=desc_h)
ed = epis.std.Trim(ED, EDend - 1)

mrgc = (
    aaep.std.Trim(0, OP - 1)
    + op
    + aaep.std.Trim(OPend, ED - 1)
    + ed
    + aaep.std.Trim(EDend, epis.num_frames - 1)
)
# ------------ #

# ----mask---- #
mrgc = dn.rfs(mrgc, epis, "[159541 159743]")
mrgc = dn.rfs_image(mrgc, epis, "1", "[159188 159372]")
mrgc = dn.rfs_image(mrgc, epis, "2", "[159373 159504]")

stabilize = dn.qtgmc(mrgc, k=2)
mrgc = dn.rfs_image(mrgc, stabilize, "e2 81516", "[81516 81758] [81789 82094] [84128 84290]")
mrgc = dn.rfs_image(mrgc, stabilize, "e2 94824", "[94752 95045] [95190 95480]")
mrgc = dn.rfs_image(mrgc, stabilize, "e2 25915", "[25915 26106] [26713 26942]")
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
F3 = dn.filt(mrgc, db_saveblack=0)
F4 = dn.filt(mrgc, db_saveblack=0, db_thr=1.1, sm_thr=50)
F5 = dn.filt(mrgc, db_thr=1.1, sm_thr=50)
F8 = dn.filt(mrgc, sm_thr=46, rt_sigma=0.8)
F9 = dn.filt(mrgc, db_thr=2.1, sm_thr=50)
F11 = dn.filt(mrgc, db_thr=2.1, sm_thr=80)
F12 = dn.filt(mrgc, db_saveblack=0, db_thr=2.1, sm_thr=50)
F13 = dn.filt(mrgc, db_thr=0, cs_mode=0, sm_thr=2000)
F14 = dn.adaptive_grain(F13, strength=0.8, static=True, luma_ag_scaling=60, show_db_mode=False)

F1 = dn.rfs(
    F1,
    F3,
    "[281 721] [815 856] [9006 9154] [12520 14374] [14434 14821] [16919 18053] [18965 18997] [29267 29332] [50456 50490] [60241 60288] [63589 63708] [63955 64062] [77748 77840] [84838 84909] [91575 91634] [92075 92105] [104228 104257] [136746 136874] [145424 145471]",
)
F1 = dn.rfs(F1, F4, "[64357 64455] [136875 136994] [137491 137706] [142851 142997]")
F1 = dn.rfs(
    F1,
    F5,
    "[722 766] [857 905] [5808 5980] [9658 9774] [14822 14862] [18054 18313] [26662 26694] [29651 29670] [30907 30929] [31137 31185] [31221 31238] [49928 50011] [50108 50173] [64456 64595] [66026 66129] [66242 66343] [66639 66993] [73210 73242] [80898 80945] [108032 108163] [108785 110086] [110290 110796] [118726 118911] [136588 136745] [137025 137078] [137398 137490] [142778 142850] [158522 158545] [158569 158590]",
)
F1 = dn.rfs(F1, F8, "[3297 3353] [40721 40751] [42878 42943] [77526 77585]")
F1 = dn.rfs(
    F1,
    F9,
    "[6035 6098] [9791 9832] [27063 27110] [50258 50399] [57710 57769] [64216 64248] [64596 64657] [65898 65917] [100773 100832] [100887 100952] [101661 101726] [101750 101780] [101817 101954]",
)
F1 = dn.rfs(F1, F11, "[2709 2763] [134102 134317] [146597 148708] [157391 158272]")
F1 = dn.rfs(F1, F12, "[99103 99156] [113022 113037] [124683 125244] [150155 150401]")
F1 = dn.rfs(F1, F14, "[38928 40384] [41944 42117]")

F1 = dn.rfs_image(
    F1,
    F11,
    "e2 906",
    "[906 1035] [1057 1107] [1231 1649] [1692 1709] [1776 1943] [2016 2243] [2325 2612] [80809 80844]",
)
# ------------ #

# ----out----- #
clip = dn.out(F1, epname)
clip.set_output()
# ------------ #

# ----save---- #
# dn.pw4(mrgc, 2, 1, epis, clip).set_output()
# epis.set_output()
# clip.std.Trim(81516, 81758).set_output()
# clip.std.Trim(39384, 39884).set_output()
# clip.std.Trim(25915, 26106).set_output()
# ------------ #

# ----err----- #
dn.check_num_frames(epis, clip)
# ------------ #
