import dnfunc as dn

# -----in----- #
epname = dn.fname(__file__)

ep1 = 0
ep2 = 31037
ep3 = 62072
ep4 = 93070
ep5 = 124083
ep6 = 155037
end = 188230

epis = dn.source(f"./in/{epname}.mp4")
# ------------ #

# ----mrgc---- #
aaep = dn.aa(epis)

mrgc = dn.rfs_resc(
    aaep,
    epis,
    mthr=18,
    maps=[
        (666, 681),
        (699, 716),
        (730, 1037),
        (1092, 1151),
        (1213, 1279),
        (1394, 1586),
        (173463, 173525),
    ],
)
# ------------ #

# ----filt---- #
F1 = dn.filt(mrgc)
F0 = dn.filt(epis, db_thr=0, ag_saveblack=2, ag_scaling=12)
F2 = dn.filt(mrgc, sm_thr=80, db_saveblack=2, ag_saveblack=2)
F3 = dn.filt(mrgc, sm_thr=60, db_thr=1.1)
F4 = dn.filt(mrgc, sm_thr=80, db_thr=1.1, rt_sigma=0.6, cs_val=1)

F1 = dn.rfs(
    F1,
    F0,
    [
        (30749, 31046),
        (61785, 62081),
        (92796, 93081),
        (123796, 124094),
        (154750, 155046),
        (188181, 193727),
        (1587, 1597),
        (16326, 16363),
        (173413, 173462),
        (103079, 103127),
        (152086, 152131),
    ],
)
F1 = dn.rfs(F1, F2, [(149100, 149257)])
F1 = dn.rfs(F1, F3, [(89400, 89538), (90847, 90912)])
F1 = dn.rfs(F1, F4, [(60619, 60730)])
# ------------ #

# ----out----- #
clip = dn.out(F1, epname)
clip.set_output()
# ------------ #

# ----save---- #
# dn.pw(mrgc, [1, 2, 3, 4, 5, 6], 'main', epis, clip).set_output()
# dn.pw(mrgc, [1, 2, 3, 4, 5, 6], 'main', epis, clip, 'old').set_output()
"""
aa 179454 180894
---
db 1193101 51941 355381 692813 696653 715853
1331181 1175357 1181117 315309 734093 658405 485278 485350 485662
"""
# epis.set_output()
# clip.std.Trim(188242, 190684).set_output() #ed1
# clip.std.Trim(193176, 193562).set_output() #ed2
# clip.std.Trim(60619, 60868-1).set_output() #fix

# dn.rfs_resc(mrgc, epis, mthr=18, out_mask=True).set_output()
# ------------ #

# ----err----- #
dn.check_num_frames(epis, clip)
# ------------ #
