import dnfunc as dn

# -----in----- #
epname = dn.fname(__file__)

Part_A = dn.chapt(epname, "Part_A")
Part_B = dn.chapt(epname, "Part_B")
ED = dn.chapt(epname, "ED")
EDend = dn.chapt(epname, "Part_C", "Next")
Next = dn.chapt(epname, "Next")
End = dn.chapt(epname, "End")

map_ed = [(ED, EDend - 1)]
map_next = [(Next, End - 1)]
map_title = [(Next - 96, Next - 1)]
map_mid = [(Part_B - 48, Part_B - 1)]

epis = dn.source(f"./in/{epname}.mp4")
epis, epis_back, edgefixer = dn.edgefix(epis)
# ------------ #

# ----mrgc---- #
aaep = dn.aa(epis)
aaep = dn.rfs_dehalo(aaep)
ed = dn.oped(epis_back, name="ed", offset=0, start=ED, end=EDend)

mrgc = aaep.std.Trim(0, ED - 1) + ed + aaep.std.Trim(EDend, epis.num_frames - 1)
# ------------ #

# ----mask---- #
mrgc = dn.rfs(mrgc, epis, map_next)
mrgc = dn.rfs(mrgc, epis, map_title)
mrgc = dn.rfs(mrgc, epis, map_mid)

mrgc = dn.rfs_resc(mrgc, epis, mthr=150, maps=[(0, 2020)], zone="resc_fix")  # avatn
# ------------ #

# ----filt---- #
F1 = dn.filt(mrgc)
F2 = dn.filt(mrgc, zone="ed")
F3 = dn.filt(mrgc, zone="next")
F4 = dn.filt(mrgc, zone="title")

F1 = dn.rfs(F1, F2, map_ed)
F1 = dn.rfs(F1, F3, map_next)
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
