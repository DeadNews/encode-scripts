#!/usr/bin/env python
from pathlib import Path

import dnfunc as dn
from yaml import safe_load

if __name__ == "__main__":
    chapters = Path(Path(__file__).parent, "chapters.yaml").read_text()

    for epname in safe_load(chapters):
        try:
            OP = dn.chapt(epname, "OP")
            OPend = dn.chapt(epname, "OPend")
            ED = dn.chapt(epname, "ED")
            EDend = dn.chapt(epname, "EDend")

            zone = (
                f"{epname}:"
                f" {OP},{OP+1412},b=0.49/{OP+1413},{OPend-1},b=0.99/{ED},{ED+1352},b=0.49"
                f"/{ED+1353},{ED+1451},b=0.99/{ED+1452},{ED+1760},b=0.49/{ED+1761},{ED+1864},b=0.99/{ED+1865},,b=0.49"
            )
            # zone=f'{epname}: {ED},{ED-24+1580},b=0.49/{ED-24+1581},{ED-24+1679},b=0.99/{ED-24+1680},{EDend-1},b=0.49'
            print(zone)

        except (NameError, TypeError):
            print("err")
