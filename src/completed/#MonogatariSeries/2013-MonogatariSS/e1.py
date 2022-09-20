import dnfunc as dn

# -----in----- #
epname = dn.fname(__file__)
desc_h = 720

OP = 1966
OPend = 4125
ED = 32611
EDend = 34768

epis = dn.source(f"./in/{epname}.mkv")
# ------------ #


def filt_ncop_aa(ncoped_aa):
    return dn.rfs_hard(ncoped_aa, ncoped_aa, mthr=99, maps="[1391 1463] [1608 1635]")


# ----mrgc---- #
aaep = dn.aa(epis, desc_h=desc_h)
op = dn.oped(epis, name="op1", offset=12, start=OP, end=OPend, desc_h=desc_h, filtred=filt_ncop_aa)
ed = dn.oped(epis, name="ed1", offset=0, start=ED, end=EDend, desc_h=desc_h)

mrgc = (
    aaep.std.Trim(0, OP - 1)
    + op
    + aaep.std.Trim(OPend, ED - 1)
    + ed
    + aaep.std.Trim(EDend, epis.num_frames - 1)
)
# ------------ #

# ----mask---- #
mrgc = dn.rfs(mrgc, aaep, f"[{OP+644} {OP+856}]")

mrgc = dn.rfs_hard(mrgc, mrgc, mthr=95, maps="[10162 10235] [16887 16928]")
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
F2 = dn.filt(mrgc, sm_thr=45, db_thr=1, rt_sigma=0.7)
F3 = dn.filt(mrgc, rt_sigma=0.8)
F4 = dn.filt(mrgc, sm_thr=300, db_thr=6, db_mode=1, rt_sigma=4, db_det=128)
F5 = dn.filt(mrgc, sm_thr=44, db_thr=1, rt_sigma=0.7)

F1 = dn.rfs(F1, F2, "[16479 16796] [17174 17552] [20935 21405]")
F1 = dn.rfs(F1, F3, "[17880 18029] [18085 18194] [24375 24482]")
F1 = dn.rfs(F1, F5, "[23997 24044]")

F1 = dn.rfs_image(F1, F4, "e1 14820", "[14820 14855]")
F1 = dn.rfs_image(F1, F4, "e1 17328", "[17328 17387]")
F1 = dn.rfs_image(F1, F4, "e1 19829", "[19829 19894]")
F1 = dn.rfs_image(F1, F4, "e1 20003", "[20003 20356] [20513 20638] [21418 21562]")
F1 = dn.rfs_image(F1, F4, "e1 20777", "[20777 20902]")
F1 = dn.rfs_image(F1, F4, "e1 21963", "[21963 22130]")
# ------------ #

# ----out----- #
clip = dn.out(F1, epname)
clip.set_output()
# ------------ #

# ----save---- #
# dn.pw4(mrgc, 2, 1, epis, clip).set_output()
# epis.set_output()
# clip.std.Trim(0, 30).set_output()

# dn.rfs_resc(mrgc, epis, desc_h=desc_h, mthr=50, out_mask=True).set_output()
# ------------ #

# ----err----- #
dn.check_num_frames(epis, clip)
# ------------ #
