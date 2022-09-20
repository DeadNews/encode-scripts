import dnfunc as dn

# -----in----- #
epname = dn.fname(__file__)

epis = dn.source(f"./in/{epname}.mp4")
epis, epis_back, edgefixer = dn.edgefix(epis)
# ------------ #

# ----mrgc---- #
mrgc = epis
mrgc = dn.rfs_repair(mrgc)
mrgc = dn.rfs_dehalo(mrgc)
mrgc = dn.rfs_linedark(mrgc)

mrgc_back = mrgc
mrgc = dn._rescale(mrgc, mode="insaneAA", width=1920, height=1080)

mrgc = dn.rfs_qtgmc(mrgc, mrgc, k=0.6, maps="[0 63]")
# ------------ #

# ----filt---- #
F1 = dn.filt(mrgc)
# ------------ #

# ----out----- #
clip = dn.out(F1, epname)
clip.set_output()
dn.downscale(clip, 576).set_output()
# ------------ #

# ----save---- #
# core.std.Interleave([epis_back, mrgc_back]).set_output()
# dn.pw(mrgc, [2, 3, 4, 6], 'main', mrgc, clip).set_output()
"""
1: 1678
2: 1678 1972 3356 3988 3914 2202
6: 10 2596 158332 76696
"""
# epis.set_output()
# dn.downscale(clip, 576).std.Trim(0, 500).set_output()
# dn.rfs_dehalo(aaep, zone='main', out_mask=True).set_output()
# ------------ #

# ----err----- #
dn.check_num_frames(epis, clip)
# ------------ #
