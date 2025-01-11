#!/usr/bin/env python
from pathlib import Path

import dnfunc as dn
from yaml import safe_load

if __name__ == "__main__":
    chapters = Path(Path(__file__).parent, "chapters.yaml").read_text()

    for epname in safe_load(chapters):
        try:
            ED = dn.chapt(epname, "ED")
            EDend = dn.chapt(epname, "EDend", "Next")

            zone = f"{epname}: {ED},{ED + 875},b=0.50"
            print(zone)

        except (NameError, TypeError):
            print("err")
