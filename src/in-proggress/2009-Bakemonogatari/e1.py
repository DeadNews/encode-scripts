import dnfunc as dn

# -----in----- #
epname = dn.fname(__file__)

OP = dn.chapt(epname, "OP")
OPend = dn.chapt(epname, "Part_A")
ED = dn.chapt(epname, "ED")
EDend = dn.chapt(epname, "Next", "EDend")

epis = dn.source(f"./in/{epname}.mp4")
# ------------ #

# ----mrgc---- #
aaep = dn.aa(epis)
mrgc = aaep
# ------------ #

# ----mask---- #
mrgc = dn.rfs_black_crop(mrgc, top=142, bot=144, maps=[(0, 2205), (OP, OPend - 1)])

# save timer (e1)
timer_mask = dn.gradfun_mask(aaep, thr_det=2.1, mode=3).fmtc.bitdepth(bits=8)
save_timer = dn.masked_merge(mrgc, aaep, db_mode=timer_mask, yuv=True)
mrgc = dn.rfs_image(mrgc, save_timer, "e1_timer", [(0, 591)], yuv=True)
# ------------ #

# ----filt---- #
F1 = dn.filt(mrgc)
# ------------ #

# ----out----- #
clip = dn.out(F1, epname)
clip.set_output()

# return what is not the noise on the mask to black
# ------------ #

# ----save---- #
# dn.pw(mrgc, None, None, epis, clip).set_output()
# dn.pw(mrgc, [2, 3, 4, 6], 'main', epis, clip).set_output()
"""
2: 5676 33644 53414
"""
# epis.set_output()
# clip.std.Trim(0, 1).set_output()
# dn.rfs_resc(epis=epis, mthr=48, out_mask=True).set_output()
# ------------ #

# ----err----- #
dn.check_num_frames(epis, clip)
# ------------ #
