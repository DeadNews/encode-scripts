import dnfunc as dn

# -----in----- #
epname = dn.fname(__file__)
desc_h = 720

# epis = dn.source(f'./in/{epname}.mp4')
# ------------ #

# -----aa----- #
# if Path(f"./temp/{epname}_aa_lossless.mp4").is_file():
#     aaep = dn.source(f"./temp/{epname}_aa_lossless.mp4")
# else:
#    aaep = dn.aa(epis, desc_h=desc_h)
#
# mrgc = aaep
# ------------ #

# -----aa----- #
epis = dn.source(f"./in/e5.mp4")

ED = 33986
EDend = 36564

ed = dn.oped(epis, name="ed_e5", offset=12, start=ED, end=EDend, desc_h=desc_h)
mrgc = ed
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
# ------------ #

# ----out----- #
clip = dn.out(F1, epname, fpsnum=24000, fpsden=1001)
clip.set_output()
# ------------ #

# ----save---- #
# dn.pw4(mrgc, 2, 1, epis, clip).set_output()
# epis.set_output()
# clip.std.Trim(0, 3000).set_output()
# ------------ #

# ----err----- #
dn.check_num_frames(epis, clip)
# ------------ #
