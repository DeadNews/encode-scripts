#!/usr/bin/env python
from os import chdir
from pathlib import Path
from sys import argv

import dnfunc as dn

chdir(Path(__file__).parent)

# ----diff---- #
for epname in argv[1:]:
    try:
        OP = dn.chapt(epname, "OP")
        OPend = dn.chapt(epname, "Part_A")
        Part_B = dn.chapt(epname, "Part_B")
        ED = dn.chapt(epname, "ED", "ED+Next")
        EDend = dn.chapt(epname, "EDend", "Next")
        Next = dn.chapt(epname, "Next")
        Ti = dn.chapt(epname, "Ti")
        EOF = dn.chapt(epname, "EOF")

        jpn = dn.source(f"./in/{epname}.mp4")
        usa = dn.source(f"./in/usa/{epname}.mp4")[24:]

        if all(v is not None for v in [OP, OPend, Part_B, ED, EDend, Next]):
            rfs_map = [
                (OP, OPend - 1),
                (ED, EDend - 1),
                (OPend, OPend + 120),
                (Part_B - 120, Part_B),
                (Next, Next + 119),
            ]

        elif all(v is not None for v in [OPend, Part_B, ED, EDend, Next]):
            rfs_map = [
                (ED, EDend - 1),
                (OPend, OPend + 120),
                (Part_B - 120, Part_B),
                (Next, Next + 119),
            ]

        elif all(v is not None for v in [OP, OPend, Part_B, Next]):
            rfs_map = [
                (OP, OPend - 1),
                (OPend, OPend + 120),
                (Part_B - 120, Part_B),
                (Next, Next + 119),
            ]

        elif all(v is not None for v in [OP, OPend, Part_B, ED, EDend]):
            rfs_map = [
                (OP, OPend - 1),
                (ED, EDend - 1),
                (OPend, OPend + 120),
                (Part_B - 120, Part_B),
            ]

        elif all(v is not None for v in [OP, OPend, Part_B, ED, EOF]):
            rfs_map = [
                (OP, OPend - 1),
                (ED, EOF - 1),
                (OPend, OPend + 120),
                (Part_B - 120, Part_B),
            ]

        dn.pv_diff(jpn, usa, name=epname, exclude_ranges=rfs_map)

        print(epname, "done")

    except Exception as e:
        print(epname, "err", e)
