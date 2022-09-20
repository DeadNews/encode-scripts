from vapoursynth import core

epis = core.lsmas.LibavSMASHSource(source="./in/m1.mp4")
clip = core.fmtc.bitdepth(epis, bits=10).std.AssumeFPS(fpsnum=24000, fpsden=1001)

clip.set_output()
