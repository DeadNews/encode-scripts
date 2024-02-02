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
            EDend = dn.chapt(epname, "EDend")

            zone = (
                f"{epname}:"
                f" 0,{OP-1},b=0.40/{OP},{OPend-1},b=0.99/{ED},{EDend-1},b=0.89/{OP-24+77},{OP-24+162},b=0.40"
                f"/{OP-24+318},{OP-24+338},b=0.40/{OP-24+484},{OP-24+520},b=0.40/{OP-24+521},{OP-24+675},b=0.65"
                f"/{OP-24+768},{OP-24+803},b=0.40/{OP-24+841},{OP-24+872},b=0.40/{OP-24+908},{OP-24+1026},b=0.40"
                f"/{OP-24+1027},{OP-24+1285},b=0.65/{OP-24+1456},{OP-24+1531},b=0.40/{OP-24+1569},{OP-24+1653},b=0.40"
                f"/{OP-24+1761},{OP-24+1764},b=0.40/{OP-24+2251},{OPend-1},b=0.76"
            )
            print(zone)

        except (NameError, TypeError):
            print("error")

# #-24
# 77,162
# 318,338
# 484,520
# 521,675 85
# 768,803
# 841,872
# 908,1026
# 1027,1285 85
# 1456,1531
# 1569,1653
# 1761,1764
