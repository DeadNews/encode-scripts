#!/usr/bin/env python
from pathlib import Path

import dnfunc as dn
from yaml import safe_load

if __name__ == "__main__":
    chapters = Path(Path(__file__).parent, "chapters.yaml").read_text()

    for epname in safe_load(chapters):
        try:
            # PreED = dn.chapt(epname, 'ED')
            # ED = dn.chapt(epname, 'realED', 'ED')
            # EDend = dn.chapt(epname, 'EDend')

            # print(f'{epname}: {ED-PreED}-{ED-PreED+EDend-ED-1439}-2')

            OP = dn.chapt(epname, "OP")
            OPend = dn.chapt(epname, "Part_A")
            ED = dn.chapt(epname, "realED", "ED")
            EDend = dn.chapt(epname, "EDend")

            zone = f"{epname}: {OP},{OPend - 1},b=0.96/{ED},{EDend - 1},b=0.4"
            print(zone)

        except (NameError, TypeError):
            print("err")
