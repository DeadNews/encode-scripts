import dnfunc as dn

# -----in----- #
epname = dn.fname(__file__)
desc_h = 720

epis = dn.source(f"./in/{epname}.mkv")
# ------------ #

# ----mrgc---- #
aaep = dn.aa(epis, desc_h=desc_h)
mrgc = aaep
# ------------ #

# ----mask---- #
# mrgc = dn.rfs_hard(mrgc, epis, mthr=99, sangnomPP=False, yuv=False, maps="[26123 26181]")
# mrgc = dn.rfs_image(mrgc, epis_ef, maskname="1", maps="[2040 2230]")
mrgc = dn.rfs_resc(
    mrgc,
    epis,
    desc_h=desc_h,
    kernel="bicubic",
    mthr=50,
    maps="[10001 10050] [10132 10233] [10306 10323] [10448 10493] [10679 10846] [10877 10987] [11183 11362] [11751 11905]",
)
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
F2 = dn.filt(mrgc, sm_thr=30, db_thr=1)

F1 = dn.rfs(F1, F2, "[3829 3891]")
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
