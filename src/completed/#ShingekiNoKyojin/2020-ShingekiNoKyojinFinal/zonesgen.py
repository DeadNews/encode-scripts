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
            Next = dn.chapt(epname, "Next")

            zone = (
                f"{epname}:"
                f" {OP},{OPend - 1},b=0.60"
                f"/{ED},{EDend - 1},b=0.80/{ED},{ED + 270},b=0.40/{ED + 1333},{ED + 1876},b=0.49/{Next},{Next + 71},b=0.50"
            )
            print(zone)

        except (NameError, TypeError):
            print("err")
