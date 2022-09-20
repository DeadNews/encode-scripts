import dnfunc as dn

# -----in----- #
epname = dn.fname(__file__)
desc_h = 720

OP = 3069
OPend = 5227
ED = 32608

epis = dn.source(f"./in/{epname}.mkv")
EDend = epis.num_frames - 36
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

stabilize = dn.qtgmc(aaep, ThSAD1=492, ThSAD2=197, ThSCD1=139, ThSCD2=75)
mrgc = dn.rfs_image(mrgc, stabilize, "e3 1394", "[1394 1591]")
mrgc = dn.rfs(mrgc, stabilize, "[28753 28980]")

hard_50 = dn.hard(mrgc, mthr=50)
mrgc = dn.rfs_image(mrgc, hard_50, "e3 8017", "[7652 8017] [9032 9342]")
hard = dn.hard(mrgc, mthr=20)
mrgc = dn.rfs_image(mrgc, hard, "e3 14094", "[14023 14094] [14513 14890]")
mrgc = dn.rfs_image(mrgc, hard, "e3 14227", "[14227 14271]")

mrgc = dn.rfs_hard(mrgc, mrgc, mthr=20, maps="[14340 14385]")

stabilize_2 = dn.qtgmc(aaep)
mrgc = dn.rfs_image(mrgc, stabilize_2, "op 749", f"[{OP+749} {OP+786}]")
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
F4 = dn.filt(mrgc, db_mode=2)

F1 = dn.rfs(F1, F2, f"[{OP-12+1510} {OP-12+1546}]")
F1 = dn.rfs(F1, F3, f"[{OP-12+373} {OP-12+760}]")
F1 = dn.rfs_image(F1, F2, "e3 26512", "[25363 25677] [25939 26037] [26476 26514] [26761 27000]")
F1 = dn.rfs_image(F1, F4, "e3 26512", "[27451 27612]")
# ------------ #

# ----out----- #
clip = dn.out(F1, epname)
clip.set_output()
# ------------ #

# ----save---- #
# dn.pw4(mrgc, 2, 1, epis, clip).set_output()
# epis.set_output()
# clip.std.Trim(1394, 1591).set_output()
# clip.std.Trim(28753, 28980).set_output()

# dn.rfs_resc(mrgc, epis, desc_h=desc_h, mthr=50, out_mask=True).set_output()
# ------------ #

# ----err----- #
dn.check_num_frames(epis, clip)
# ------------ #
