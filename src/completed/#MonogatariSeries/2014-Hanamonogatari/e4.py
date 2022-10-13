import dnfunc as dn

# -----in----- #
epname = dn.fname(__file__)
desc_h = 720

OP = 4915
OPend = 7074
ED = 34241

epis = dn.source(f"./in/{epname}.mkv")
EDend = epis.num_frames - 39
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
    maps=[
        (OP - 12 + 1341, OP - 12 + 1372),
        (OP - 12 + 1400, OP - 12 + 1425),
        (OP - 12 + 1453, OP - 12 + 1476),
    ],
)

mrgc = dn.rfs_hard(mrgc, mrgc, mthr=20, maps=[(26153, 26215)])

hard = dn.hard(mrgc, mthr=20)
mrgc = dn.rfs_image(mrgc, hard, "e4 4303", [(4303, 4470)])
mrgc = dn.rfs_image(mrgc, hard, "e4 16887", [(16887, 16946)])
mrgc = dn.rfs_image(mrgc, hard, "e4 16983", [(16983, 17168)])
mrgc = dn.rfs_image(mrgc, hard, "e4 17447", [(17447, 17510), (17742, 17789)])
mrgc = dn.rfs_image(mrgc, hard, "e4 26537", [(26537, 26725)])
mrgc = dn.rfs_image(mrgc, hard, "e4 26819", [(26819, 26872)])
mrgc = dn.rfs_image(mrgc, hard, "e4 29756", [(29756, 29815), (30197, 30628), (32393, 32428)])
# hard_70 = dn.hard(mrgc, mthr=70)
# mrgc = dn.rfs_image(mrgc, hard_70, 'e4 30173', [(30173, 30196), (30677, 30718), (31226, 31363)])
mrgc = dn.rfs_image(mrgc, hard, "e4 32363", [(32363, 32392)])

stabilize = dn.qtgmc(mrgc)
mrgc = dn.rfs_image(mrgc, stabilize, "op 749", [(OP + 749, OP + 786)])
mrgc = dn.rfs_image(mrgc, stabilize, "e4 30628", [(29756, 29815), (30197, 30628), (32393, 32410)])
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
F4 = dn.filt(mrgc, db_saveblack=0, sm_thr=35)
F5 = dn.filt(mrgc, sm_thr=35, db_thr=1)

F1 = dn.rfs(F1, F2, [(OP - 12 + 1510, OP - 12 + 1546)])
F1 = dn.rfs(F1, F3, [(OP - 12 + 373, OP - 12 + 760)])
F1 = dn.rfs(F1, F4, [(22601, 22642)])
F1 = dn.rfs(F1, F5, [(22727, 23146), (28535, 29074)])
# ------------ #

# ----out----- #
clip = dn.out(F1, epname)
clip.set_output()
# ------------ #

# ----save---- #
# dn.pw4(mrgc, 2, 1, epis, clip).set_output()
# epis.set_output()
# clip.std.Trim(29756, 29815).set_output()

# dn.rfs_resc(mrgc, epis, desc_h=desc_h, mthr=50, out_mask=True).set_output()
# ------------ #

# ----err----- #
dn.check_num_frames(epis, clip)
# ------------ #
