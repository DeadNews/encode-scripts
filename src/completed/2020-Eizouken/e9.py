import dnfunc as dn

# -----in----- #
epname = dn.fname(__file__)

OP = dn.chapt(epname, "OP")
OPend = dn.chapt(epname, "Part_A")
ED = dn.chapt(epname, "ED")
EDend = dn.chapt(epname, "EDend")

epis = dn.source(f"./in/{epname}.mp4")
# ------------ #

# ----mrgc---- #
aaep = dn.aa(epis, zone="eedi3")  # 1080
mrgc = aaep
# ------------ #

# ----mask---- #
mrgc = dn.rfs_dehalo(mrgc)

mrgc = dn.rfs(mrgc, epis, f"[{OP} {OPend-1}] [{ED} {EDend-1}]")  # op ed

mrgc = dn.rfs_repair(mrgc, maps=f"[{ED+724} {ED+2133}]")  # ed repair
# ------------ #

# ----filt---- #
F1 = dn.filt(mrgc)
F2 = dn.filt(mrgc, zone="op")
F3 = dn.filt(mrgc, zone="ed")
F4 = dn.filt(mrgc, zone="ed_grain")

F1 = dn.rfs(F1, F2, f"[{OP} {OPend-1}]")
F1 = dn.rfs(F1, F3, f"[{ED} {EDend-1}]")
F1 = dn.rfs(F1, F4, f"[{ED} {ED+251}]  [{ED+724} {ED+1538}]  [{ED+1886} {ED+2133}]")
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
