import dnfunc as dn
from vapoursynth import GRAY, core

epis = dn.source("./in/e1.mp4")
Y = core.std.ShufflePlanes(epis, 0, GRAY)
U = core.std.ShufflePlanes(epis, 1, GRAY)
V = core.std.ShufflePlanes(epis, 2, GRAY)

U.set_output()
