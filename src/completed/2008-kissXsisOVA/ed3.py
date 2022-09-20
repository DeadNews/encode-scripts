import dnfunc as dn

# -----in----- #
epname = dn.fname(__file__)

epis = dn.source(f"./in/{epname}.mp4")
epis, epis_back, edgefixer = dn.edgefix(epis)
# ------------ #

# -----aa----- #
aaep = dn.aa(epis, epname, zone="hi")
mrgc = aaep

mrgc = dn.rfs_dehalo(mrgc)
# ------------ #

# ----filt---- #
F1 = dn.filt(mrgc, sm_thr=140, dn_pref=1, db_adaptive=False)
# ------------ #

# ----out----- #
clip = dn.out(F1, epname)
clip.set_output()
# ------------ #

# ----save---- #
# dn.pw4(mrgc, 2, 1, epis_back, clip).set_output()
"""
3250 4210
"""
# epis.set_output()
# ------------ #

# ----err----- #
dn.check_num_frames(epis, clip)
# ------------ #
