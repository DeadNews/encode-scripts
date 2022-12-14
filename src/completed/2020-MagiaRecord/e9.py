import dnfunc as dn

# -----in----- #
epname = dn.fname(__file__)

ED = dn.chapt(epname, "ED")

epis = dn.source(f"./in/{epname}.mp4")
# ------------ #

# ----mrgc---- #
mrgc = epis
# ------------ #

# ----filt---- #
F1 = dn.filt(mrgc)
F2 = dn.filt(mrgc, zone="harder")
F3 = dn.filt(mrgc, zone="harder_2")
F4 = dn.filt(mrgc, zone="harder_e9")

F1 = dn.rfs(F1, F2, [(5922, 6941)])
F1 = dn.rfs(F1, F3, [(ED + 308 - 24, ED + 448 - 24)])
F1 = dn.rfs(F1, F4, [(9805, 13350), (15554, 15928), (20471, 28375)])
# ------------ #

# ----out----- #
clip = dn.out(F1, epname)
clip.set_output()
# ------------ #

# ----save---- #
# dn.pw(mrgc, None, None, epis, clip).set_output()
# dn.pw(mrgc, [2, 3, 4, 6], 'main', epis, clip).set_output()
# dn.pw(mrgc, [2, 3, 4, 6], 'harder_e9', epis, clip).set_output()
"""
"""
# epis.set_output()
# clip.std.Trim(23455, 24082).set_output()
# ------------ #

# ----err----- #
dn.check_num_frames(epis, clip)
# ------------ #
