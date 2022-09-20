import dnfunc as dn

# -----in----- #
epname = dn.fname(__file__)
desc_h = 720

OP = 36
OPend = 2182
Part_B = 13499
# ED = 31712
# EDend = 33950

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
mrgc = dn.rfs_resc(mrgc, epis, desc_h=desc_h, mthr=36, maps="[13030 13127] [33831 33949]")
mrgc = dn.rfs_resc(
    mrgc, epis, desc_h=desc_h, mthr=65, maps="[31841 32353] [32561 32929] [33071 33769]"
)
mrgc = dn.rfs_image(mrgc, epis, "e5 01", "[31628 31711]")

mrgc = dn.rfs_hard(
    mrgc,
    epis,
    desc_h=desc_h,
    mthr=99,
    maps="[16318 16902] [17122 17493] [17818 18189] [18463 18954] [19909 20029] [21181 21360] [21565 21660] [21944 22327] [22502 22645] [19513 19722] [19759 19842]",
)

stabilize = dn.qtgmc(aaep, k=0.77)
mrgc = dn.rfs(mrgc, stabilize, "[18028 18189] [17188 17493]")
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
