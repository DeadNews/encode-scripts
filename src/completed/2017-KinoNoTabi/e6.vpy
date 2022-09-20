import dnfunc as dn

# -----in----- #
epname = dn.fname(__file__)
desc_h = 720

Avant = 0
OP = 1032
OPend = 3189
Part_B = 19421
# ED = 31768
# EDend = 33926

epis = dn.source(f"./in/{epname}.mkv")
# ------------ #

# ----mrgc---- #
aaep = dn.aa(epis, desc_h=desc_h)
# mrgc =  aaep

op = dn.oped(epis, name="op2", offset=24, start=OP, end=OPend, desc_h=desc_h)
# ed = epis.std.Trim(ED, EDend-1)

mrgc = aaep.std.Trim(0, OP - 1) + op + aaep.std.Trim(OPend, epis.num_frames - 1)
# ------------ #

# ----mask---- #
mrgc = dn.rfs_resc(mrgc, epis, desc_h=desc_h, mthr=25, maps="[25 143] [254 39] [31672 31767]")
mrgc = dn.rfs_resc(mrgc, epis, desc_h=desc_h, mthr=90, maps="[32023 33697]")

mrgc = dn.rfs_image(mrgc, epis, "e6 01", "[31777 31896]")
mrgc = dn.rfs_image(mrgc, epis, "e6 02", "[31941 32016]")
mrgc = dn.rfs_image(mrgc, epis, "e6 03", "[18311 18406]")

mrgc = dn.rfs_hard(
    mrgc, epis, desc_h=desc_h, mthr=20, yuv=True, maps="[19025 19036] [19073 19090] [19127 19144]"
)
mrgc = dn.rfs_hard(
    mrgc,
    epis,
    desc_h=desc_h,
    mthr=80,
    maps="[22097 22234] [23014 24703] [26337 26432] [26565 26660] [27705 28060]",
)

hard = dn.hard(epis, desc_h=desc_h, mthr=80)
mrgc = dn.rfs_image(mrgc, hard, "e6 04", "[26565 26660] [27705 28060]")
# ------------ #

# ----filt---- #
"""
def filt_old(
    mrgc=mrgc,
    sm_thr=100,
    tr=48,
    pref=1,
    cs_mode=99,
    cs_val=0.5,
    db_thr=2.1,
    db_mode=2,
    db_det=64,
    db_grain=52,
    db_range=15,
    db_saveblack=0,
    rt_sigma=1,
    out_mode=0,
):
"""

F1 = dn.filt(mrgc)
F2 = dn.filt(mrgc, sm_thr=80, db_mode=3)

F1 = dn.rfs(F1, F2, f"[{OP} {OPend-1}]")
# ------------ #

# ----out----- #
clip = dn.out(F1, epname)
clip.set_output()
# ------------ #

# ----save---- #
# dn.pw4(mrgc, 2, 1, epis, clip).set_output()
# epis.set_output()
# clip.std.Trim(14918, 15266).set_output()

# dn.rfs_resc(mrgc, epis, desc_h=desc_h, mthr=50, out_mask=True).set_output()
# ------------ #

# ----err----- #
dn.check_num_frames(epis, clip)
# ------------ #
