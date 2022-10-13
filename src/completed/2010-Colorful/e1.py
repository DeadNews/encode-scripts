import dnfunc as dn

# -----in----- #
epname = dn.fname(__file__)

Chapter_11 = 69110
Chapter_12 = 80444
ED = 175896

epis = dn.source(f"./in/{epname}.mp4")
# ------------ #

# ----mrgc---- #
epis_back = epis
epis = epis.edgefixer.Continuity(top=1, bottom=1, left=1, right=1)

aaep = dn.aa(epis)
aaep = dn.rfs_dehalo(aaep)
mrgc = dn.rfs(aaep, epis_back, [(0, 265), (ED, epis.num_frames - 1)])
# ------------ #

# ----filt---- #
F1 = dn.filt(mrgc)
F2 = dn.filt(mrgc, zone="rain")
F3 = dn.filt(mrgc, zone="noise_1")
F4 = dn.filt(mrgc, zone="noise_2")
F5 = dn.filt(mrgc, zone="avant")

F1 = dn.rfs(F1, F2, [(Chapter_11, Chapter_12 - 1)])
F1 = dn.rfs(F1, F3, [(161625, 163451), (163651, 164215)])
F1 = dn.rfs(F1, F4, [(163452, 163650), (164216, 164982)])
F1 = dn.rfs(F1, F5, [(540, 5117)])
# ------------ #

# ----out----- #
clip = dn.out(F1, epname)
clip.set_output()
# ------------ #

# ----save---- #
# dn.pw(mrgc, [1, 2, 3, 4, 5, 6], 'main', epis_back, clip).set_output()
# dn.pw(mrgc, [2, 3, 4, 5, 6], 'rain', epis_back, clip, 'main').set_output()
# dn.pw(mrgc, [2, 3, 4, 5, 6], 'noise_2', epis_back, clip, 'main').set_output()
# dn.pw(mrgc, [2, 3, 4, 5, 6], 'avant', epis_back, clip, 'main').set_output()
"""
aa 847054 848014 848974 253702
db 219318 220278 597542 1301949 9917
"""
# epis.set_output()
# clip.std.Trim(161625, 164215).set_output()
# ------------ #

# ----err----- #
dn.check_num_frames(epis, clip)
# ------------ #
