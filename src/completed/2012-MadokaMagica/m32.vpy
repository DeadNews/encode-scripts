import dnfunc as dn

# -----in----- #
epname = dn.fname(__file__)
epis = dn.source(f"./in/{epname}.mp4")
# ------------ #

# ----out----- #
clip = dn.out(epis, epname).std.AssumeFPS(fpsnum=24000, fpsden=1001)
clip.set_output()
