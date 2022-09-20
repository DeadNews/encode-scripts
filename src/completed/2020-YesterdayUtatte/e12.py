import dnfunc as dn

# -----in----- #
epname = dn.fname(__file__)

Part_A = dn.chapt(epname, "Part_A")
Part_B = dn.chapt(epname, "Part_B")
End = dn.chapt(epname, "EDend")

epis = dn.source(f"./in/{epname}.mp4")
# ------------ #

# ----mrgc---- #
aaep = dn.aa(epis)
mrgc = aaep
# ------------ #

# ----mask---- #
eedi = dn.aa(epis, zone="eedi3")
mrgc = dn.rfs(mrgc, eedi, f"[{Part_B} {Part_B+71}]")

mrgc = dn.rfs_dehalo(mrgc)

mrgc = dn.rfs_resc(mrgc, epis, maps=f"[{Part_A} {Part_A+143}]")  # title

mrgc = dn.rfs_resc(mrgc, epis, mthr=110, maps=f"[29778 {End-1}]")  # ed
# ------------ #

# ----filt---- #
F1 = dn.filt(mrgc)
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
