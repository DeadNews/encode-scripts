import dnfunc as dn

# -----in----- #
epname = dn.fname(__file__)
desc_h = 720

OP = 0
OPend = 2169
ED = 31420

epis = dn.source(f"./in/{epname}.mkv")
EDend = epis.num_frames - 34
# ------------ #

# ----mrgc---- #
op = dn.oped(epis, name="op3", offset=0, start=OP, end=OPend, desc_h=desc_h)
ed = dn.oped(epis, name="ed3", offset=12, start=ED, end=EDend, desc_h=desc_h)

aaep = dn.aa(epis, desc_h=desc_h)

mrgc = op + aaep.std.Trim(OPend, ED - 1) + ed + aaep.std.Trim(EDend, epis.num_frames - 1)
# ------------ #

# ----mask---- #
mrgc = dn.rfs_hard(mrgc, mrgc, mthr=80, maps="[15895 15959] [16103 16162] [16325 16372]")
mrgc = dn.rfs_hard(mrgc, mrgc, mthr=20, maps="[16217 16252] [16758 16793]")

hard = dn.hard(mrgc, mthr=20)
mrgc = dn.rfs_image(mrgc, hard, "e6 9332", "[9332 9367]")
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

F1 = dn.rfs(F1, F2, f"[{ED} {ED+112}] [10416 10565]")
F1 = dn.rfs(F1, F3, f"[{OP} {OPend-1}]")
# ------------ #

# ----out----- #
clip = dn.out(F1, epname)
clip.set_output()
# ------------ #

# ----save---- #
# dn.pw4(mrgc, 2, 1, epis, clip).set_output()
# epis.set_output()
# clip.std.Trim(30000, 32800).set_output()

# dn.rfs_resc(mrgc, epis, desc_h=desc_h, mthr=50, out_mask=True).set_output()
# ------------ #

# ----err----- #
dn.check_num_frames(epis, clip)
# ------------ #
