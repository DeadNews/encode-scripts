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
            EDend = dn.chapt(epname, "Next")

            zone = f"{epname}: {OP},{OPend - 1},b=0.80/{OP + 1092},{OP + 1280},b=0.99/{ED},{ED + 173},b=0.55/{ED + 174},{EDend - 1},b=0.90"
            print(zone)

        except (NameError, TypeError):
            try:
                OP = dn.chapt(epname, "OP")
                OPend = dn.chapt(epname, "Part_A")
                ED = dn.chapt(epname, "ED")
                EDend = dn.chapt(epname, "End")

                zone = (
                    f"{epname}:"
                    f" {OP},{OPend - 1},b=0.80/{OP + 1092},{OP + 1280},b=0.99"
                    f"/{ED},{ED + 173},b=0.55/{ED + 174},{EDend - 1},b=0.90"
                )
                print(zone)

            except (NameError, TypeError):
                print("err")
