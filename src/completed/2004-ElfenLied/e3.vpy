import dnfunc as dn
from lvsfunc import demangle

# -----in----- #
epname = dn.fname(__file__)

OP = dn.chapt(epname, "OP")
OPend = dn.chapt(epname, "Part_A")
Part_B = dn.chapt(epname, "Part_B")
ED = dn.chapt(epname, "ED")
EDend = dn.chapt(epname, "EDend", "Next")
Next = dn.chapt(epname, "Next")
EOF = dn.chapt(epname, "EOF")

epis = dn.source(f"./in/{epname}.mp4")
epis = epis.std.FreezeFrames(first=23186, last=23186, replacement=23187)
# ------------ #

# -----ef----- #
epis, epis_back, _ = dn.edgefix(epis)
epis = dn.rfs(epis, epis_back, [(ED, EDend - 1), (1182, 1221)])
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
mrgc = dn.rfs(
    mrgc,
    aanc,
    [(OP, OPend - 1), (ED, EDend - 1), (Next, Next + 47), (EOF - 361, EOF - 1)],
)

# fix op
mrgc = dn.rfs_qtgmc(mrgc, mrgc, maps=(86, 648))
# ------------ #

# ----filt---- #
F1 = dn.filt(mrgc)
F2 = dn.filt(mrgc, zone="op")
F3 = dn.filt(mrgc, zone="ed")

F1 = dn.rfs(F1, F2, (OP, OPend - 1))
F1 = dn.rfs(F1, F3, (ED, EDend - 1))
# ------------ #

# ----out----- #
clip = dn.out(F1, epname)
clip.set_output()
# ------------ #

# ----save---- #
# dn.pw(mrgc, None, None, epis_back, clip).set_output()
# dn.pw(mrgc, [2, 3, 4, 6], 'main', epis_back, clip).set_output()
"""
"""
# epis.set_output()
# dn.rfs_resc(epis=epis, out_mask=True).set_output()
# ------------ #

# ----err----- #
dn.check_num_frames(epis, clip)
# ------------ #
