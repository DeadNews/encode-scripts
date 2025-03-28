#!/usr/bin/env python
from pathlib import Path

import dnfunc as dn
from yaml import safe_load

if __name__ == "__main__":
    chapters = Path(Path(__file__).parent, "chapters.yaml").read_text()

    for epname in safe_load(chapters):
        try:
            OP = dn.chapt(epname, "OP")
            OPend = dn.chapt(epname, "Part_A")
            Part_B = dn.chapt(epname, "Part_B")
            ED = dn.chapt(epname, "ED")
            EDend = dn.chapt(epname, "EDend", "Next")
            Next = dn.chapt(epname, "Next")
            T1 = dn.chapt(epname, "T1")
            T2 = dn.chapt(epname, "T2")
            EOF = dn.chapt(epname, "EOF")

            zone = (
                f"{epname}:"
                f" {OP},{OPend - 1},b=0.80/{OPend},{OPend + 120},b=0.36"
                f"/{ED},{EDend - 1},b=0.35/{Next},{T1},b=0.36/{T2},{EOF - 1},b=0.36"
            )
            print(zone)

        except (NameError, TypeError):
            OP = dn.chapt(epname, "OP")
            OPend = dn.chapt(epname, "Part_A")
            Part_B = dn.chapt(epname, "Part_B")
            ED = dn.chapt(epname, "ED")
            EDend = dn.chapt(epname, "EDend", "Next")

            zone = f"{epname}: {OP},{OPend - 1},b=0.80/{OPend},{OPend + 120},b=0.36/{ED},{EDend - 1},b=0.35"
            print(zone)
