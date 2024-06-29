import dnfunc as dn

# -----in----- #
epname = dn.fname(__file__)
desc_h = 544

ED = 88210

epis = dn.source(f"./in/{epname}.mkv")
epis = epis.std.CropRel(top=132, bottom=132)
# ------------ #

# ----mrgc---- #
epis_ef = epis.edgefixer.Continuity(top=2, bottom=2)
aaep = dn.aa(epis_ef, desc_h=desc_h)

mrgc = aaep
# ------------ #

# ----mask---- #
mrgc = dn.rfs_image(mrgc, epis_ef, maskname="1", maps=[(2040, 2230)])

stabilize = dn.qtgmc(aaep)
mrgc = dn.rfs_image(mrgc, stabilize, "e2 51454", [(51244, 51454)])

mrgc = dn.rfs(mrgc, stabilize, [(52673, 52780)])
hard_1 = dn.hard(mrgc, mthr=3)
mrgc = dn.rfs_image(mrgc, hard_1, "e2 52762", [(52673, 52780)])

mrgc = dn.rfs(mrgc, stabilize, [(54493, 54786)])
hard_2 = dn.hard(mrgc, mthr=9)
mrgc = dn.rfs_image(mrgc, hard_2, "e2 54493v2", [(54493, 54786)])
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
    rt_sigma=0.8,
    out_mode=0,
):
"""

F0 = dn.filt(epis, db_thr=0)

F1 = dn.filt(mrgc)
F2 = dn.filt(mrgc, mrgc=epis_ef, sm_thr=200, db_thr=3, db_mode=1)

F1 = dn.rfs(F1, F2, [(87997, 88125), (88220, 97967), (97968, 98183)])
# ------------ #

# ----out----- #
clip = dn.out(F1, epname)
clip.set_output()
# ------------ #

# ----save---- #
# dn.pw4(mrgc, 2, 1, epis, clip).set_output()
# epis.set_output()
# clip.std.Trim(96720, epis.num_frames-1).set_output()
# clip.std.Trim(51244, 51454).set_output()
# clip.std.Trim(52673, 52780).set_output()
# clip.std.Trim(54493, 54786).set_output()

# dn.rfs_resc(mrgc, epis, desc_h=desc_h, mthr=50, out_mask=True).set_output()
# ------------ #

# ----err----- #
dn.check_num_frames(epis, clip)
# ------------ #
