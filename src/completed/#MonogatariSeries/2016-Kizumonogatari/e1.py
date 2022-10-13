import dnfunc as dn

# -----in----- #
epname = dn.fname(__file__)
desc_h = 544

ED = 84360

epis = dn.source(f"./in/{epname}.mkv")
epis = epis.std.CropRel(top=132, bottom=132)
# ------------ #

# ----mrgc---- #
epis_ef = epis.edgefixer.Continuity(top=2, bottom=2)
aaep = dn.aa(epis_ef, desc_h=desc_h)

mrgc = aaep
# ------------ #

# ----mask---- #
mrgc = dn.rfs_hard(mrgc, mrgc, mthr=50, maps=[(25592, 25731)])

mrgc = dn.rfs_qtgmc(mrgc, aaep, k=0.77, maps=[(17132, 17203), (21080, 21235)])

stabilize = dn.qtgmc(aaep)
mrgc = dn.rfs_image(mrgc, stabilize, "e1 83515", [(83234, 83515)])
mrgc = dn.rfs_image(mrgc, stabilize, "e1 84083", [(83844, 84083)])
mrgc = dn.rfs_image(mrgc, stabilize, "e1 56391", [(56391, 56816)])
mrgc = dn.rfs_image(mrgc, stabilize, "e1 57091", [(57091, 57208)])
mrgc = dn.rfs_image(mrgc, stabilize, "e1 51798", [(51798, 51911)])
# ------------ #

# ----filt---- #
"""
def filt_old(
    mrgc=mrgc,
    sm_thr=60,
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
    rt_sigma=0.8,
    out_mode=0,
):
"""

F0 = dn.filt(epis, db_thr=0)

F1 = dn.filt(mrgc)
F2 = dn.filt(mrgc, sm_thr=38, db_thr=1, rt_sigma=0.7, cs_val=0.50)
F3 = dn.filt(mrgc, db_saveblack=0, db_mode=1)

F1 = dn.rfs(F1, F0, [(ED, 90187), (90703, epis.num_frames - 1)])
F1 = dn.rfs(
    F1,
    F2,
    [
        (14298, 14333),
        (14469, 14534),
        (14534, 14711),
        (14904, 14975),
        (13554, 13631),
        (37102, 37362),
    ],
)
F1 = dn.rfs(F1, F3, [(67791, 67827), (68558, 68590)])
# ------------ #

# ----out----- #
clip = dn.out(F1, epname)
clip.set_output()
# ------------ #

# ----save---- #
# epis.set_output()
# dn.pw4(mrgc, 2, 1, epis, clip).set_output()

# clip.std.Trim(64031, 67091).set_output()
# clip.std.Trim(37930, 40330).set_output()
# clip.std.Trim(ED, epis.num_frames-1).set_output()
# clip.std.Trim(17132, 17203).set_output()
# clip.std.Trim(83234, 83515).set_output()
# clip.std.Trim(83844, 84083).set_output()
# clip.std.Trim(37102, 37362).set_output()
# clip.std.Trim(56391, 56816).set_output()
# ------------ #

# ----err----- #
dn.check_num_frames(epis, clip)
# ------------ #
