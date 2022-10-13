import dnfunc as dn

# -----in----- #
epname = dn.fname(__file__)
desc_h = 720

Avant = 0
OP = 4916
OPend = 7074
Part_B = 16761
ED = 30881
EDend = 33954

epis = dn.source(f"./in/{epname}.mkv")
# ------------ #

# ----mrgc---- #
aaep = dn.aa(epis, desc_h=desc_h)
# mrgc =  aaep

op = dn.oped(epis, name="op2", offset=24, start=OP, end=OPend, desc_h=desc_h)
ed = epis.std.Trim(ED, EDend - 1)

mrgc = (
    aaep.std.Trim(0, OP - 1)
    + op
    + aaep.std.Trim(OPend, ED - 1)
    + ed
    + aaep.std.Trim(EDend, epis.num_frames - 1)
)
# ------------ #

# ----mask---- #
mrgc = dn.rfs_resc(mrgc, epis, desc_h=desc_h, mthr=70, maps=[(31256, 31794)])
mrgc = dn.rfs_resc(mrgc, epis, desc_h=desc_h, mthr=88, maps=[(22837, 22929)])
mrgc = dn.rfs_resc(mrgc, epis, desc_h=desc_h, mthr=50, maps=[(25836, 25932), (90, 203)])
mrgc = dn.rfs_resc(mrgc, epis, desc_h=desc_h, mthr=65, maps=[(7077, 7169)])

mrgc = dn.rfs_hard(mrgc, mrgc, mthr=45, yuv=True, maps=[(20254, 2038)])
mrgc = dn.rfs_hard(mrgc, mrgc, mthr=95, maps=[(7386, 7559)])
mrgc = dn.rfs_hard(mrgc, epis, desc_h=desc_h, mthr=95, maps=[(17558, 17832)])
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

F1 = dn.rfs(F1, F2, [(OP, OPend - 1), (29486, 29896)])
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
