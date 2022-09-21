import dnfunc as dn

# -----in----- #
epname = dn.fname(__file__)
desc_h = 720

OP = 5635
OPend = 7795
ED = 36927

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
mrgc = dn.rfs_hard(
    mrgc,
    mrgc,
    mthr=30,
    maps=f"[{OP-12+1341} {OP-12+1372}] [{OP-12+1400} {OP-12+1425}] [{OP-12+1453} {OP-12+1476}]",
)

stabilize = dn.qtgmc(aaep)
mrgc = dn.rfs_image(mrgc, stabilize, "op 749", f"[{OP+749} {OP+786}] [26475 26879]")

mrgc = dn.rfs_qtgmc(mrgc, aaep, k=2, maps="[27144 27260] [26964 27065] [27333 27570]")

mrgc = dn.rfs_hard(
    mrgc,
    mrgc,
    mthr=20,
    maps="[26964 27065] [26475 26879] [30080 30115] [28419 28442] [28986 29015] [29340 29441]",
)

hard = dn.hard(mrgc, mthr=20)
mrgc = dn.rfs_image(mrgc, hard, "e1 14399", "[14399 14523]")
mrgc = dn.rfs_image(mrgc, hard, "e1 17678", "[17657 17687]")
mrgc = dn.rfs_image(mrgc, hard, "e1 27600", "[27600 27647]")
mrgc = dn.rfs_image(mrgc, hard, "e1 27833", "[27804 27833]")
mrgc = dn.rfs_image(mrgc, hard, "e1 30140", "[30140 30211]")
mrgc = dn.rfs_image(mrgc, hard, "e1 27333", "[27333 27570]")
mrgc = dn.rfs_image(mrgc, hard, "e1 10682", "[10682 10725]")
mrgc = dn.rfs_image(
    mrgc,
    hard,
    "e1 9321",
    "[8607 8669] [10399 10513] [10643 10681] [9321 9506] [10828 10989] [11018 11344]",
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
F2 = dn.filt(mrgc, db_mode=1)
F3 = dn.filt(mrgc, rt_sigma=0.8)

F1 = dn.rfs(F1, F2, f"[{OP-12+1510} {OP-12+1546}] [12359 12484]")
F1 = dn.rfs(F1, F3, f"[{OP-12+373} {OP-12+760}]")
# ------------ #

# ----out----- #
clip = dn.out(F1, epname)
clip.set_output()
# ------------ #

# ----save---- #
# dn.pw4(mrgc, 2, 1, epis, clip).set_output()
# epis.set_output()
# clip.std.Trim(26475, 27833).set_output()
# clip.std.Trim(27144, 27260).set_output()
# clip.std.Trim(26964, 27065).set_output()

# dn.rfs_resc(mrgc, epis, desc_h=desc_h, mthr=50, out_mask=True).set_output()
# ------------ #

# ----err----- #
dn.check_num_frames(epis, clip)
# ------------ #
