import dnfunc as dn

# -----in----- #
epname = dn.fname(__file__)

jpn = dn.source(f"./in/{epname}.mp4")
ita = dn.source(f"./in/ita/{epname}.mp4")
usa = dn.source(f"./in/usa/{epname}.mp4")

ita = (
    ita.std.Trim(0, 125725 - 1)
    + jpn.std.Trim(125725, 139708 - 1)
    + ita.std.Trim(139094, 145674 - 1)
    + jpn.std.Trim(146288, 152769 - 1)
    + ita.std.Trim(152155, ita.num_frames - 1)
)
usa = (
    usa.std.Trim(0, 125725 - 1)
    + jpn.std.Trim(125725, 139708 - 1)
    + usa.std.Trim(139094, 145674 - 1)
    + jpn.std.Trim(146288, 152769 - 1)
    + usa.std.Trim(152155, usa.num_frames - 1)
)

epis = dn.average([jpn, ita, usa, ita, usa, jpn, usa, ita, jpn])
# ------------ #

# -----ef----- #
epis, epis_back, _ = dn.edgefix(epis)
# ------------ #

# ----mrgc---- #
aaep = dn.aa(epis)

mrgc = dn.rfs_resc(aaep, epis)

mrgc = dn.rfs_resc(mrgc, epis, maps=[(4599, 7035)], zone="op")  # op
mrgc = dn.rfs(mrgc, epis_back, [(146288, 152769 - 1)])  # ed
# ------------ #

# ----filt---- #
F1 = dn.filt(mrgc)
# ------------ #

# ----out----- #
clip = dn.out(F1, epname)
clip.set_output()
# ------------ #

# ----save---- #
# dn.pw(mrgc, None, None, epis_back, clip).set_output()
# dn.pw(mrgc, None, None, jpn, clip).set_output()
# dn.pw(mrgc, [2, 3, 4, 6], 'main', epis_back, clip).set_output()
"""
1:
2: 119236 119812 122692 122980 6360 155180 160364
2: aa 9240
6:
"""
# epis.set_output()
# dn.rfs_resc(epis=epis, out_mask=True).set_output()
# ------------ #

# ----err----- #
dn.check_num_frames(epis, clip)
# ------------ #
