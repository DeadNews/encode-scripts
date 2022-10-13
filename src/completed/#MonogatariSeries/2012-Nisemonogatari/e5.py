import dnfunc as dn

# -----in----- #
epname = dn.fname(__file__)
desc_h = 720

ED = 32609
EDend = 34766

epis = dn.source(f"./in/{epname}.mkv")
# ------------ #

# ----mrgc---- #
ed = dn.oped(epis, name="ed3", offset=12, start=ED, end=EDend, desc_h=desc_h)

aaep = dn.aa(epis, desc_h=desc_h)

mrgc = aaep.std.Trim(0, ED - 1) + ed + aaep.std.Trim(EDend, epis.num_frames - 1)
# ------------ #

# ----mask---- #
mrgc = dn.rfs_hard(mrgc, mrgc, mthr=20, maps=[(17863, 17895), (20777, 20801), (22197, 22223)])
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
F2 = dn.filt(mrgc, db_mode=1)
F3 = dn.filt(mrgc, db_mode=2)
F4 = dn.filt(mrgc, sm_thr=100)
F5 = dn.filt(mrgc, sm_thr=35, db_thr=1, rt_sigma=0.7)
F6 = dn.filt(mrgc, sm_thr=35, db_thr=1, rt_sigma=0.7, db_saveblack=0)
F7 = dn.filt(mrgc, sm_thr=35, db_thr=1, rt_sigma=0.7, db_grain=8, db_range=5)
F8 = dn.filt(mrgc, db_saveblack=0)

F1 = dn.rfs(F1, F2, [(0, 60), (30931, 31110)])
F1 = dn.rfs(
    F1,
    F3,
    [
        (22167, 22196),
        (22778, 22896),
        (30677, 30930),
        (31290, 31565),
        (31810, 32138),
        (32344, 32409),
    ],
)
F1 = dn.rfs(F1, F4, [(31678, 31809)])
F1 = dn.rfs(
    F1,
    F5,
    [(8246, 8419), (10117, 10284), (11099, 11140), (11658, 11687), (15191, 15303), (17683, 17754)],
)
F1 = dn.rfs(F1, F7, [(15115, 15159), (15362, 15409)])
F1 = dn.rfs(F1, F8, [(22981, 23100), (24552, 24641)])
F1 = dn.rfs_image(F1, F6, "crop2", [(3959, 3970), (10063, 10117), (12594, 12623)])
# ------------ #

# ----out----- #
clip = dn.out(F1, epname)
clip.set_output()
# ------------ #

# ----save---- #
# dn.pw4(mrgc, 2, 1, epis, clip).set_output()
# epis.set_output()
# clip.std.Trim(0, 3000).set_output()

# dn.rfs_resc(mrgc, epis, desc_h=desc_h, mthr=50, out_mask=True).set_output()
# ------------ #

# ----err----- #
dn.check_num_frames(epis, clip)
# ------------ #
