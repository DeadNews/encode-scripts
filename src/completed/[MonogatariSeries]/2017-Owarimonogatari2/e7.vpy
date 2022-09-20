import dnfunc as dn

# -----in----- #
epname = dn.fname(__file__)
desc_h = 720

OP = 7288
OPend = 9445

epis = dn.source(f"./in/{epname}.mkv")
# ------------ #

# ----mrgc---- #
op = dn.oped(epis, name="op3", offset=12, start=OP, end=OPend, desc_h=desc_h)

aaep = dn.aa(epis, desc_h=desc_h)

mrgc = aaep.std.Trim(0, OP - 1) + op + aaep.std.Trim(OPend, epis.num_frames - 1)
# ------------ #

# ----mask---- #
aa_titles = dn.aa(epis, desc_h=900)
mrgc = dn.rfs(mrgc, aa_titles, "[33806 34921]")
mrgc = dn.rfs_resc(mrgc, epis, desc_h=desc_h, mthr=99, maps="[33806 34921]")

stabilize = dn.qtgmc(aaep)
mrgc = dn.rfs(mrgc, stabilize, "[3090 3173] [3216 3251] [4623 4781] [6326 6591]")

mrgc = dn.rfs_hard(mrgc, mrgc, mthr=50, maps="[4461 4592] [32483 32542]")
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
F2 = dn.filt(mrgc, db_mode=2)
F3 = dn.filt(mrgc, db_mode=1)

F1 = dn.rfs(
    F1,
    F2,
    f"[{OP} {OPend-1}] [10355 10390] [14751 14765] [14895 14918] [14933 14962] [14985 15209] [16806 16883] [17133 17270] [28945 29055]",
)
F1 = dn.rfs(
    F1, F3, "[5176 5478] [13911 13934] [10313 10354] [14679 14708] [22207 22293] [28142 28165]"
)

# ----out--- #

clip = dn.out(F1, epname)
clip.set_output()
# ------------ #

# ----save---- #
# dn.pw4(mrgc, 2, 1, epis, clip).set_output()
# epis.set_output()
# clip.std.Trim(3090, 3251).set_output()
# clip.std.Trim(6326, 6640).set_output()
# clip.std.Trim(33263, epis.num_frames-1).set_output()

# dn.rfs_resc(mrgc, epis, desc_h=desc_h, mthr=99, out_mask=True).set_output()
# ------------ #

# ----err----- #
dn.check_num_frames(epis, clip)
# ------------ #
