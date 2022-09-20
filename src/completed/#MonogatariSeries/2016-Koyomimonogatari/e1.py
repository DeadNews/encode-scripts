import dnfunc as dn

# -----in----- #
epname = dn.fname(__file__)
desc_h = 720

OP = 34
OPend = 2184
ED = 17576

epis = dn.source(f"./in/{epname}.mkv")
EDend = epis.num_frames - 12
# ------------ #

# ----mrgc---- #
op = dn.oped(epis, name="op1", offset=22, start=OP, end=OPend, desc_h=desc_h)
ed = dn.oped(epis, name="ed1", offset=12, start=ED, end=EDend, desc_h=desc_h)

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
mrgc = dn.rfs(mrgc, aaep, "[300 463] [738 901]")
mrgc = dn.rfs_resc(mrgc, epis, desc_h=desc_h, mthr=50, maps="[339 449] [898 901]")

mrgc = dn.rfs_hard(
    mrgc,
    mrgc,
    mthr=20,
    maps="[2814 2897] [2928 3119] [3216 3377] [3498 3690] [11225 11404] [11619 11948] [12306 12410] [13860 14027] [14064 14195] [14505 14752] [14948 15031] [15104 15253]",
)

hard = dn.hard(mrgc, mthr=2, yuv=False)
mrgc = dn.rfs_image(mrgc, hard, "e1 4008", "[3937 4008]")
# ------------ #

# -----in----- #
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
F2 = dn.filt(mrgc, sm_thr=45, db_thr=1, rt_sigma=0.8)

F1 = dn.rfs(F1, F2, "[12616 12816]")
# ------------ #

# ----out----- #
clip = dn.out(F1, epname)
clip.set_output()
# ------------ #

# ----save---- #
# dn.pw4(mrgc, 2, 1, epis, clip).set_output()
# epis.set_output()
# clip.std.Trim(0, 3000).set_output()

# dn.rfs_resc(mrgc, epis, desc_h=desc_h, mthr=50, out_mask=True).set_output()
# ------------ #

# ----err----- #
dn.check_num_frames(epis, clip)
# ------------ #
