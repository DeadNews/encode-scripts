import dnfunc as dn

# -----in----- #
epname = dn.fname(__file__)
desc_h = 720

OP = 24
OPend = 2181
ED = 15962

epis = dn.source(f"./in/{epname}.mkv")
EDend = epis.num_frames - 14
# ------------ #


def filt_ncop_aa(ncoped_aa):
    stabilize = dn.qtgmc(ncoped_aa, k=0.77)
    return dn.rfs(ncoped_aa, stabilize, [(12, 221), (1167, 1408), (1730, 1760), (1783, 1901)])


# ----mrgc---- #
op = dn.oped(epis, name="op4", offset=12, start=OP, end=OPend, desc_h=desc_h, filtred=filt_ncop_aa)
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
mrgc = dn.rfs(mrgc, aaep, [(292, 310), (1984, 2180)])
mrgc = dn.rfs_image(mrgc, epis, f"{epname} 2151", [(2103, 2180)])

stabilize = dn.qtgmc(aaep, ThSAD1=492, ThSAD2=197, ThSCD1=139, ThSCD2=75)
mrgc = dn.rfs(mrgc, stabilize, [(15467, 15883)])

hard = dn.hard(mrgc, mthr=30)
mrgc = dn.rfs_image(mrgc, hard, "e4 15467", [(15467, 15883)])
mrgc = dn.rfs_image(mrgc, hard, "e4 8763", [(8763, 8822)])
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
F2 = dn.filt(mrgc, db_mode=2)

F1 = dn.rfs(F1, F2, [(7667, 7729)])
# ------------ #

# ----out----- #
clip = dn.out(F1, epname)
clip.set_output()
# ------------ #

# ----save---- #
# dn.pw4(mrgc, 2, 1, epis, clip).set_output()
# epis.set_output()
# clip.std.Trim(15467, 15883).set_output()
# clip.std.Trim(0, 2181).set_output()
# clip.std.Trim(0, 245).set_output()

# dn.rfs_resc(mrgc, epis, desc_h=desc_h, mthr=50, out_mask=True).set_output()
# ------------ #

# ----err----- #
dn.check_num_frames(epis, clip)
# ------------ #
