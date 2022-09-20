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

            zone = f"{epname}: {OP},{OPend},b=0.99/{OP},{OP+282},b=0.50/{OP+1294},{OP+1398},b=0.90/{ED},{EDend},b=0.99/{ED+112},{ED+399},b=0.98"
            print(zone)

        except (NameError, TypeError):
            print("err")
