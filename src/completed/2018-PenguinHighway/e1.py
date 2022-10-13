import dnfunc as dn

# -----in----- #
epname = dn.fname(__file__)

Chap2 = 6394
ED = 162790

epis = dn.source(f"./in/{epname}.mkv")
epis = epis.std.CropRel(top=104, bottom=104)

# -----ef----- #
epis_ef = epis.edgefixer.Continuity(top=2, bottom=2, left=2, right=2)

aaep = dn.aa(epis_ef, desc_h=862)  # 872
mrgc = aaep
# ------------ #

# ----mask---- #
mrgc = dn.rfs_hard(mrgc, mrgc, mthr=85, maps=[(4094, 4213), (132773, 132868)])
mrgc = dn.rfs_hard(
    mrgc,
    mrgc,
    mthr=99,
    maps=[(2931, 3092), (6694, 6861), (18375, 18440), (20865, 20936), (139050, 139105)],
)

hard = dn.hard(mrgc, mthr=50)
mrgc = dn.rfs_image(mrgc, hard, "2198", [(2140, 2198)])
mrgc = dn.rfs_image(mrgc, hard, "11489", [(11489, 11572), (15189, 15284)])
mrgc = dn.rfs_image(mrgc, hard, "161049", [(161013, 161074)])

epis_ef = dn.rfs_image(epis_ef, aaep, "4094", [(4094, 4213)])
# ------------ #

# ----filt---- #

"""
def filt_old(
    mrgc=mrgc,
    sm_thr=100,
    tr=16,
    pref=1,
    cs_mode=99,
    cs_val=0.53,
    db_thr=2.5,
    db_mode=1,
    db_det=64,
    db_grain=52,
    db_range=15,
    db_saveblack=2,
    rt_sigma=0.9,
    out_mode=0,
):
"""

F0 = dn.filt(epis, db_thr=0)

F1 = dn.filt(mrgc)
F2 = dn.filt(mrgc, mrgc=epis_ef)
F3 = dn.filt(mrgc, db_grain=88)
F4 = dn.filt(mrgc, db_grain=62)
F5 = dn.filt(mrgc, db_thr=1.0)
F6 = dn.filt(mrgc, db_thr=1.0, sm_thr=80)

F1 = dn.rfs(F1, F0, [(ED, epis.num_frames - 1)])
F1 = dn.rfs(F1, F2, [(3758, Chap2 - 1)])
F1 = dn.rfs(F1, F3, [(69527, 71363)])
F1 = dn.rfs(F1, F4, [(71364, 74363)])
F1 = dn.rfs(F1, F5, [(47198, 48243)])
F1 = dn.rfs(F1, F6, [(138870, 141104), (141297, 141488), (155253, 155681)])
# ------------ #

# ----out----- #
clip = dn.out(F1, epname)
clip.set_output()
# ------------ #

# ----save---- #
# dn.pw4(mrgc, 2, 1, epis, clip).set_output()
# epis.set_output()
# clip.std.Trim(ED, epis.num_frames-1).set_output()
# ------------ #

# ----err----- #
dn.check_num_frames(epis, clip)
# ------------ #
