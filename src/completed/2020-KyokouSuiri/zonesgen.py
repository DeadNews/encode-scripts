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
            EDend = dn.chapt(epname, "EDend", "Next")

            zone = f"{epname}: {OP},{OPend},b=0.99/{OP+559-24},{OP+623-24},b=0.90/{ED},{ED+282-24},b=0.89"
            print(zone)

        except (NameError, TypeError):
            try:
                OP = dn.chapt(epname, "OP")
                OPend = dn.chapt(epname, "Part_A")

                zone = f"{epname}: {OP},{OPend},b=0.99/{OP+559-24},{OP+623-24},b=0.90"
                print(zone)

            except (NameError, TypeError):
                try:
                    ED = dn.chapt(epname, "ED")
                    EDend = dn.chapt(epname, "EDend", "Next")

                    zone = f"{epname}: {ED},{ED+282-24},b=0.89"
                    print(zone)

                except (NameError, TypeError):
                    print("err")
