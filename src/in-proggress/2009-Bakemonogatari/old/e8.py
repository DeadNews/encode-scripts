import dnfunc as dn

# -----in----- #
epname = dn.fname(__file__)
desc_h = 720

OP = 6978
OPend = 9134
ED = 32224
EDend = 34404

epis = dn.source(f"./in/{epname}.mp4")
# ------------ #


def filt_ncop_aa(ncoped_aa):
    stabilize = dn.qtgmc(ncoped_aa, k=0.77)
    return dn.rfs(ncoped_aa, stabilize, [(12, 221), (1167, 1408), (1730, 1760), (1783, 1901)])


# ----mrgc---- #
aaep = dn.aa(epis, desc_h=desc_h)
op = dn.oped(
    aaep,
    name="op3",
    offset=12,
    start=OP,
    end=OPend,
    desc_h=desc_h,
    filtr=filt_ncop_aa,
    inputAA=True,
)
ed = dn.oped(epis, name="ed_e8", offset=0, start=ED, end=EDend, desc_h=desc_h)

mrgc = (
    aaep.std.Trim(0, OP - 1)
    + op
    + aaep.std.Trim(OPend, ED - 1)
    + ed
    + aaep.std.Trim(EDend, epis.num_frames - 1)
)
# ------------ #

# ----mask---- #
mrgc = dn.rfs(mrgc, epis, [(35292, epis.num_frames - 1)])

fixed_black = mrgc.std.CropRel(top=142, bottom=144).std.AddBorders(top=142, bottom=144)
mrgc = dn.rfs(mrgc, fixed_black, [(0, OP - 1)])

# it is possible to do the opposite: in a series without credits, and credits separately
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
# ------------ #

# ----out----- #
clip = dn.out(F1, epname)
clip.set_output()
# ------------ #

# ----save---- #
# dn.pw4(mrgc, 2, 1, epis, clip).set_output()
# epis.set_output()
# clip.std.Trim(22062, 22237).set_output()
# ------------ #

# ----err----- #
dn.check_num_frames(epis, clip)
# ------------ #
