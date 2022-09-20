import dnfunc as dn

# -----in----- #
epname = dn.fname(__file__)

OP = dn.chapt(epname, "OP")
OPend = dn.chapt(epname, "Part_A")
ED = dn.chapt(epname, "ED")
EDend = dn.chapt(epname, "End") - 24

epis = dn.source(f"./in/{epname}.mp4")
# ------------ #

# ----mrgc---- #
aaep = dn.aa(epis)
op = dn.oped(epis, name="op", offset=0, start=OP, end=OPend)
ed = dn.oped(epis, name="ed", offset=48, start=ED, end=EDend)

mrgc = op + aaep.std.Trim(OPend, ED - 1) + ed + epis.std.Trim(EDend, epis.num_frames - 1)
# ------------ #

# ----mask---- #
mrgc = dn.rfs_dehalo(mrgc)
mrgc = dn.rfs_image(mrgc, epis, f"{epname}", "[3764 3858]")
mrgc = dn.rfs_qtgmc(mrgc, mrgc, k=2, maps=f"[{ED} {ED+179}]")
# ------------ #

# ----filt---- #
F1 = dn.filt(mrgc)
F2 = dn.filt(mrgc, zone="oped")

F1 = dn.rfs(F1, F2, f"[{OP} {OPend-1}] [{ED} {EDend-1}]")
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
# ------------ #

# ----err----- #
dn.check_num_frames(epis, clip)
# ------------ #
