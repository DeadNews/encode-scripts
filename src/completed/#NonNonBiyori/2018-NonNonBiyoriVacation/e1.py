import dnfunc as dn

# -----in----- #
epname = dn.fname(__file__)

Avant = dn.chapt(epname, "Avant")
Part_1 = dn.chapt(epname, "Part_1")
ED = dn.chapt(epname, "ED")

epis = dn.source(f"./in/{epname}.mp4")
# ------------ #

# ----mrgc---- #
aaep = dn.aa(epis)
mrgc = dn.rfs_dehalo(aaep)
mrgc = dn.rfs_resc(mrgc, epis)
# ------------ #

# ----mask---- #
mrgc = dn.rfs(mrgc, epis, [(Avant, Part_1 - 1), (ED, epis.num_frames - 1)])
# ------------ #

# ----filt---- #
F1 = dn.filt(mrgc)
F2 = dn.filt(mrgc, zone="dark")

F1 = dn.rfs(
    F1,
    F2,
    [
        (25613, 25707),
        (35250, 35415),
        (35947, 35987),
        (36047, 39762),
        (42004, 42074),
        (42662, 42679),
        (42989, 43658),
        (79503, 84746),
    ],
)
# ------------ #

# ----out----- #
clip = dn.out(F1, epname)
clip.set_output()
# ------------ #

# ----save---- #
# dn.pw(mrgc, None, None, epis, clip).set_output()
# dn.pw(mrgc, [2, 3, 4, 6], 'main', epis, clip).set_output()
# dn.pw(mrgc, [2, 3, 4, 6], 'main', epis, clip, ext_rip=rip).set_output()
# dn.pw(mrgc, [2, 3, 4, 6], 'dark', epis, clip).set_output()
# dn.pw(mrgc, [2, 3, 4, 6], 'dark', epis, clip, ext_rip=rip).set_output()
"""
1: 3999 75903
2: 35318 99316 76196 151806 26502
6: aa 79504 102532 53368
6: db 153790 144382 252256 477028
7: 256204 260306 300423 302250 305211 577595
7: 321164 189417
"""
# epis.set_output()
# dn.rfs_resc(epis=epis, mthr=35, resc_bc=True, out_mask=True).set_output()
# ------------ #

# ----err----- #
dn.check_num_frames(epis, clip)
# ------------ #
