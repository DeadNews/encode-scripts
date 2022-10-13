import dnfunc as dn

# -----in----- #
epname = dn.fname(__file__)
desc_h = 720

OP = 0
Part_A = 864
Part_B = 16784
Next = 33928

epis = dn.source(f"./in/{epname}.mkv")
# ------------ #

# ----mrgc---- #
aaep = dn.aa(epis, desc_h=desc_h)
mrgc = aaep
# ------------ #

# ----mask---- #
mrgc = dn.rfs_resc(mrgc, epis, desc_h=desc_h, mthr=40, maps=[(27987, 28193)])
mrgc = dn.rfs_resc(mrgc, epis, desc_h=desc_h, mthr=66, maps=[(770, 863)])
mrgc = dn.rfs_resc(mrgc, epis, desc_h=desc_h, mthr=17, maps=[(880, 998)])
mrgc = dn.rfs_resc(mrgc, epis, desc_h=desc_h, mthr=58, maps=[(28470, 30013)])

mrgc = dn.rfs_hard(
    mrgc,
    epis,
    desc_h=desc_h,
    mthr=99,
    maps=[
        (10301, 10469),
        (11468, 11905),
        (12044, 12044),
        (12290, 12418),
        (13076, 13135),
        (13412, 13525),
        (14015, 14278),
        (14309, 14512),
        (15524, 15625),
        (15767, 16051),
        (23780, 23977),
        (24152, 24351),
        (9242, 10124),
        (8188, 8508),
        (8545, 9004),
        (9182, 9241),
        (10718, 10837),
        (11906, 12043),
    ],
)

stabilize = dn.qtgmc(aaep, k=0.77)
mrgc = dn.rfs(mrgc, stabilize, [(8545, 8652)])
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
F2 = dn.filt(mrgc, sm_thr=50, db_mode=3)
F0 = dn.filt(mrgc, db_thr=0)

F1 = dn.rfs(F1, F2, [(26800, 27384)])
F1 = dn.rfs(F1, F0, [(0, 292)])
# ------------ #

# ----out----- #
clip = dn.out(F1, epname)
clip.set_output()
# ------------ #

# ----save---- #
# dn.pw4(mrgc, 2, 1, epis, clip).set_output()
# epis.set_output()
# clip.std.Trim(8545, 8652).set_output()

# dn.rfs_resc(mrgc, epis, desc_h=desc_h, mthr=50, out_mask=True).set_output()
# ------------ #

# ----err----- #
dn.check_num_frames(epis, clip)
# ------------ #
