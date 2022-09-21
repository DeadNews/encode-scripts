#!/usr/bin/env python
from os import chdir, path

import dnfunc as dn

chdir(path.dirname(__file__))

# ----diff---- #
epname = "e1"

try:
    src1 = dn.source(f"./in/{epname}.mp4")
    src2 = dn.source(f"./in/usa/{epname}.mp4")[171:]

    dn.pv_diff(src1, src2, name=epname, thr=72)
    # dn.pv_diff(src1, src2, name=epname, thr=100)

    print(epname, "done")

except Exception as e:
    print(epname, "err", e)
