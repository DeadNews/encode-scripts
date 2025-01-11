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
                f" {OP},{OP + 1842 - 24},b=0.40/{OP + 1843 - 24},{OP + 2038 - 24},b=0.88/{OP + 2039 - 24},{OPend - 1},b=0.40"
                f"/{ED},{EDend - 1},b=0.80"
            )
            print(zone)

        except (NameError, TypeError):
            ED = dn.chapt(epname, "ED")
            EDend = dn.chapt(epname, "EDend")

            zone = f"{epname}: {ED},{EDend - 1},b=0.80"
            print(zone)
