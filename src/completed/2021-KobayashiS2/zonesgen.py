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
            EOF = dn.chapt(epname, "EOF")

            zone = f"{epname}: {OP},{OPend},b=0.85/{OP},{OP + 356},b=0.70/{ED},{EDend},b=0.90"
            print(zone)

        except (NameError, TypeError):
            print("err")
