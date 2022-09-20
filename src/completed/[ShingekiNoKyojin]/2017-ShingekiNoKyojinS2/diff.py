#!/usr/bin/env python
from os import chdir, path
from sys import argv

import dnfunc as dn

chdir(path.dirname(__file__))

# ----diff---- #
for epname in argv[1:]:

    OP = dn.chapt(epname, "OP")
    OPend = dn.chapt(epname, "Part_A")
    Part_B = dn.chapt(epname, "Part_B")
    ED = dn.chapt(epname, "ED")
    EDend = dn.chapt(epname, "EDend", "Next")
    Next = dn.chapt(epname, "Next")
    T1 = dn.chapt(epname, "T1")
    T2 = dn.chapt(epname, "T2")
    EOF = dn.chapt(epname, "EOF")

    jpn = dn.source(f"./in/{epname}.mp4")
    usa = dn.source(f"./in/usa/{epname}.mp4")[24:]

    rfs_map = [
        (OP, OPend - 1),
        (ED, EDend - 1),
        (OPend, OPend + 120),
        (Part_B - 120, Part_B),
        (Next, T1),
        (T2, EOF - 1),
    ]

    # # e12
    # rfs_map = [
    #     (OP, OPend - 1),
    #     (ED, EOF - 1),  # no next
    #     (OPend, OPend + 120),
    #     (Part_B - 120, Part_B),
    # ]

    dn.pv_diff(jpn, usa, name=epname, exclude_ranges=rfs_map)
