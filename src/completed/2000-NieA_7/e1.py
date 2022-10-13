import dnfunc as dn

# -----in----- #
epname = dn.fname(__file__)

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

epis = dn.rfs(
    epis,
    epis_back,
    [(ED, epis.num_frames - 1), (6499, 6584), (5336, 5981), (7940, 8565), (7113, 7223)],
)
epis = dn.rfs(epis, fix, [(10384, 10388), (4022, 4116)])
# ------------ #

# ----mrgc---- #
aaep = dn.aa(epis)
mrgc = aaep

mrgc = dn.rfs_dehalo(mrgc)
mrgc = dn.rfs_dehalo(mrgc, zone="2nd")
mrgc = dn.rfs_dehalo(mrgc, zone="3nd")

mrgc = dn.qtgmc(mrgc, k=1.0, sharp=0.0)  # <<<
# ------------ #

# ----filt---- #
F1 = dn.filt(mrgc)
F2 = dn.filt(mrgc, zone="ed")
F3 = dn.filt(mrgc, zone="next")

F1 = dn.rfs(F1, F2, [(ED, EDend - 1)])
F1 = dn.rfs(F1, F3, [(Next, epis.num_frames - 1)])
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
aa 74390 1446 17286 50798 72938
db 109350
ha 117330 38330 38814 62382 42174 18234  125858 133058
qt 10410*4 8506
---
co 18234 29332 12323 9612 4286 18532 4579 11848
"""
# epis.set_output()
# clip.std.Trim(0, 1500).set_output()
# dn.rfs_dehalo(aaep, zone='main', out_mask=True).set_output()
# ------------ #

# ----err----- #
dn.check_num_frames(epis, clip)
# ------------ #
