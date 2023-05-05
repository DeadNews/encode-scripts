import dnfunc as dn


def get_maps(epname):
    maps = {
        "e1": [(6763, 6819)],
        "e2": [(16232, 16317)],
        "e4": [(3272, 3322), (3356, 3411)],
        "e9": [(3578, 3630), (18415, 18518)],
        "e10": [(26723, 26790)],
        "e14": [(4073, 4174), (4555, 4660)],
        "e15": [(3060, 3168), (3244, 3387)],
        "e17": [(7052, 9305)],
        "e18": [(954, 1005), (17281, 17425), (17673, 17954)],
        "e23": [(2971, 3141), (4082, 4277)],
        "e24": [(3520, 3572)],
    }

    try:
        m = []
        for r in maps[epname]:
            start, end = r
            m.append((start - 6, end + 6))

    except Exception:
        return None
    else:
        return m


def ext_nc(epname):
    if epname == "op2":
        jpn = dn.source(f"./in/{epname}.mp4")
        ita = dn.source(f"./in/ita/{epname}.mp4")
        ita = (
            ita[24:]
            .std.DuplicateFrames(324)
            .std.DuplicateFrames(324)
            .std.DeleteFrames(927)
            .std.DeleteFrames(927)
        )
        ita = dn.rfs(ita, jpn, [(324, 433)])

        return dn.average([jpn, ita, jpn, ita, jpn, ita, jpn, ita, jpn, ita])

    if epname == "ed1":
        jpn = dn.source(f"./in/{epname}.mp4")
        ita = dn.source(f"./in/ita/{epname}.mp4")[27:].std.AssumeFPS(fpsnum=24000, fpsden=1001)
        usa = dn.source(f"./in/usa/{epname}.mp4")[24:].std.AssumeFPS(fpsnum=24000, fpsden=1001)

    else:
        jpn = dn.source(f"./in/{epname}.mp4")
        ita = dn.source(f"./in/ita/{epname}.mp4")[24:].std.AssumeFPS(fpsnum=24000, fpsden=1001)
        usa = dn.source(f"./in/usa/{epname}.mp4")[24:].std.AssumeFPS(fpsnum=24000, fpsden=1001)

    return dn.average([jpn, ita, usa, ita, jpn, ita, jpn, jpn])


def opname(epname):
    ep_num = int(epname[1:])

    return "op1" if ep_num in list(range(1, 13 + 1)) else "op2"


def edname(epname):
    ep_num = int(epname[1:])

    return "ed1" if ep_num in range(1, 13 + 1) else "ed2"
