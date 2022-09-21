import dnfunc as dn


def ext_nc(epname):
    jpn = dn.source(f"./in/{epname}.mp4")
    ita = dn.source(f"./in/ita/{epname}.mp4")

    return dn.average([jpn, ita])
