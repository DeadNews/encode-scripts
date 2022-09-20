from sys import path

import dnfunc as dn

path.append(".")

epname = "e2"
epis = dn.source(f"./in/{epname}.mp4")

clip = epis.std.CropRel(top=130, bottom=130)

planes = dn.split(clip)

y = planes[0].std.CropRel(top=1, bottom=1).edgefixer.Continuity(top=3, bottom=3, radius=3)

y.set_output()
# clip.set_output()

# 914 12385
