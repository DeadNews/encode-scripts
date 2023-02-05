#!/usr/bin/env python
from pathlib import Path

import dnfunc as dn
from yaml import safe_load

if __name__ == "__main__":
    chapters = Path(Path(__file__).parent, "chapters.yaml").read_text()

    for epname in safe_load(chapters):
        try:
            OP = dn.chapt(epname, "OP")
            OPend = dn.chapt(epname, "OPend", "Part_A")
            ED = dn.chapt(epname, "ED")
            EDend = dn.chapt(epname, "EDend", "Part_C")

            zone = f"{epname}: {OP},{OPend-1},b=0.90/{ED},{ED+1691-24},b=0.70/{ED+1691-24+1},{EDend-1},b=0.80/{ED+58-24},{ED+307-24},b=0.80"
            print(zone)

        except (NameError, TypeError):
            try:
                OP = dn.chapt(epname, "OP")
                OPend = dn.chapt(epname, "OPend", "Part_A")

                zone = f"{epname}: {OP},{OPend-1},b=0.90"
                print(zone)

            except (NameError, TypeError):
                print("err")
