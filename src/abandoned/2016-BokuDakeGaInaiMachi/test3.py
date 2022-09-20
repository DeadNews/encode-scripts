from sys import path

import dnfunc as dn
from vapoursynth import core

path.append(".")

epname = "e2"
epis = dn.source(f"./in/{epname}.mp4")

clip = epis.std.CropRel(top=130, bottom=130)
clip = clip.std.AddBorders(top=130, bottom=130, color=[4096, 32768, 32768])

mask1 = dn.rfs_color(mask_src=epis, tolerance=2, out_mask=True)
mask2 = dn.rfs_color(mask_src=clip, tolerance=2, out_mask=True)

core.std.Interleave([mask2, mask1]).set_output()
# core.std.Interleave([clip, epis]).set_output()

# 8285
