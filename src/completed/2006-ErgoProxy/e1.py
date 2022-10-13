import dnfunc as dn

# -----in----- #
epname = dn.fname(__file__)

ED = dn.chapt(epname, "ED")
EDend = dn.chapt(epname, "Next", "EDend")

jpn = dn.source(f"./in/{epname}.mp4")
ita = dn.source(f"./in/2nd/{epname}.mp4")
epis = dn.average([jpn, ita])

epis, epis_back, edgefixer = dn.edgefix(epis)
# ------------ #

# ----mrgc---- #
aaep = dn.aa(epis)
mrgc = dn.rfs_image(aaep, epis, "ef")  # fix bot
# ------------ #

# ----mask---- #
mrgc = dn.rfs(mrgc, epis_back, [(ED, EDend - 1)])  # ed
mrgc = dn.rfs_repair(mrgc, maps=[(ED, EDend - 1)])  # ed repair

mrgc = dn.rfs_resc(mrgc, epis, mthr=50, maps=[(1395, 4173)])  # op titles (1-2)
# ------------ #

# ----filt---- #
F1 = dn.filt(mrgc)
F2 = dn.filt(mrgc, zone="ed")

F1 = dn.rfs(F1, F2, [(ED, EDend - 1)])
# ------------ #

# ----out----- #
clip = dn.out(F1, epname)
clip.set_output()
# ------------ #

# ----save---- #
# dn.pw(mrgc, None, None, epis_back, clip).set_output()
# dn.pw(mrgc, [2, 3, 4, 6], 'main', epis_back, clip).set_output()
# dn.pw(mrgc, [2, 3, 6], 'main', epis_back, clip, ext_rip=rip).set_output()
"""
6: 142456 143320 164416 61270   179032 179662! 10612!
2: 17620 1856 15876 22500 59886! 7530 2696 3536!
1: 2696
"""
# epis.set_output()
# dn.rfs_resc(epis=epis, mthr=50, out_mask=True).set_output()
# dn.rfs_repair(mrgc, out_mask=True).set_output()
# ------------ #

# ----err----- #
dn.check_num_frames(epis, clip)
# ------------ #
