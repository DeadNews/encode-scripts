#!/usr/bin/env python
from pathlib import Path

import dnfunc as dn
from yaml import safe_load

if __name__ == "__main__":
    chapters = Path(Path(__file__).parent, "chapters.yaml").read_text()

    for epname in safe_load(chapters):

        try:
            OP = dn.chapt(epname, "OP")
            OPend = dn.chapt(epname, "Episode")
            ED = dn.chapt(epname, "ED")
            EDend = dn.chapt(epname, "Epilogue", "EOF")

            zone = f"{epname}: {OP},{OPend},b=0.90/{ED},{EDend},b=0.89"
            print(zone)

        except (NameError, TypeError):
            print("err")