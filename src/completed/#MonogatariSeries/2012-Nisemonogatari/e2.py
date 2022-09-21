import dnfunc as dn

# -----in----- #
epname = dn.fname(__file__)
desc_h = 720

ED = 32609
EDend = 34766

epis = dn.source(f"./in/{epname}.mkv")
# ------------ #

# ----mrgc---- #
ed = dn.oped(epis, name="ed2", offset=12, start=ED, end=EDend, desc_h=desc_h)

aaep = dn.aa(epis, desc_h=desc_h)

mrgc = aaep.std.Trim(0, ED - 1) + ed + aaep.std.Trim(EDend, epis.num_frames - 1)
# ------------ #

# ----mask---- #
mrgc = dn.rfs_hard(mrgc, mrgc, mthr=20, maps="[28158 28217] [30405 30437]")

mrgc = dn.rfs_qtgmc(mrgc, aaep, maps="[15800 15853] [16006 16091]")

hard = dn.hard(mrgc, mthr=20)
mrgc = dn.rfs_image(mrgc, hard, "e2 25706", "[25706 25768] [26270 26353] [26735 26917]")
mrgc = dn.rfs_image(mrgc, hard, "e2 26489", "[26489 26626]")

stabilize = dn.qtgmc(mrgc, k=0.77)
mrgc = dn.rfs_image(mrgc, stabilize, "e2 26270", "[25706 25768] [26270 26353] [26735 26917]")
mrgc = dn.rfs_image(mrgc, stabilize, "e2 26489", "[26489 26626]")
mrgc = dn.rfs_image(mrgc, stabilize, "e2 28689", "[28689 28766] [28979 29058]")
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
F3 = dn.filt(mrgc, db_mode=2)

F1 = dn.rfs(
    F1,
    F2,
    "[1129 1194] [1424 1465] [12409 12475] [12623 12718] [14287 14370] [15872 16005] [28641 28670] [29406 29420] [29430 29451] [32477 32529]",
)
F1 = dn.rfs(
    F1,
    F3,
    "[1791 1820] [12297 12378] [13003 13068] [15161 15328] [22506 22614] [25907 26239] [26969 27155] [28512 28595] [29521 29646] [30615 30665] [31610 31621]",
)
# ------------ #

# ----out----- #
clip = dn.out(F1, epname)
clip.set_output()
# ------------ #

# ----save---- #
# dn.pw4(mrgc, 2, 1, epis, clip).set_output()
# epis.set_output()
# clip.std.Trim(26489, 26626).set_output()
# output = clip[25706:25768] + clip[26489:26626] + clip[28689:28766]; output.set_output()

# dn.rfs_resc(mrgc, epis, desc_h=desc_h, mthr=50, out_mask=True).set_output()
# ------------ #

# ----err----- #
dn.check_num_frames(epis, clip)
# ------------ #
