import dnfunc as dn

# -----in----- #
epname = dn.fname(__file__)
desc_h = 720

OP = 5395
OPend = 7553
ED = 32607

epis = dn.source(f"./in/{epname}.mkv")
EDend = epis.num_frames - 50
# ------------ #

# ----mrgc---- #
op = dn.oped(epis, name="op1", offset=12, start=OP, end=OPend, desc_h=desc_h)
ed = dn.oped(epis, name="ed1", offset=12, start=ED, end=EDend, desc_h=desc_h)

aaep = dn.aa(epis, desc_h=desc_h)

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
        (729, 860),
        (1056, 1082),
        (1107, 1214),
        (1386, 1466),
        (1491, 1580),
        (26540, 26852),
        (28389, 28472),
        (4879, 5212),
        (10679, 10900),
        (14249, 14371),
        (18080, 18349),
        (11159, 11194),
        (11323, 11430),
    ],
)
mrgc = dn.rfs_qtgmc(mrgc, aaep, k=2, maps=[(19811, 20155)])

stabilize = dn.qtgmc(mrgc)
mrgc = dn.rfs_image(mrgc, stabilize, "e2 378", [(378, 401)])
mrgc = dn.rfs_image(mrgc, stabilize, "e2 705", [(705, 728)])
mrgc = dn.rfs_image(mrgc, stabilize, "e2 7633", [(7633, 7668)])
mrgc = dn.rfs_image(mrgc, stabilize, "e2 12232", [(12232, 12255)])
mrgc = dn.rfs_image(mrgc, stabilize, "e2 21314", [(21314, 21349)])
mrgc = dn.rfs_image(mrgc, stabilize, "e2 28569", [(28569, 28604)])

mrgc = dn.rfs_hard(
    mrgc,
    mrgc,
    mthr=20,
    maps=[
        (1056, 1082),
        (1107, 1214),
        (1386, 1466),
        (1491, 1580),
        (2055, 2138),
        (2163, 2240),
        (3539, 3598),
        (3659, 3718),
        (4879, 5212),
        (11839, 11974),
        (13643, 13726),
        (16928, 16975),
        (16976, 16999),
        (21014, 21043),
        (26852, 27049),
        (11159, 11194),
        (24341, 24418),
        (17246, 17305),
        (17585, 17782),
        (18638, 18745),
        (18080, 18349),
        (10679, 10900),
        (20192, 20264),
        (11323, 11430),
    ],
)
mrgc = dn.rfs_hard(
    mrgc,
    mrgc,
    mthr=85,
    maps=[
        (729, 860),
        (12770, 12817),
        (17414, 17461),
        (17549, 17584),
        (18422, 18493),
        (18917, 18994),
        (28281, 28352),
    ],
)
mrgc = dn.rfs_hard(
    mrgc,
    mrgc,
    mthr=99,
    maps=[
        (3341, 3472),
        (4843, 4878),
        (8332, 10498),
        (11599, 11640),
        (13727, 13906),
        (14249, 14371),
        (14372, 14494),
        (14615, 14782),
        (14897, 15154),
        (16262, 16507),
        (18008, 18079),
        (18554, 18637),
        (21188, 21313),
        (21452, 21601),
        (21980, 22054),
        (22055, 22099),
        (22364, 22531),
        (22700, 22999),
        (23404, 23448),
        (24971, 25126),
        (28389, 28472),
        (10555, 10678),
        (10901, 11158),
        (11195, 11250),
        (13535, 13642),
        (26150, 26332),
        (3719, 3772),
    ],
)

hard_def = dn.hard(mrgc, mthr=20)
mrgc = dn.rfs_image(mrgc, hard_def, "e2 15452", [(15452, 15694)])
mrgc = dn.rfs_image(mrgc, hard_def, "e2 15791", [(15791, 15889)])
mrgc = dn.rfs_image(mrgc, hard_def, "e2 15890", [(15890, 15989)])
mrgc = dn.rfs_image(mrgc, hard_def, "e2 18746", [(18746, 18868)])
mrgc = dn.rfs_image(mrgc, hard_def, "e2 21044", [(21044, 21073)])
mrgc = dn.rfs_image(mrgc, hard_def, "e2 24227", [(24227, 24262)])
mrgc = dn.rfs_image(mrgc, hard_def, "e2 24803", [(24803, 24838)])
mrgc = dn.rfs_image(mrgc, hard_def, "e2 25754", [(25754, 26017)])
mrgc = dn.rfs_image(mrgc, hard_def, "e2 27212", [(27212, 27241)])
mrgc = dn.rfs_image(mrgc, hard_def, "e2 19487", [(19487, 19558)])
# on top of qtgmc
mrgc = dn.rfs_image(mrgc, hard_def, "e2 378", [(378, 401)])
mrgc = dn.rfs_image(mrgc, hard_def, "e2 705", [(705, 728)])
mrgc = dn.rfs_image(mrgc, hard_def, "e2 7633", [(7633, 7668)])
mrgc = dn.rfs_image(mrgc, hard_def, "e2 12232", [(12232, 12255)])
mrgc = dn.rfs_image(mrgc, hard_def, "e2 21314", [(21314, 21349)])
mrgc = dn.rfs_image(mrgc, hard_def, "e2 28569", [(28569, 28604)])

hard_desc = dn.hard(epis, desc_h=desc_h, mthr=10)
mrgc = dn.rfs_image(mrgc, hard_desc, "e2 13781", [(13781, 13906)])
mrgc = dn.rfs_image(mrgc, hard_desc, "e2 28497", [(28497, 28562)])
mrgc = dn.rfs_image(mrgc, hard_desc, "e2 5155", [(5155, 15217)])
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
F5 = dn.filt(mrgc, sm_thr=44, db_thr=1, rt_sigma=0.7)
F6 = dn.filt(mrgc, db_mode=1, db_thr=1.2)
F7 = dn.filt(mrgc, db_mode=2)
F8 = dn.filt(mrgc, db_thr=1, rt_sigma=0.8)

F1 = dn.rfs(F1, F2, [(OP, OP - 24 + 386), (OP - 24 + 451, OPend - 1)])
F1 = dn.rfs(F1, F3, [(OP - 24 + 387, OP - 24 + 450)])
F1 = dn.rfs(F1, F4, [(ED, EDend - 1 - 24), (4448, 4527)])
F1 = dn.rfs(F1, F5, [(20824, 20845)])
F1 = dn.rfs(
    F1,
    F6,
    [
        (1011, 1055),
        (1215, 1286),
        (1581, 1616),
        (1851, 1910),
        (2241, 2294),
        (20759, 20776),
        (21134, 21157),
        (24632, 24661),
        (27449, 27532),
    ],
)
F1 = dn.rfs(
    F1,
    F7,
    [(3965, 4012), (4369, 4369), (20708, 20725), (20876, 20929), (21188, 21235), (22562, 22663)],
)
F1 = dn.rfs(F1, F8, [(31730, 31777)])
# ------------ #

# ----out----- #
clip = dn.out(F1, epname)
clip.set_output()
# ------------ #

# ----save---- #
# dn.pw4(mrgc, 2, 1, epis, clip).set_output()
# epis.set_output()
# clip.std.Trim(11323, 11430).set_output()
# ------------ #

# ----err----- #
dn.check_num_frames(epis, clip)
# ------------ #
