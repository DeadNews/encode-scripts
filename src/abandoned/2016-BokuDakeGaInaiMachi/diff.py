#!/usr/bin/env python
from os import chdir, path
from sys import argv

import dnfunc as dn

chdir(path.dirname(__file__))

# ----diff---- #
for epname in argv[1:]:

    try:
        src1 = dn.source(f"./in/{epname}.mp4")
        # src1 = dn.source(f"./in/{epname}.mp4")[:1940]
        src2 = src1.std.CropRel(top=130, bottom=130).std.AddBorders(top=130, bottom=130)

        # dn.pv_diff(src1, src2, name=epname, thr=72)
        dn.pv_diff(src1, src2, name=epname, thr=100)

        print(epname, "done")

    except Exception as e:
        print(epname, "err", e)
