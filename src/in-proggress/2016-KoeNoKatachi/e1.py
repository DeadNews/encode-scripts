import dnfunc as dn

# -----in----- #
epname = dn.fname(__file__)

jpn = dn.source(f"./in/{epname}.mp4")
gbr = dn.source(f"./in/gbr/{epname}.mp4")
usa = dn.source(f"./in/usa/{epname}.mp4")[171:]
fra = dn.source(f"./in/fra/{epname}.mp4")
hkg = dn.source(f"./in/hkg/{epname}.mp4")[48:]

usa = dn.rfs(
    usa,
    jpn,
    maps=[
        (10061, 10108),
        (10193, 10270),
        (10616, 10740),
        (12008, 12117),
        (19155, 19207),
        (43839, 43930),
        (47960, 48027),
        (75367, 75452),
        (75608, 75654),
        (89580, 89646),
        (93784, 93873),
        (93912, 93997),
        (97349, 97363),
        (108045, 108197),
        (114994, 115106),
        (119430, 119477),
        (124368, 124440),
        (134016, 134183),
        (134889, 134952),
        (135015, 135088),
        (135214, 135679),
        (135796, 135956),
        (141492, 141498),
        (141555, 141555),
        (141560, 141563),
        (141566, 141567),
        (141569, 141573),
        (150320, 150415),
        (181215, 186413),
    ],
)

epis = dn.average([jpn, usa, gbr, fra, hkg, usa, jpn, jpn])
# ------------ #

# ----mrgc---- #
epis = dn.crop(epis)[0]

mrgc = epis
# ------------ #

# ----filt---- #
F1 = dn.filt(mrgc)
F2 = dn.filt(mrgc, zone="fireworks")

F1 = dn.rfs(F1, F2, maps=(136223, 145099))
# ------------ #

# ----out----- #
clip = dn.out(F1, epname)
clip.set_output()
# ------------ #

# ----save---- #
# dn.pw(mrgc, None, None, epis, clip).set_output()
# dn.pw(mrgc, [2, 3, 4, 6], "main", epis, clip).set_output()
"""
2: 347024 274466
2: 143248 54768 280792
2: 187920 363370
2: 277262!
6: 798784 817840 831796! 1041076 164308
7: 997203 1000228 1007284 1008292 959334 961350 962358 965382 966390 970422! 1214588 974334
"""
# epis.set_output()
# clip.std.Trim(137479, 137479 + 400).set_output()
# dn.rfs_resc(epis=epis, out_mask=True).set_output()
# ------------ #

# ----err----- #
dn.check_num_frames(epis, clip)
# ------------ #
