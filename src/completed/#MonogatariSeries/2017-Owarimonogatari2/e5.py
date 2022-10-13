import dnfunc as dn

# -----in----- #
epname = dn.fname(__file__)
desc_h = 720

OP = 2614
OPend = 4771
ED = 32129

epis = dn.source(f"./in/{epname}.mkv")
EDend = epis.num_frames - 24
# ------------ #

# ----mrgc---- #
op = dn.oped(epis, name="op3", offset=12, start=OP, end=OPend, desc_h=desc_h)
ed = dn.oped(epis, name="ed3", offset=12, start=ED, end=EDend, desc_h=desc_h)

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
stabilize = dn.qtgmc(aaep)
mrgc = dn.rfs_image(
    mrgc,
    stabilize,
    "e5 000",
    [
        (10671, 10760),
        (11049, 11249),
        (11904, 12138),
        (12532, 12662),
        (16459, 16655),
        (16776, 16922),
        (17364, 17573),
        (17703, 17863),
        (18026, 18139),
        (18890, 19127),
        (20481, 20642),
        (20883, 20996),
        (27839, 28012),
        (28145, 28402),
        (29399, 29656),
        (30161, 30448),
        (30509, 30814),
    ],
)

hard = dn.hard(mrgc, mthr=20)
mrgc = dn.rfs_image(mrgc, hard, "e5 000", [(10890, 10940), (18494, 18565), (20412, 20444)])
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
F2 = dn.filt(mrgc, db_mode=1)
F3 = dn.filt(mrgc, db_mode=2)
F4 = dn.filt(mrgc, sm_thr=60, db_mode=2)

F1 = dn.rfs(F1, F2, [(ED, ED + 112), (12337, 12483), (29909, 29968)])
F1 = dn.rfs(F1, F3, [(OP, OPend - 1), (6177, 6224)])
F1 = dn.rfs(F1, F4, [(6511, 6643), (6672, 6869), (7129, 7236), (7479, 7506), (7561, 7738)])
# ------------ #

# ----out----- #
clip = dn.out(F1, epname)
clip.set_output()
# ------------ #

# ----save---- #
# dn.pw4(mrgc, 2, 1, epis, clip).set_output()
# epis.set_output()
# clip.std.Trim(17364, 17573).set_output()
# clip.std.Trim(28145, 28402).set_output()
# clip.std.Trim(6177, 6224).set_output()

# dn.rfs_resc(mrgc, epis, desc_h=desc_h, mthr=50, out_mask=True).set_output()
# ------------ #

# ----err----- #
dn.check_num_frames(epis, clip)
# ------------ #
