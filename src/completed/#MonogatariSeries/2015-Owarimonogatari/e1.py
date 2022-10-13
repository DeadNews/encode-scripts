import dnfunc as dn

# -----in----- #
epname = dn.fname(__file__)
desc_h = 720

OP = 2949
OPend = 5107
ED = 36924

epis = dn.source(f"./in/{epname}.mkv")
EDend = epis.num_frames - 37
# ------------ #

# ----mrgc---- #
aaep = dn.aa(epis, desc_h=desc_h)

op = dn.oped(epis, name="op1", offset=12, start=OP, end=OPend, desc_h=desc_h)
ed = dn.oped(epis, name="ed1", offset=12, start=ED, end=EDend, desc_h=desc_h)

mrgc = (
    aaep.std.Trim(0, OP - 1)
    + op
    + aaep.std.Trim(OPend, ED - 1)
    + ed
    + aaep.std.Trim(EDend, epis.num_frames - 1)
)
# ------------ #

# ----mask---- #
mrgc = dn.rfs_qtgmc(
    mrgc,
    aaep,
    maps=[
        (857, 976),
        (14859, 15038),
        (15654, 15899),
        (22952, 23017),
        (23417, 23722),
        (35970, 36197),
        (19471, 19530),
        (19694, 19729),
        (25379, 25454),
    ],
)
mrgc = dn.rfs_qtgmc(mrgc, aaep, k=2, maps=[(20372, 20575)])

stabilize = dn.qtgmc(mrgc)
mrgc = dn.rfs_image(mrgc, stabilize, "e1 42", [(20, 47)])
mrgc = dn.rfs_image(mrgc, stabilize, "e1 48", "48")
mrgc = dn.rfs_image(mrgc, stabilize, "e1 49", "49")
mrgc = dn.rfs_image(mrgc, stabilize, "e1 50", "50")
mrgc = dn.rfs_image(mrgc, stabilize, "e1 5179", [(5179, 5211)])
mrgc = dn.rfs_image(mrgc, stabilize, "e1 12616", [(12616, 12645)])
mrgc = dn.rfs_image(mrgc, stabilize, "e1 28886", [(28886, 28915)])
mrgc = dn.rfs_image(mrgc, stabilize, "e1 25583", [(25583, 25612)])
mrgc = dn.rfs_image(mrgc, stabilize, "e1 26857", [(26857, 26868)])
mrgc = dn.rfs_image(mrgc, stabilize, "e1 33226", [(33226, 33249)])

mrgc = dn.rfs_hard(
    mrgc,
    mrgc,
    mthr=20,
    maps=[
        (5212, 5259),
        (5452, 5493),
        (14730, 14771),
        (16717, 16788),
        (22862, 22951),
        (23060, 23122),
        (32566, 32787),
        (6046, 6231),
        (7889, 7924),
        (8141, 8185),
        (14652, 14729),
        (19471, 19530),
        (19585, 19729),
        (32362, 32493),
        (32920, 33015),
        (33016, 33069),
    ],
)
mrgc = dn.rfs_hard(
    mrgc,
    mrgc,
    mthr=85,
    maps=[
        (6010, 6027),
        (19369, 19428),
        (19914, 19961),
        (32689, 32787),
        (35358, 35684),
        (35721, 35894),
    ],
)
mrgc = dn.rfs_hard(
    mrgc,
    mrgc,
    mthr=99,
    maps=[
        (18829, 19173),
        (19757, 19853),
        (6286, 6504),
        (6772, 7058),
        (7388, 7693),
        (14772, 14858),
        (16900, 17187),
        (17278, 17514),
        (17746, 17853),
        (18373, 18765),
        (18766, 18828),
        (27091, 27174),
        (27343, 27492),
        (27655, 27751),
        (28123, 28236),
        (28520, 28684),
        (31585, 31923),
        (35970, 36197),
        (5566, 5742),
        (30373, 30495),
        (9722, 9760),
        (9785, 9838),
        (9863, 9925),
        (9950, 9979),
        (11689, 11979),
        (12157, 12372),
        (15147, 15212),
        (15303, 15593),
        (15654, 15899),
        (15969, 15972),
        (18196, 18264),
        (19730, 19772),
        (22952, 23017),
        (23417, 23722),
        (24209, 24304),
        (24593, 24892),
        (25379, 25502),
        (27787, 27966),
        (29704, 29835),
        (30088, 30138),
        (35127, 35297),
    ],
)

