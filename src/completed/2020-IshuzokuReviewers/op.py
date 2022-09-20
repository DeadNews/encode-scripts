import dnfunc as dn

# -----in----- #
epname = dn.fname(__file__)

epis = dn.source(f"./in/{epname}.mp4")
# ------------ #

# -----aa----- #
aaep = dn.aa(epis, epname)
mrgc = aaep
# ------------ #

# ----mask---- #
mrgc = dn.rfs_dehalo(mrgc)

OP = 0
mrgc = dn.rfs_resc(mrgc, epis, mthr=50, maps=f"[{OP+1486} {OP+1508}] [{OP+2084} {OP+2159}]")
mrgc = dn.rfs_hard(mrgc, mrgc, mthr=99, maps=f"[{OP+2101} {OP+2159}]")  # op_end
# ------------ #

# ----filt---- #
F1 = dn.filt(mrgc, zone="oped")
# ------------ #

# ----out----- #
clip = dn.out(F1, epname)
clip.set_output()
# ------------ #

# ----save---- #
# dn.pw(mrgc, None, None, epis, clip).set_output()
# epis.set_output()
# ------------ #

# ----err----- #
dn.check_num_frames(epis, clip)
# ------------ #
