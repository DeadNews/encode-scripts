import dnfunc as dn

# -----in----- #
epname = dn.fname(__file__)

OP = dn.chapt(epname, "OP")
OPend = dn.chapt(epname, "Part_A")
ED = dn.chapt(epname, "ED")
EDend = dn.chapt(epname, "Next")

epis = dn.source(f"./in/{epname}.mp4")
# ------------ #

# -----aa----- #
aaep = dn.aa(epis)
aaep = dn.aa(aaep, zone="eedi3")

mrgc = dn.rfs_dehalo(aaep)
mrgc = dn.rfs_dehalo(mrgc, zone="2nd")
# ------------ #

# ----mrgc---- #
mrgc = dn.rfs_qtgmc(mrgc, mrgc, maps=[(13023, 13221), (20587, 20833)])
# ------------ #

# ----mask---- #
eedi = dn.aa(epis, zone="eedi3")
mrgc = dn.rfs_resc(mrgc, eedi, maps=[(OP, OPend - 1), (ED, EDend - 1)])
# ------------ #

# ----filt---- #
F1 = dn.filt(mrgc)
# F1 = mrgc
# ------------ #

# ----out----- #
clip = dn.out(F1, epname)
clip.set_output()
# ------------ #

# ----save---- #
# dn.pw(mrgc, None, None, epis, clip).set_output()
# dn.pw(mrgc, [2, 3, 4, 6], 'main', epis, clip).set_output()
"""
1: aa 8467 34915
2: aa 16934 16946 26162 626 67288 69016 68966
2: db 24722 18674 3494 69666 42380
"""
# epis.set_output()
# dn.rfs_resc(epis=epis, out_mask=True).set_output()
# dn.rfs_dehalo(aaep, out_mask=True).set_output()
# clip.std.Trim(8373, 8573).set_output()
# ------------ #

# ----err----- #
dn.check_num_frames(epis, clip)
# ------------ #
