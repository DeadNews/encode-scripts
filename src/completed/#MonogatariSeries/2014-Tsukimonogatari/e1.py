import dnfunc as dn

# -----in----- #
epname = dn.fname(__file__)
desc_h = 720

ED = 32608

epis = dn.source(f"./in/{epname}.mkv")
EDend = epis.num_frames - 36
# ------------ #

# ----mrgc---- #
ed = dn.oped(epis, name="ed1", offset=12, start=ED, end=EDend, desc_h=desc_h)

aaep = dn.aa(epis, desc_h=desc_h)

mrgc = aaep.std.Trim(0, ED - 1) + ed + aaep.std.Trim(EDend, epis.num_frames - 1)
# ------------ #

# ----mask---- #
hard_2 = dn.hard(aaep, mthr=2)
stabilize = dn.qtgmc(hard_2, ThSAD1=492, ThSAD2=197, ThSCD1=139, ThSCD2=75)
mrgc = dn.rfs(mrgc, stabilize, [(19677, 19712), (19861, 19900)])

mrgc = dn.rfs_hard(
    mrgc,
    mrgc,
    mthr=20,
    maps=[
        (10219, 10278),
        (15418, 15452),
        (20025, 20055),
        (16250, 16336),
        (16367, 16492),
        (16793, 16983),
        (13355, 13366),
        (13462, 13488),
        (12424, 12474),
    ],
)
mrgc = dn.rfs_hard(mrgc, mrgc, mthr=80, maps=[(19189, 19327), (20056, 20082), (20359, 20406)])

hard = dn.hard(mrgc, mthr=20)
mrgc = dn.rfs_image(mrgc, hard, "e1 18711", [(18711, 18755)])
mrgc = dn.rfs_image(mrgc, hard, "e1 18900", [(18900, 19040)])
mrgc = dn.rfs_image(mrgc, hard, "e1 19434", [(19434, 19496)])
mrgc = dn.rfs_image(mrgc, hard, "e1 19772", [(19772, 19807)])
mrgc = dn.rfs_image(mrgc, hard, "e1 12942", [(12942, 13034)])
mrgc = dn.rfs_image(
    mrgc,
    hard,
    "e1 12330",
    [(13384, 13431), (12330, 12423), (12616, 12711), (12733, 12870), (13489, 13617)],
)
mrgc = dn.rfs_image(
    mrgc,
    hard,
    "e1 50170",
    [
        (11954, 11986),
        (12119, 12261),
        (12294, 12329),
        (12475, 12579),
        (13745, 13825),
        (14034, 14225),
        (14429, 14477),
        (15008, 15232),
        (15548, 15631),
        (17324, 17401),
    ],
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
F2 = dn.filt(mrgc, sm_thr=30, db_thr=1)
F3 = dn.filt(mrgc, sm_thr=30, db_thr=1, rt_sigma=0.5)

F1 = dn.rfs(
    F1, F2, [(885, 1277), (1719, 2322), (2508, 2974), (3056, 3594), (3655, 3834), (3885, 3972)]
)
F1 = dn.rfs(F1, F3, [(18311, 18415)])
# ------------ #

# ----out----- #
clip = dn.out(F1, epname)
clip.set_output()
# ------------ #

# ----save---- #
# dn.pw4(mrgc, 2, 1, epis, clip).set_output()
# epis.set_output()
# clip.std.Trim(19861, 19900).set_output()

# dn.rfs_resc(mrgc, epis, desc_h=desc_h, mthr=50, out_mask=True).set_output()
# ------------ #

# ----err----- #
dn.check_num_frames(epis, clip)
# ------------ #