hard = dn.hard(mrgc, mthr=20)
mrgc = dn.rfs_image(mrgc, hard, "e1 14240", [(14240, 14317)])
mrgc = dn.rfs_image(mrgc, hard, "e1 15993", [(15993, 16226)])
mrgc = dn.rfs_image(mrgc, hard, "e1 16551", [(16551, 16665)])
mrgc = dn.rfs_image(mrgc, hard, "e1 16900", [(16900, 17187)])
mrgc = dn.rfs_image(mrgc, hard, "e1 18301", [(18301, 18336)])
mrgc = dn.rfs_image(mrgc, hard, "e1 15993", [(15039, 15110)])
mrgc = dn.rfs_image(mrgc, hard, "e1 24945", [(24893, 24945)])
mrgc = dn.rfs_image(mrgc, hard, "e1 5842", [(5842, 5883)])
mrgc = dn.rfs_image(mrgc, hard, "e1 5308", [(5308, 5355)])
mrgc = dn.rfs_image(mrgc, hard, "e1 5914", [(5914, 6009)])
# on top of qtgmc
mrgc = dn.rfs_image(mrgc, hard, "e1 42", [(20, 47)])
mrgc = dn.rfs_image(mrgc, hard, "e1 48", "48")
mrgc = dn.rfs_image(mrgc, hard, "e1 49", "49")
mrgc = dn.rfs_image(mrgc, hard, "e1 50", "50")
mrgc = dn.rfs_image(mrgc, hard, "e1 5179", [(5179, 5211)])
mrgc = dn.rfs_image(mrgc, hard, "e1 12616", [(12616, 12645)])
mrgc = dn.rfs_image(mrgc, hard, "e1 28886", [(28886, 28915)])
mrgc = dn.rfs_image(mrgc, hard, "e1 25583", [(25583, 25612)])
mrgc = dn.rfs_image(mrgc, hard, "e1 26857", [(26857, 26868)])
mrgc = dn.rfs_image(mrgc, hard, "e1 33226", [(33226, 33249)])
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
F2 = dn.filt(mrgc, sm_thr=90, db_mode=1)
F3 = dn.filt(mrgc, sm_thr=180, db_mode=1, db_saveblack=0)
F4 = dn.filt(mrgc, rt_sigma=0.8, db_saveblack=0)
F5 = dn.filt(mrgc, sm_thr=45, db_thr=1, rt_sigma=0.8)
F6 = dn.filt(mrgc, sm_thr=44, db_thr=1, rt_sigma=0.7)
F7 = dn.filt(mrgc, sm_thr=38, db_thr=1, rt_sigma=0.6, db_grain=40)
F8 = dn.filt(mrgc, sm_thr=34, db_thr=1, rt_sigma=0.6, db_grain=36)
F9 = dn.filt(mrgc, sm_thr=300, db_thr=6, db_mode=1, rt_sigma=4, db_det=128)
F10 = dn.filt(mrgc, db_mode=1)
F11 = dn.filt(mrgc, db_thr=1, rt_sigma=0.8, db_saveblack=0)

F1 = dn.rfs(F1, F2, [(OP, OP - 24 + 386), (OP - 24 + 451, OPend - 1)])
F1 = dn.rfs(F1, F3, [(OP - 24 + 387, OP - 24 + 450)])
F1 = dn.rfs(F1, F4, [(ED, EDend - 1 - 24)])
F1 = dn.rfs(
    F1,
    F5,
    [
        (1613, 1786),
        (8381, 8422),
        (8543, 8572),
        (9761, 10177),
        (10786, 10845),
        (11101, 11169),
        (11980, 12120),
        (14318, 14347),
        (16837, 16860),
        (19875, 19913),
        (20010, 20059),
        (22550, 23017),
        (23249, 23284),
        (25948, 26019),
    ],
)
F1 = dn.rfs(F1, F6, [(1913, 2323), (12409, 12495)])
F1 = dn.rfs(F1, F7, [(12385, 12408), (33070, 33117)])
F1 = dn.rfs(F1, F8, [(9338, 9373)])
F1 = dn.rfs(F1, F10, [(2704, 2942), (10178, 10225), (21312, 21356), (9642, 9679), (20060, 20119)])
F1 = dn.rfs(F1, F11, [(24893, 24946)])

F1 = dn.rfs_image(F1, F9, "e1 24946", [(24893, 24946)])
# ------------ #

# ----out----- #
clip = dn.out(F1, epname)
clip.set_output()
# ------------ #

# ----save---- #
# dn.pw4(mrgc, 2, 1, epis, clip).set_output()
# epis.set_output()
# clip.std.Trim(0, 219).set_output()
# ------------ #

# ----err----- #
dn.check_num_frames(epis, clip)
# ------------ #
