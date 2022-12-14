import dnfunc as dn
from lvsfunc import demangle

# -----in----- #
epname = dn.fname(__file__)

OP = dn.chapt(epname, "OP")
OPend = dn.chapt(epname, "Part_A")
Part_B = dn.chapt(epname, "Part_B")
ED = dn.chapt(epname, "ED")
# EDend = dn.chapt(epname, "EDend", "Next")
Next = dn.chapt(epname, "Next")
EOF = dn.chapt(epname, "EOF")

epis = dn.source(f"./in/{epname}.mp4")
# ------------ #

# -----ef----- #
epis, epis_back, _ = dn.edgefix(epis)
epis = dn.rfs(epis, epis_back, (1182, 1221))
# ------------ #

# ----mrgc---- #
# aa
mrgc = dn.aa(epis, zone="yuv")
# dehalo+ sharp
mrgc = dn.rfs_dehalo(mrgc)
mrgc = dn.rfs_sharp(mrgc)
mrgc = dn.rfs_dehalo(mrgc, zone="2nd")
# chroma
mrgc = demangle(mrgc, radius=6)
mrgc = dn.dehalo_chroma(mrgc, zone="uv")

# nc
aanc = dn.aa(epis)
aanc = dn.rfs_resc(aanc, epis)

# mrgc
mrgc = dn.rfs(mrgc, aanc, [(OP, OPend - 1), (EOF - 361, EOF - 1)])

# fix op
mrgc = dn.rfs_qtgmc(mrgc, mrgc, maps=[(86, 648)])

# ed titles
epis_dehalo = dn.rfs_dehalo(epis)
epis_dehalo = dn.rfs_dehalo(epis_dehalo)
mrgc = dn.rfs_resc(mrgc, epis_dehalo, maps=[(ED, EOF - 1)])
# ------------ #

# ----filt---- #
F1 = dn.filt(mrgc)
F2 = dn.filt(mrgc, zone="op")

F1 = dn.rfs(F1, F2, (OP, OPend - 1))
# ------------ #

# ----out----- #
clip = dn.out(F1, epname)
clip.set_output()
# ------------ #

# ----save---- #
# dn.pw(mrgc, None, None, epis_back, clip).set_output()
# dn.pw(mrgc, [2, 3, 4, 6], 'main', epis_back, clip).set_output()
"""
2: 66934
"""
# epis.set_output()
# dn.rfs_resc(epis=epis, out_mask=True).set_output()
# ------------ #

# ----err----- #
dn.check_num_frames(epis, clip)
# ------------ #
