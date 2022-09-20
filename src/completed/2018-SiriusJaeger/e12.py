import dnfunc as dn

# -----in----- #
epname = dn.fname(__file__)

Part_A = dn.chapt(epname, "Part_A")
Part_B = dn.chapt(epname, "Part_B")
ED = dn.chapt(epname, "ED")
End = dn.chapt(epname, "End")

map_ed = f"[{ED+376} {End-1}]"
map_title = f"[{Part_A-96} {Part_A-1}]"
map_mid = f"[{Part_B-48} {Part_B-1}]"
map_avant = f"[0 {Part_A-97}]"

epis = dn.source(f"./in/{epname}.mp4")
epis, epis_back, edgefixer = dn.edgefix(epis)
# ------------ #

# ----mrgc---- #
aaep = dn.aa(epis)
aaep = dn.rfs_dehalo(aaep)
mrgc = aaep
# ------------ #

# ----mask---- #
mrgc = dn.rfs(mrgc, epis_back, map_ed)  # ed (castom2)
mrgc = dn.rfs(mrgc, epis, map_title)
mrgc = dn.rfs(mrgc, epis, map_mid)

mrgc = dn.rfs_resc(mrgc, epis, mthr=150, maps=map_avant, zone="resc_fix")  # avatn
# ------------ #

# ----filt---- #
F1 = dn.filt(mrgc)
F2 = dn.filt(mrgc, db_saveblack=2)  # ed (castom2)
F4 = dn.filt(mrgc, zone="title")

F1 = dn.rfs(F1, F2, map_ed)
F1 = dn.rfs(F1, F4, map_title)
# ------------ #

# ----out----- #
clip = dn.out(F1, epname)
clip.set_output()
# ------------ #

# ----save---- #
# dn.pw4(mrgc, 2, 1, epis_back, clip).set_output()
# dn.pw8(mrgc, 4, 7, 2, 5, 6, epis_back, clip, 0, zone='main').set_output()
"""
"""
# epis.set_output()
# clip.std.Trim(Next, epis.num_frames-1).set_output()
# clip.std.Trim(ED, EDend-1).set_output()

# dn.rfs_resc(epis=epis, mthr=150, out_db_mode=True, zone='resc_fix').set_output()  # 816
# dn.rfs_dehalo(aaep, zone='main', out_mask=True).set_output()
# dn.planes(clip)[2].set_output()
# ------------ #

# ----err----- #
dn.check_num_frames(epis, clip)
# ------------ #
