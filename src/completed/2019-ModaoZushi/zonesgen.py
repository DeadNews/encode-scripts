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
            ED = dn.chapt(epname, "ED")
            EDend = dn.chapt(epname, "Next", "EOF")

            zone = (
                f"{epname}: {OP},{OPend},b=0.65/{ED},{EDend},b=0.60/{ED+58-24},{ED+289-24},b=0.40"
            )
            print(zone)

        except (NameError, TypeError):
            print("err")
