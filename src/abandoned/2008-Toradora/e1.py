import dnfunc as dn

# -----in----- #
epname = dn.fname(__file__)

epis = dn.source(f"./in/{epname}.mp4")
# ------------ #

# ----fix----- #
epis = dn.to444(epis, mode="Lanczos")
epis, _crop = dn.crop(epis)
epis, epis_back, edgefixer = dn.edgefix(epis)
# ------------ #

# ----mrgc---- #
aaep = dn.aa(epis)
mrgc = aaep

mrgc = dn.rfs_dehalo(mrgc)

mrgc_back = mrgc
mrgc = dn.qtgmc(mrgc, k=0.6, sharp=0.1)  # <<<
mrgc = dn.rfs_qtgmc(mrgc, mrgc_back, k=2, sharp=0.0, maps="[1089 1215]")
# ------------ #

# ----filt---- #
F1 = dn.filt(mrgc)
# ------------ #

# ----out----- #
clip = dn.out(F1, epname)
# clip.set_output()
dn.downscale(clip, 720, to420=True).set_output()
# ------------ #

# ----save---- #
# dn.pw(mrgc, None, None, epis_back, clip).set_output()
# dn.pw(mrgc, [2, 3, 4, 6], 'main', epis, clip).set_output()
"""
2: 5348 13672 17492 17778 18642 19794 20082 20946 21810 64028 65468 66044 25842 26418
1: 8906
8: 123150
"""
# epis.set_output()
# dn.downscale(clip, 720, to420=True).std.Trim(0, 1500).set_output()
# dn.rfs_dehalo(aaep, zone='main', out_mask=True).set_output()
# dn.rfs_resc(epis=epis, mthr=28, out_mask=True).set_output()
# ------------ #

# ----err----- #
dn.check_num_frames(epis, clip)
# ------------ #
