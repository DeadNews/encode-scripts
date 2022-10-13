import dnfunc as dn

# -----in----- #
epname = dn.fname(__file__)

ED = dn.chapt(epname, "ED")

epis = dn.source(f"./in/{epname}.mp4")
# ------------ #

# ----mrgc---- #
mrgc = epis
# ------------ #

# ----mrgc---- #
crop = mrgc.std.Crop(top=132, bottom=132)
edgefixe = crop.edgefixer.Continuity(top=1, bottom=1)
borders = edgefixe.std.AddBorders(top=132, bottom=132)
mrgc = dn.rfs(mrgc, borders, [(0, 2905)])
# ------------ #

# ----filt---- #
F1 = dn.filt(mrgc)
F2 = dn.filt(mrgc, zone="harder")
F3 = dn.filt(mrgc, zone="harder_2")

F1 = dn.rfs(F1, F2, [(21916, 23859), (20638, 21741)])
F1 = dn.rfs(F1, F3, [(ED + 308 - 24, ED + 448 - 24)])
# ------------ #

# ----out----- #
clip = dn.out(F1, epname)
clip.set_output()
# ------------ #

# ----save---- #
# dn.pw(mrgc, None, None, epis, clip).set_output()
# dn.pw(mrgc, [2, 3, 4, 6], 'main', epis, clip).set_output()
"""
"""
# epis.set_output()
# ------------ #

# ----err----- #
dn.check_num_frames(epis, clip)
# ------------ #
