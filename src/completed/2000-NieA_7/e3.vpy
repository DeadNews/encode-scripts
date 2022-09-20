import dnfunc as dn

# -----in----- #
epname = dn.fname(__file__)

OP = dn.chapt(epname, "OP")
OPend = dn.chapt(epname, "Part_A")
ED = dn.chapt(epname, "ED")
EDend = dn.chapt(epname, "Next", "EDend")
Next = dn.chapt(epname, "Next")

epis = dn.source(f"./in/{epname}.mp4")
# ------------ #

# ----fix----- #
epis, _crop = dn.crop(epis)
epis, epis_back, edgefixer = dn.edgefix(epis)

fix = dn.chromashift(epis, cx=2.5, cy=0)
epis = dn.adaptive_chromashift(epis, fix, pw_mode=False)

epis = dn.rfs(epis, epis_back, f"[{ED} {epis.num_frames-1}] [{OP} {OPend-1}] [15371 15478]")
epis = dn.rfs(epis, fix, "[29630 29964]")
# ------------ #

# ----mrgc---- #
aaep = dn.aa(epis)
mrgc = aaep

mrgc = dn.rfs_dehalo(mrgc)
mrgc = dn.rfs_dehalo(mrgc, zone="2nd")
mrgc = dn.rfs_dehalo(mrgc, zone="3nd")

mrgc = dn.qtgmc(mrgc, k=1.0, sharp=0.0)
# ------------ #

# ----filt---- #
F1 = dn.filt(mrgc)
F2 = dn.filt(mrgc, zone="ed")
F3 = dn.filt(mrgc, zone="next")
F4 = dn.filt(mrgc, zone="op")

F1 = dn.rfs(F1, F2, f"[{ED} {EDend-1}]")
F1 = dn.rfs(F1, F3, f"[{Next} {epis.num_frames-1}]")
F1 = dn.rfs(F1, F4, f"[{OP} {OPend-1}]")
# ------------ #

# ----out----- #
clip = dn.out(F1, epname)
# clip.set_output()
clip.resize.Spline36(960, 720).set_output()
# ------------ #

# ----save---- #
# dn.pw(mrgc, [3, 4], 'main', epis, clip).set_output()
# dn.pw(mrgc, [1, 2, 3, 4, 5, 6], 'main', epis, clip).set_output()
"""
"""
# epis.set_output()
# dn.rfs_dehalo(aaep, zone='main', out_mask=True).set_output()
# ------------ #

# ----err----- #
dn.check_num_frames(epis, clip)
# ------------ #
