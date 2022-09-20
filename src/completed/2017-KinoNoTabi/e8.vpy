import dnfunc as dn

# -----in----- #
epname = dn.fname(__file__)
desc_h = 720

Avant = 0
OP = 888
OPend = 3045
Part_B = 17047
# ED = 31720
# EDend = 33927

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
mrgc = dn.rfs_resc(mrgc, epis, desc_h=desc_h, mthr=32, maps="[24650 24797]")
mrgc = dn.rfs_resc(mrgc, epis, desc_h=desc_h, mthr=50, maps="[26773 26849] [3469 3643]")
mrgc = dn.rfs_resc(mrgc, epis, desc_h=desc_h, mthr=70, maps="[31825 33192]")

hard = dn.hard(mrgc, mthr=2)
mrgc = dn.rfs_image(mrgc, hard, "e8 01", "[17417 17590]")
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
