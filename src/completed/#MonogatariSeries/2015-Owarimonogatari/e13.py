import dnfunc as dn

# -----in----- #
epname = dn.fname(__file__)
desc_h = 720

OP = 4531
OPend = 5970
ED = 34047

epis = dn.source(f"./in/{epname}.mkv")
EDend = epis.num_frames - 50
# ------------ #

# ----mrgc---- #
ed = dn.oped(epis, name="ed2", offset=12, start=ED, end=EDend, desc_h=desc_h)

aaep = dn.aa(epis, desc_h=desc_h)

mrgc = aaep.std.Trim(0, ED - 1) + ed + aaep.std.Trim(EDend, epis.num_frames - 1)
# ------------ #

# ----mask---- #
mrgc = dn.rfs_qtgmc(mrgc, aaep, maps=[(7512, 7550), (9369, 9416)])

stabilize = dn.qtgmc(mrgc)
mrgc = dn.rfs_image(mrgc, stabilize, "e13 29009-2", [(29009, 29208)])

mrgc = dn.rfs_hard(mrgc, mrgc, mthr=20, maps=[(9369, 9416), (20632, 20651), (7512, 7550)])
mrgc = dn.rfs_hard(
    mrgc,
    mrgc,
    mthr=99,
    maps=[
        (7749, 7808),
        (11289, 11324),
        (14733, 14768),
        (17578, 17601),
        (18523, 18669),
        (22433, 22469),
    ],
)

hard_def = dn.hard(mrgc, mthr=2)
mrgc = dn.rfs_image(
    mrgc,
    hard_def,
    "e13 7227",
    [(7227, 7511), (7809, 8072), (8766, 8887), (9195, 9368), (9417, 9677)],
)
mrgc = dn.rfs_image(mrgc, hard_def, "e13 14769", [(14769, 14804)])
mrgc = dn.rfs_image(mrgc, hard_def, "e13 19076", [(19075, 19152)])
mrgc = dn.rfs_image(mrgc, hard_def, "e13 19153", [(19153, 19254)])
mrgc = dn.rfs_image(mrgc, hard_def, "e13 20984", [(20984, 21059)])
mrgc = dn.rfs_image(mrgc, hard_def, "e13 21060", [(21060, 21061)])
mrgc = dn.rfs_image(mrgc, hard_def, "e13 25694", [(25694, 25840), (26292, 26354)])
mrgc = dn.rfs_image(mrgc, hard_def, "e13 26355", [(26355, 26433)])
mrgc = dn.rfs_image(mrgc, hard_def, "e13 26458", [(26458, 26565)])
mrgc = dn.rfs_image(
    mrgc, hard_def, "e13 27109", [(27109, 27369), (27625, 28074), (28458, 28684), (28715, 28933)]
)
mrgc = dn.rfs_image(mrgc, hard_def, "e13 29009", [(29009, 29208)])

hard_desc = dn.hard(epis, desc_h=desc_h, mthr=4)
mrgc = dn.rfs_image(mrgc, hard_desc, "e13 21385", [(21350, 21385)])
# ------------ #

# ----filt---- #
"""
def filt_old(
    mrgc=mrgc,
    sm_thr=50,
    tr=48,
    pref=1,
    cs_mode=99,
    cs_val=0.55,
    db_thr=1.1,
    db_mode=3,
    db_det=64,
    db_grain=48,
    db_range=15,
    db_saveblack=2,
    rt_sigma=0.9,
    out_mode=0,
):
"""

F1 = dn.filt(mrgc)
F2 = dn.filt(mrgc, sm_thr=45, db_thr=1, rt_sigma=0.8)
F3 = dn.filt(mrgc, rt_sigma=0.8, db_saveblack=0)
F4 = dn.filt(mrgc, sm_thr=44, db_thr=1, rt_sigma=0.7)
F5 = dn.filt(mrgc, sm_thr=38, db_thr=1, rt_sigma=0.6, db_grain=40)
F6 = dn.filt(mrgc, sm_thr=300, db_thr=6, db_mode=1, rt_sigma=4, db_det=128)
F7 = dn.filt(mrgc, db_mode=1)

F1 = dn.rfs(
    F1, F2, [(OP, OPend - 1), (14322, 14357), (21494, 21536), (27391, 27411), (28934, 28973)]
)
F1 = dn.rfs(F1, F3, [(ED, EDend - 1 - 24)])
F1 = dn.rfs(F1, F4, [(23493, 23540)])
F1 = dn.rfs(F1, F5, [(22703, 22762), (23355, 23408), (23775, 23792)])
F1 = dn.rfs(
    F1,
    F7,
    [
        (22433, 22576),
        (25667, 25693),
        (26694, 26783),
        (27370, 27390),
        (28351, 28457),
        (28685, 28714),
    ],
)

F1 = dn.rfs_image(F1, F6, "e13 10812", [(10812, 10997), (11037, 11213), (11325, 11642)])
# ------------ #

# ----out----- #
clip = dn.out(F1, epname)
clip.set_output()
# ------------ #

# ----save---- #
# dn.pw4(mrgc, 2, 1, epis, clip).set_output()
# epis.set_output()
# clip.std.Trim(22391, 25004).set_output()

# dn.rfs_resc(mrgc, epis, desc_h=desc_h, mthr=50, out_mask=True).set_output()
# ------------ #

# ----err----- #
dn.check_num_frames(epis, clip)
# ------------ #
