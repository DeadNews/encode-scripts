import dnfunc as dn

# -----in----- #
epname = dn.fname(__file__)

OP = dn.chapt(epname, "OP")
OPend = dn.chapt(epname, "Part_A")
ED = dn.chapt(epname, "ED")
EDend = dn.chapt(epname, "Next")

epis = dn.source(f"./in/{epname}.mp4")
# ------------ #

# ----mrgc---- #
aaep = dn.aa(epis)
op = dn.oped(epis, name="op", offset=24, start=OP, end=OPend)
ed = dn.oped(epis, name="ed", offset=24, start=ED, end=EDend)

mrgc = (
    aaep.std.Trim(0, OP - 1)
    + op
    + aaep.std.Trim(OPend, ED - 1)
    + ed
    + epis.std.Trim(EDend, epis.num_frames - 1)
)
# ------------ #

# ----mask---- #
mrgc = dn.rfs_dehalo(mrgc)
mrgc = dn.rfs_qtgmc(mrgc, mrgc, k=2, maps=f"[{ED} {ED+173}]")
# ------------ #

# ----filt---- #
F1 = dn.filt(mrgc)
F2 = dn.filt(mrgc, zone="oped")
F3 = dn.filt(mrgc, zone="limb")
F4 = dn.filt(mrgc, zone="noise")

F1 = dn.rfs(F1, F2, f"[{OP} {OPend-1}] [{ED} {EDend-1}]")
F1 = dn.rfs(F1, F3, f"[{OP+1092} {OP+1280}]")
F1 = dn.rfs(F1, F4, "[14549 15256] [15295 15806]")
# ------------ #

# ----out----- #
clip = dn.out(F1, epname)
clip.set_output()
# ------------ #

# ----save---- #
# dn.pw(mrgc, [1, 2, 3, 4, 6], 'main', epis, clip, 'old').set_output()
"""
"""
# epis.set_output()
# clip2 = clip.std.Trim(14549, 15256) + clip.std.Trim(15295, 15806)
# clip2.set_output()
# ------------ #

# ----err----- #
dn.check_num_frames(epis, clip)
# ------------ #